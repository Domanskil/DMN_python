# Gracze otrzymują jedną kartę, 
# porównanie wartości kart
# koniec gry i zwycięstwo karty wyższej. 


import karty
import gry

class Game_Card(karty.Card):


    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v == 1:
                v = 14
        
        return v


class Game_Deck(karty.Deck):
    
class Game_Hand(karty.Hand):

class Player(Game_Hand):
    
     def lose(self):
        print(self.name, "przegrywa.")

    def win(self):
        print(self.name, "wygrywa.")

    def push(self):
        print(self.name, "remisuje.")

class Game(object):
    
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = Player(name)
            self.players.append(player)

        self.deck = Game_Deck
        self.deck.populate()
        self.deck.shuffle()


    def play(self):
        # rozdaj każdemu początkowe dwie karty
        self.deck.deal(self.players, per_hand = 1)
           
        for player in self.players:
            print(player)

        