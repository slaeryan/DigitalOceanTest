# Implant targeting
Implant targeting can be a useful tool in the attacker's arsenal; instead of developing weaponized malcode that will execute on arbitrary systems, we can take precautions to protect the confidentiality of our payloads while ensuring deployment occurs only on targeted/intended assets.

But we as red teams why should we care about it? This is why:

1. To prevent the accidental breaking of the rules of engagement. This will ensure that the malcode doesn't end being executed on any unintended host which are out of the scope.
1. To hinder the efforts of blue teams trying to reverse engineer the implant on non-targeted assets and thwart analysis on automated malware sandboxes.

Now, APT groups do not care about violating any rules of engagement but their only concern is staying low for as long as possible till their mission is completed. And I believe that this technique could be very useful in their arsenal as reverse engineering an implant on a non-targeted asset should be non-trivial. As a bonus point, they could wipe the implant off the disk if the host is not the intended target.

That way there shall be no forensic artifacts left to recover for the analysts.

Okay, but how do we implement this?

Using something known as an environmental keying factor which could be any network/host specific identifier that is found out previously by reconnoitering the target. This factor need not even be private. 

By hard-coding that value in the implant and comparing it at runtime, we can verify whether the executing host is the intended target or not.

One problem that arises from this approach is that it would be trivial to extract that identifier from the binary if left in a plaintext format using strings.

So why don’t we hash it? And compare the hashes at runtime instead of the original string?

I have a working implementation of this technique and the name of the project is FALCONSTRIKE.
Link: https://github.com/slaeryan/FALCONSTRIKE

FalconZero(Loader implant of project FALCONSTRIKE) uses the hostname as the environmental keying factor, hashes it using MD5 algorithm and what’s more? It even encrypts that hash using XOR before hard-coding it to thwart all kinds of static analysis. Should the checks fail, the implant shall not execute on the host at all.

# Using social media as C2
So I was reading the report by FireEye on the Russian state-sponsored cyber operator team - APT 29 and their malware named HAMMERTOSS tDiscoverer. What it did was generate seemingly “random” Twitter handles periodically and use commands embedded in a tweeted image from that handle for C&C.

Basically, their motto is to mimic human behaviour so as not to get caught by next-gen network security solutions.

Naturally, it caught my eye due to the unconventional C2 channel used by them. I mean sure we have seen social media being used as C2 in real-life by APTs such as the "alleged" Indian Patchwork team led by Phronesis Intelligence Ltd. (alleged) but we don’t really see it often though I am sure there are many other undocumented cases.

Anyway, I decided to create a quick prototype in Python 3 demonstrating the implant’s capabilities and also added some extra features. The name of the project is LARRYCHATTER.
Link: https://github.com/slaeryan/LARRYCHATTER

First I want to start with the Twitter Handle Generation algorithm, what I’ve made is a simple pseudo-random string generator. In other words, not really random but possible to predict with the correct seed. I’ve used the current date as the seed after hashing it and extracting some characters out of the hash. The LP and the Implant will be kept in sync through the use of this algorithm. The end result is that it’s quite difficult to predict the Twitter handle using statistical analysis unlike some DGAs(Domain Generation Algorithm) without reverse-engineering the implant first which as we all know here may not be child’s play increasing the longevity of the Implant on a host machine.

Now, assume the operator wants to communicate with the agent on say day 'X', they will have to register that handle on Twitter beforehand and of course, only they would know what the handle for day 'X' should be. After that, they will use the CommandPost to send their desired command which is first encrypted and then embedded in an image before it is tweeted from that handle.

The Implant/agent generates a Twitter handle every 24 hours and checks if it is a registered one and if so then it will visit the profile, download the image, decode the encrypted text embedded steganographically, decrypt the text to get the command and perform that routine.

This way nothing has to be hard-coded on the Implant side which increases its resiliency to account take-downs and ensures Implant longevity on a host machine.

The Implant side is based on web-scraping so as to avoid hard coding any API keys on the Implant side. I use BeautifulSoup library to scrape the image from the Twitter handle and then proceed to extract the embedded encrypted command from the image, decrypt it and then proceed to perform the intended action on the host. All of this happens without dropping any files to the disk.

One important thing to note is that Twitter is just an example here and it may be potentially changed as the attacker sees fit after performing reconnaissance on the target. I am aware that many Governmental organisations block access to social media from the premises but would probably not block access to something as legitimate and benign as VirusTotal/Github/Dropbox etc. So the attacker could utilise these legitimate sites to fetch secondary payloads and load them for in-memory execution without touching the disk.



