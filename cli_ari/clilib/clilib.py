'''
Created on 14 mar 2019

@author: a.airaghi
'''
import queue
import threading
import socket
import urllib3

ricevuti=queue.Queue()
sema_glob = threading.Semaphore() 
import time




def comando(testo):
    headers = {"User-agent": "Mozilla/5.0"}
    http = urllib3.PoolManager()
    b=testo.rstrip()
    a='http://127.0.0.1:8081/comandi_ui?nome=''&valore=1&cod='+b
    r = http.request('GET',a )

def decodificapos(pos):
    p=pos.split(":")
    x=p[1].split(";")
    teta=x[3]
    posx=x[1]
    posy=x[2]
    movi=x[6]
    return {'teta': teta, 'posx': posx, 'posy': 'posy', 'movi': movi} 
    


class ricevente(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 10000)
        self.sock.bind(self.server_address)
    def run(self):
        messaggio=""
        self.sock.settimeout(0.1)
        while 1:
            sema_glob.acquire()
            try:
                data, address = self.sock.recvfrom(4096)
                ricevuti.put(data.decode())
            except:
                pass;
            sema_glob.release()
            time.sleep(0.1)


thread1 = ricevente(1, "ascolto")
thread1.start()
    
