import socket 
import datetime
host = socket.gethostname()  
port = 5000  

client_socket = socket.socket()  
client_socket.connect((host, port))  
def sendmsg(text):
         client_socket.send(text.encode())
        

sendmsg("Merhaba Dünya!")
