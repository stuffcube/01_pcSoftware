'''
Created on 29/set/2017

@author: a.airaghi
'''
import socket
import time
import sqlite3 as lite

def letturadb(id='PAAA'):
    con = lite.connect('arianna.db3', isolation_level=None)  
    cur = con.cursor()
    cur.execute("""select angolo_rel,dist*10 from radar where id='"""+id+"""'  order by angolo_rel""")
    rec=cur.fetchall()
    letture=[]
    for i in rec:
        letture.append("echo-"+str(int(i[0]))+"-"+str(int(i[1]))+"-"+str(int(i[1]))+"-"+str(int(i[1]))+"-"+str(int(i[1]))+"-"+str(int(i[1]))+"-"+str(int(i[1])))
        #punti.append([i[0],i[1]])
    return letture


 
def Main():
    host = "127.0.0.1"
    port = 8181
    stato=0
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    cont=0
    contrit=0
    test=0
    data=''
    time.sleep(5)
    dati2="!pos: 0;0;0;6.32;0;0;0;0;0 ?"
    conn.send(dati2.encode())
    while True:
            if test==0:
                dati2="!pos: 0;0;0;6.32;0;0;0;0 ?"
                misura1='150'
            if test==1:
                dati2="!pos: 0;1000;0;6.32;0;0;0;0 ?"
                misura1='50'
            conn.send(dati2.encode())
            data=''
            dati2=''
            cont+=1
            conn.settimeout(0)
            try:
                data = conn.recv(1024)
                
                if not data:
                    break

            except:
                pass;
            if str(data).find("!1qyy")>=0:
                for i in range(30 , 60, 5):
                    dati2="!xxxxxxxxxxxxxxxxxxxx?"
                    conn.send(dati2.encode())
                time.sleep(1)
                dati2="!echf?"
                conn.send(dati2.encode())
           
            if str(data).find("!1q")>=0:
                xxxx=str(data)
                ang1=int(xxxx[5:8])
                ang2=int(xxxx[8:11])
                step=int(xxxx[11:13])
                if ang2<ang1:
                    step=step*-1
                messaggio='echo-ang-misu-misu-misu-misu-misu-misu-misu-misu-'
                messaggioinv=''
                print("angoli",ang1,ang2)
                for ixx in range (ang1,ang2,step):
                    messaggioinv=''
                    messaggioinv=messaggio.replace('ang',str(ixx))
                    if ixx==90:
                        messaggioinv=messaggioinv.replace('misu',misura1)
                    else:
                        messaggioinv=messaggioinv.replace('misu',misura1)
                    dati2="!"+messaggioinv+"?"
                    conn.send(dati2.encode())
                    time.sleep(0.3)
                dati2="!echf?"
                conn.send(dati2.encode())
                dati2=''
                test=1
            
            if str(data).find("!1r")>=0:
                
                print("richiesta stato",str(data)[5:7])
                if contrit==0:
                    dati2="!r: 0;"+str(data)[5:7]+"?"
                    conn.send(dati2.encode())
                    dati2=''
                if contrit!=0:
                    dati2="!r: 0;"+str(data)[5:7]+"?"
                    conn.send(dati2.encode())
                    dati2=''

            if str(data).find("!3R")>=0 or str(data).find("!3D") >=0 :
                print("sono qui")
                if contrit==0:
                    contrit=20
                data=''
            if contrit>0 and contrit<15:        
                dati2="!pos: "+str(cont)+";"+str(1000+contrit)+";1000;0;0;0;0;0;=;0 ?"
                contrit-=1
            elif contrit>=15:
                contrit-=1
            else:
                pass;
                #dati2="!pos: "+str(cont)+";1000;1000;1 ?"
            #print(dati2)
            conn.send(dati2.encode())
            dati2=''
            time.sleep(2)

             
    conn.close()


     
if __name__ == '__main__':
    Main()
    