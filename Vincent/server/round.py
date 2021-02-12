
from .chat import *

import time
import threading

class Round(object):
    ROUND_TIME = 75
    def __init__(self, word, player_drawing, all_players, game):
        self.game = game
        self.end = False
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = set()
        self.skips = 0
        self.player_scores = { player : 0 for player in all_players}
        self.chat = Chat()        
        self.time = Round.ROUND_TIME
        threading.Timer( 1, self.time_thread)
        #start_new_thread
        

    def time_thread(self):
        """
        a thread that keep track pf time
        """
        while(True):
            #self.time_lock.acquire()
            self.time -= 1
            #self.time_lock.release()
            if self.time < 0:
                self.end_round("Time is up")
                return None


    
    def guess(self, player, wrd):
        # we want to write a notification to user
        
        if player == self.player_drawing:
            return None

        if (wrd == self.word):
            if player not in self.player_guessed:
                self.player_guessed.add(player)
                # TODO score system
                self.player.update_score((self.time/Round.ROUND_TIME)*20)
                return player.name+ "guessed correctly"
            else:
                return None
        else:
            return player.name+": "+ wrd
                


    def player_left(self, player_gone):
        """
        remove players left from the round
        """
        if player_gone in self.player_scores:
            del self.player_scores[player_gone]

        if player_gone in self.player_guessed:
            self.player_guessed.remove(player_gone)
        
        if player_gone == self.player_drawing:
            self.end_round("Drawing players leaves")

        if len(self.player_scores) < 2:
            self.end_round("Not enough players")


    def end_round(self, msg):
        self.game.round_ended()
        
    
    def skip(self):
        pass



    def get_all_scores(self):
        return self.player_scores
    
    def get_a_score(self, player):
        if player in self.player_scores:
            return self.player_scores[player]
        else: 
            raise Exception("player not in this round")



