'''
Created on 10/apr/2018

@author: a.airaghi
'''

import config as cfg
from tkinter import  Button,Text,END,scrolledtext,NE
import time
import arianna_utility
import urllib3
from tkinter.constants import FIRST

headers = {"User-agent": "Mozilla/5.0"}
http = urllib3.PoolManager()

#===============================================================================
# gui
#===============================================================================


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Arianna")
        master.geometry('500x700')
        self.msglog = scrolledtext.ScrolledText(master, height=10, width=50)
        self.msglog.pack()
        self.msglog2 = scrolledtext.ScrolledText(master, height=10, width=50)
        self.msglog2.pack()
        self.msglog3 = scrolledtext.ScrolledText(master, height=10, width=50)
        self.msglog3.pack()
        self.comandi = Text(master, height=1, width=50)
        self.comandi.pack()
        self.inviacmd= Button(master,text='InviaCMD',command = self.clicked)
        self.inviacmd.pack()
        self.btn2= Button(master,text='btn2',command = '')
        self.btn2.pack()
        self.inviacmd.place(relx=1, x=-200, y=670, anchor=NE)
        self.btn2.place(relx=1, x=-100, y=670, anchor=NE)
        #self.master.bind('<Return>', self.clicked2)
        self.comandi.bind('<Return>',self.clicked)
        if cfg.simu==0:
            self.aggiungi2("mod simulazione")
        if cfg.simu==1:
            self.aggiungi2("mod normale")
        if cfg.simu==2:
            self.aggiungi2("ip statico")
        
    
    def aggiungi(self,testo):
        self.msglog.insert(END, testo)
        self.msglog.see(END)
        
    def aggiungi2(self,testo):
        self.msglog2.insert(END, testo)
        self.msglog2.see(END)
    def aggiungi3(self,testo):
        self.msglog3.insert(END, testo)
        self.msglog3.see(END)

            
    def clicked(self,evt=''):
        #messagebox.showinfo( "Hello Python", self.comandi.get("1.0",END))
        #=======================================================================
        # if self.comandi.get("1.0",END)[:2]!='1i':
        #     cfg.messaggirx.put((time.time(),self.comandi.get("1.0",END)))
        # else:
        #     arianna_utility.registratore(self.comandi.get("1.0",END)[2:])
        #=======================================================================
        b=self.comandi.get("1.0",END).rstrip()
        b=b.strip('\n')
        b=b.strip('\r')
        a='http://127.0.0.1:8081/comandi_ui?nome=''&valore=1&cod='+b
        print (a,"-")
        r = http.request('GET',a )
        self.comandi.delete("1.0", END)
        self.comandi.focus()
        print(r.data)
    
    def start(self):
        self.master.mainloop()


