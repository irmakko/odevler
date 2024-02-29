import datetime
import socket 
host = socket.gethostname()
port = 5000  

server_socket = socket.socket()  
   

server_socket.bind((host, port))  

server_socket.listen(2)
conn, address = server_socket.accept()
while True:
    print("Dinliyorum")
    
    data =conn.recv(1024).decode()
    conn.close()
    time=datetime.datetime.now()
    print(f'Alındı: '+data+" ("+str(time.strftime("%H:%M"))+")")
    break