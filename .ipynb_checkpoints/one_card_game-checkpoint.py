# Gracze otrzymują jedną kartę, 
# porównanie wartości kart
# koniec gry i zwycięstwo karty wyższej. 


import karty
import gry

class BJ_Card(karty.Card):
    """ Karta do blackjacka. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v