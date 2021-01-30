
from chat import *

import time
import threading

class Round(object):
    ROUND_TIME = 75
    def __init__(self, word, player_drawing, all_players):
        self.end = False
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.player_scores = { player : 0 for player in all_players}
        self.chat = Chat()

        self.time_lock = threading.Lock()
        self.time = self.ROUND_TIME
        threading.Thread(target= self.time_thread)
        #start_new_thread
        

    def time_thread(self):
        """
        a thread that keep track pf time
        """
        while(True):
            time.sleep(1)
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
                self.player_guessed.append(player)
                # TODO score system
                self.time_lock.acquire()
                self.player_scores[player] = self.time
                self.time_lock.release()


    def player_left(self, player_gone):
        """
        remove players left from the game
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
        self.end = True
        pass
    
    def skip(self):
        pass



    def get_all_scores(self):
        return self.player_scores
    
    def get_a_score(self, player):
        if player in self.player_scores:
            return self.player_scores[player]
        else: 
            raise Exception("player not in this round")



