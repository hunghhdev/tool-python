from queue import Queue
import threading
import socket


target = input('Input a remote host to scan: ')

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        con = s.connect((target, port))
        print('Port :', port, " is open.")
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.deamon = True
    t.start()

for worker in range(1, 65535):
    q.put(worker)

q.join()

