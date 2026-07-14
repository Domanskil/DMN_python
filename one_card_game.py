# Gracze otrzymują jedną kartę, 
# porównanie wartości kart
# koniec gry i zwycięstwo karty wyższej. 


import karty
import gry

class Game_Card(karty.Card):


    @property
    def value(self):
        v = Game_Card.RANKS.index(self.rank) + 1
        if v == 1:
            v = 14
        
        return v

class Game_Deck(karty.Deck):
    
    def populate(self):
        for suit in Game_Card.SUITS: 
            for rank in Game_Card.RANKS: 
                self.cards.append(Game_Card(rank, suit))



class Player(karty.Hand):  
    
    
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
    
    def __str__(self):
        rep = self.name + ":\t" + super(Player, self).__str__()  
               
        return rep

    @property
    def total(self):
        t = self.cards[0].value

        return t
    
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

        self.deck = Game_Deck()
        self.deck.populate()
        self.deck.shuffle()


    def play(self):
        
        self.deck.deal(self.players, per_hand = 1)
           
        
        totals = []
        for player in self.players:
            print(player)
            print(player.total)
            totals.append(player.total)
            
            
        totals.sort(reverse = True)
        for player in self.players:
            if player.total == totals[0]:
                player.win()
            else:
                player.lose()
        
        
        totals = []
        # self.players.sort(player.total, reverse = True)
        # print(self.players)


        
        for player in self.players:
            player.clear()



#test
        if len(self.deck.cards) < 26:
            self.shoe.populate()
            self.shoe.shuffle()
            self.deck.cards += self.shoe.cards
            self.shoe.clear()



def main():
    print("\t\tWitaj w grze 'One Card Game'!\n")
    
    names = []
    number = gry.ask_number("Podaj liczbę graczy (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Wprowadź nazwę gracza: ")
        names.append(name)
    print()
        
    game = Game(names)

    again = None
    while again != "n":
        game.play()
        again = gry.ask_yes_no("\nCzy chcesz zagrać ponownie?: ")


main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")