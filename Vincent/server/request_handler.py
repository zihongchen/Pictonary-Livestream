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
            

    # def player_thread(self,connectionSocket,ip, name):
    #     # while True:
    #     #     try:
    #     #         send_msg = -2
    #     #         data = connectionSocket.recv(1024)
    #     #         data = json.loads(data)

    #     #         # player not part of the game
    #     #         key = [ key for key in data.keys()]
    #     #         connectionSocket.sendall(json.dumps(send_msg))


    #     #     except Exception as e:
    #     #         print(f"[EXCEPTION] {player.get_name} disconnected", e)
    def player_thread(self, conn, player):
        """
        handles in game communication between clients
        :param conn: connection object
        :param ip: str
        :param name: str
        :return: None
        """
        while True:
            try:
                # Receive request
                try:
                    data = conn.recv(1024)
                    data = json.loads(data.decode()) 
                    print("[LOG] Recived data:", data)
                except Exception as e:
                    break


                # Player is not apart of game
                # :param data: dictionary

                keys = [int(key) for key in data.keys()]
                send_msg = {key:[] for key in keys}

                for key in keys:
                    if key == -1:  # get game, returns a list of players
                        if player.game:
                            send = {player.get_name():player.get_score() for player in player.game.players}
                            send_msg[-1] = send
                        else:
                            send_msg[-1] = []

                    if player.game:
                        if key == 0:  # guess
                            correct = player.game.player_guess(player, data['0'][0])
                            send_msg[0] = correct
                        elif key == 1:
                            skip = player.game.skip()
                            send_msg[1] = skip
                        elif key == 2:  # get chat
                            content = player.game.round.chat.get_chat()
                            send_msg[2] = content
                        elif key == 3:  # get board
                            brd = player.game.board.get_board()
                            send_msg[3] = brd
                        elif key == 4:  # get score
                            scores = player.game.get_player_scores()
                            send_msg[4] = scores
                        elif key == 5:  # get round
                            rnd = player.game.round_count
                            send_msg[5] = rnd
                        elif key == 6:  # get word
                            word = player.game.round.word
                            send_msg[6] = word
                        elif key == 7:  # get skips
                            skips = player.game.round.skips
                            send_msg[7] = skips
                        elif key == 8:  # update board
                            x, y, color = data[8][:3]
                            player.game.update_board(x, y, color)
                        elif key == 9:  # get round time
                            t = player.game.round.time
                            send_msg[9] = t


                send_msg = json.dumps(send_msg)
                # TODO why add . here
                conn.sendall(send_msg.encode() + ".".encode())


            except Exception as e:
                print(f"[EXCEPTION] {player.get_name()}:", e)
                break

        print(F"[DISCONNECT] {player.name} DISCONNECTED")
        #player.game.player_disconnected(player)
        conn.close()



    def handle_queue(self,player):
        self.connection_queue.append(player)
        if len(self.connection_queue) >= 8:
            # create game
            game = Game(self.gameId, self.connection_queue)
            self.gameId += 1
            for player in self.connection_queue:
                player.set_game(game, self.gameId)

            self.connection_queue = []

            




    def authentication(self,connectionSocket, ip):
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

            threading.Thread(target = self.authentication, args = (clientSocket, addr))




if __name__ == "__main__":
    s = Server()
    threading.Thread(target= s.connection_thread)
