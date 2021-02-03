"""
connect players, rounds, chat, board

"""


from .player import Player
from .board import Board
from .round import Round
from .chat import Chat
import random
class Game(object):
    def __init__(self, id, players):
        self.id = id
        self.players = players
        self.word_idx = 0
        self.drawer_idx = 0
        self.round = None
        self.board = None
        self.chat = None
        self.round = None
        self.word_used = set()


      


        # components
        self.start_new_board()
        self.start_new_round()
        self.start_new_chat()


    def player_guess(self,player, guess_msg):

        self.round.guess(player, guess_msg)
        
        if guess_msg != self.round.word:
            msg = player.name+": "+ guess_msg
            self.round.chat.update_chat(msg)
        

        

    def player_disconnected(self,player):
        if player in self.players:
            self.players.remove(player)

            # TODO
            #REVIEW
            # deal with player_idx

        else:
            raise Exception("player not exist")        

        if len(self.players < 2):
            self.end_game()



    def skip(self):
        if not self.round:
            self.round.skip()
        else:
            raise Exception("The round has not started yet")



    def start_new_chat(self):
        self.chat = Chat()
        return None

    
    def start_new_board(self):
        self.board = Board()
        return None


    def update_board(self, player, x: int, y: int, color: tuple) -> None:
        self.board.update(x, y, color)
    

    def start_new_round(self):
        self.board.clear()
        #FIXME
        word = self.word_pool[self.word_idx]
        self.word_idx += 1
        player_drawing = self.players[self.drawer_idx]
        self.drawer_idx += 1
        if self.drawer_idx >= len(self.players):
            self.end_round()
            self.end_game()


        
        all_players = self.players
        self.round = Round(word, player_drawing, all_players)


    def end_round(self):
        self.start_new_round()
        pass
    
    def end_game(self):
        for player in self.players:
            self.round.player_left(player)
        

    def assign_players(self):
        for player in self.players:
            player.assign_game(self.id)

    def add_player(self, player):
        if self.round == None:
            self.players.append(player)
        else:
            print("game has started")
    

    def get_Words(self):
        # after shuffling, just pop from the end
        words = []

        with open("words.txt", 'r') as f:
            for line in f:
                wrd = line.strip()
                if wrd not in self.word_used:
                    self.word_used.add(wrd)

                    words.append(wrd)
#FIXME

            return words[r].strip()

