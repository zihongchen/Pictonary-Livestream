
class Player(object):
    def __init__(self, connSocket, ip, name):
        self.connSocket = connSocket
        self.ip = ip
        self.name = name
        self.score = 0
        self.game = None
        self.game_id = None

    def update_score(self, x):
        self.score += x

    def guess(self, wrd):
        return self.game.player_guess(self, wrd)

    def disconnect(self):
        self.game.player_disconnected(self)





    def get_score(self):
        return self.score
    
    def get_name(self):
        return self.name

    def get_ip(self):
        return self.ip

    def assign_game(self,game_id):
        self.game_id = game_id
        return None
