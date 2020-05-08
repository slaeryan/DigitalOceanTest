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


