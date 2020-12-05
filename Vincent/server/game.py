"""
connect players, rounds, chat, board

"""


from .player import *
from .board import *
from .round import *

import random
class Game(object):

    def __init__(self, id, players):
        self.id = id
        self.players = players
        self.words_used = ['a', 'b']
        self.board = Board()
        self.round = None


    def player_guess(self,player, guess_msg):

        self.round.guess(player)
        
        if guess_msg != self.round.word:
            msg = player.name+": "+ guess_msg
            self.round.chat.update_chat(msg)
        

    

    def player_disconnected(self,player):
        pass        


    def skip(self):
        pass


    def update_board(self, player, x: int, y: int, color: tuple) -> None:
        if player == self.round.player_drawing
        self.board.update(x, y, color)
    




    def start_new_round(self):
        word = random.choice(self.words_used)
        player_drawing = random.choice(self.players)
        all_players = self.players
        self.round = Round(word, player_drawing, all_players)


    def round_ended(self):
        self.board.clear()
        self.round = None
        pass
        
    def assign_players(self):
        for player in self.players:
            player.assign_game(self.id)