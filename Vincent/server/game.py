"""
connect players, rounds, chat, board

"""


from player import *
from board import *
from round import *

import random
class Game(object):

    def __init__(self, id, players):
        self.id = id
        self.players = players
        self.word_pool = ["apple", "orange", "banana"]
        random.shuffle(self.word_pool)
        self.word_idx = 0
        self.drawer_idx = 0

        self.board = Board()
        self.round = None

        self.start_new_round()


    def player_guess(self,player, guess_msg):

        self.round.guess(player, guess_msg)
        
        if guess_msg != self.round.word:
            msg = player.name+": "+ guess_msg
            self.round.chat.update_chat(msg)
        

    

    def player_disconnected(self,player):
        pass        


    def skip(self):
        if not self.round:
            self.round.skip()
        else:
            raise Exception("The round has not started yet")

    def update_board(self, player, x: int, y: int, color: tuple) -> None:
        self.board.update(x, y, color)
    

    def start_new_round(self):
        self.board.clear()
        word = self.word_pool[self.word_idx]
        self.word_idx += 1
        player_drawing = self.players[self.drawer_idx]
        self.drawer_idx += 1
        if self.drawer_idx >= len(self.players):
            self.end_round()


        
        all_players = self.players
        self.round = Round(word, player_drawing, all_players)


    def end_round(self):
        self.start_new_round()
        pass
    
    def end_game(self):
        pass

    def assign_players(self):
        for player in self.players:
            player.assign_game(self.id)

    def add_player(self, player):
        if self.round == None:
            self.players.append(player)
        else:
            print("game has started")

