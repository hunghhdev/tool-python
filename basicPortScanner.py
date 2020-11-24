import socket
import sys
from datetime import datetime


remoteServer = input("Enter a remote host to scan: ")
remoteServerIp = socket.gethostbyname(remoteServer)


print("-" * 60)
print("Please wait, scanning remote host", remoteServerIp)
print("-" * 60)

t1 = datetime.now()

try:
    for port in range(1,65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIp, port))
        if result == 0:
            print("Port {}: Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print("Scanning Completed in: ", total)



