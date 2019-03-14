'''
Created on 21 feb 2019

@author: a.airaghi
'''

import sys
import threading
import time
import clilib


class sentinella(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.fermo=1
        self.avanti=0
    def run(self):
        while 1:
            while clilib.ricevuti.empty()==False:
                msg=clilib.ricevuti.get()
                if msg.find('pos')>=0:
                    print(clilib.decodificapos(msg))
            
            time.sleep(0.5)
            clilib.comando('1r')
   
if __name__ == '__main__':
    thread2 = sentinella(2, "sentinella")
    thread2.start()









