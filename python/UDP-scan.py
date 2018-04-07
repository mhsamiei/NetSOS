from socket import *

host = "127.0.0.1"
s2 = socket(AF_INET, SOCK_DGRAM)

for port in range(10, 65535):
    try:
        data = "Hello"
        #print "Try "+str(port)
        s2.sendto(data.encode(),(host,port))
        s2.settimeout(0)
        print ((s2.recvfrom(1024)))
        break
    except Exception as e:
        print(e)
        pass
