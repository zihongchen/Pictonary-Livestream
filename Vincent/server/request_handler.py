import socket
# from _thread import *
import threading 
import time
from .player import Player
from .game import Game
from queue import Queue
import json
PLAYERS = 8
class Server(object):
    def __init__(self):    
        self.connection_queue = []
        self.localHost = socket.gethostbyname()
        self.gameId = 0
            

    def player_thread(self,connectionSocket,ip, name):
        while True:
            try:
                send_msg = -2
                data = conn.recv(1024)
                data = json.loads(data)

                # player not part of the game
                key = [ key for key in data.keys()]
                connectionSocket.sendall(json.dumps(send_msg))


            except Exception as e:
                print(f"[EXCEPTION] {player.get_name} disconnected", e)


    def handle_queue(self,player):
        self.connection_queue.append(player)
        if len(self.connection_queue) >= 8:
            # create game
            game = Game(gameId, self.connection_queue)
            self.gameId += 1
            for player in self.connection_queue:
                player.set_game(game, gameId)

            self.connection_queue = []

            




    def authentication(connectionSocket, ip):
        try:
            # TODO authentication process
            data = connectionSocket.recv(16).decode()
            name = str(data)
            if not name:
                raise Exception(" NO name received")
            connectionSocket.sendall("Autentication successful! You are in the game now".encode())
            self.player_thread(connectionSocket,ip, "")
        except Exception as e:
            print(e)
            connectionSocket.sendall(str(e).encode())
            connectionSocket.close()# close the connection
        
        

    def connection_thread(self):
        server = ""
        port = 2333
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
    s = Server()
    threading.Thread(target= s.connection_thread)
