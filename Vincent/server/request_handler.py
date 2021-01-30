import socket
# from _thread import *
import threading 
import time
from .player import Player
from .game import Game
from queue import Queue

def player_thread(connectionSocket,ip, name):
    pass
    


def authentication(connectionSocket, ip):
    try:
        # some  authentication
        data = connectionSocket.recv(16).decode()
        name = str(data)
        if not name:
            raise Exception(" NO name received")
        connectionSocket.sendall("Autentication successful! You are in the game now".encode())
    except Exception as e:
        print(e)
        connectionSocket.sendall(str(e).encode())
        connectionSocket.close()# close the connection
    
    player_thread(connectionSocket,ip, "")

def connection_thread():
    server = ""
    port = 2333
    localHost = socket.gethostbyname()
    try:
         #create an INET, STREAMing socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print ('Socket sucreated')
    except socket.error as err:
        print (f"socket creation failed with error {err}")
           
    try:
        s.bind((server, port))
    except socket.error as e:
        print(str(e))

    s.listen()
    print("waiting for connections, server started... ")

    while True:
        clientSocket, addr = s.accept()
        print("new incommming connection")

        threading.Thread(target = authentication, args = (clientSocket, addr))




if __name__ == "__main__":
    threading.Thread(target= connection_thread)
