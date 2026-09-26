import marimo

__generated_with = "0.24.0"
app = marimo.App(width="columns")


@app.cell
def _(i, locations):
    # # Simple game about traveling to different places. 
    # I want to make a grid of random place names, like a chess board. Than maybe a Dice roll for distance and choice of direction. 
    # Location will have random points 1-3, and after five rolls the player with most points wins. 

    # print the dict as a grid. decided to use f-string. Manual writing sucks.
    # if_player should be added to dictionary, based on location. Can I edit the dict value? 
    # my_dict.update({'key1': 'value1', 'key2': 'value2'})

    #lg('2a')
    # for key, value in locations.items():
    #     print(f"{key}: {value}")

    #print(locations, end = '\n')

    # Written by Domanskil

    # import gry
    import random

    """
    Od początku.

    Klasa Locations = Stół, siatka, podłoga. Współrzędne, na których układane są kafelki gry i po których poruszają się gracze. 
    [coord][tile][if_player]
    Tutaj aktualizowana i rysowana co rundę jest siatka gry. 
    Kafelek zostaje odwrócony i taki pozostaje, kiedy przyjdzie gracz. 
    Obecność gracza odwracalna-tylko do wyświetlania.


    Kafelek wyświetlany i obracany raz przez pierwszego gracza. 

    Gracz - pozycja, punkty, ruch. Zwraca zmienną, która modyfikuje wartość [if_player]. 



    """



    class Player(object):  # obrobić!!! ---  Pseudokod

        def __init__(self, name, p_number, score =0, location = None):
            self.score = score
            self.name = name
            self.p_pnum = f"p{p_number}"
            self._location = location


        @property 
        def location(self):

            return self._location


        @location.setter
        def location(self, location):
            self._location = location
            return self._location

        # def move(self, direction =  None, roll = 2):

        #     while direction not in ["u", "d", "l", "r"]:
        #         direction = input("""Which direction do you want to move?
        #         "u" - up
        #         "d" - down
        #         "l" - left
        #         "r" - right
        #         ...?""")
        #         return direction

        #     if direction == "u":
        #         self.loc = self.loci.locations[1][-roll * 5]  # to jest zła składnia
        #     if direction == "d":
        #         self.loc = self.loci.locations[1][+roll * 5]  # to jest zła składnia
        #     if direction == "l":
        #         self.loc = self.loci.locations[1][-roll]  # to jest zła składnia
        #     if direction == "r":
        #         self.loc = self.loci.locations[1][+roll]  # to jest zła składnia

        #     return self.loc
    class Tile(object):

        def __init__(self, i, p1 = False, p2 = False, p3 = False, p4 = False, vis = False):
            self._vis = vis
            self.i = i
            self.p1 = p1
            self.p2 = p2
            self.p3 = p3
            self.p4 = p4
    
        def __str__(self):
            self.i = i if self._vis else "X"
            self.if_p1 = "A" if self.p1 else " "
            self.if_p2 = "B" if self.p2 else " "
            self.if_p3 = "C" if self.p3 else " "
            self.if_p4 = "D" if self.p4 else " "
            return self.i, self.if_p1, self.if_p2, self.if_p3, self.if_p4
    
        @property
        def tile(self, p1 = False, p2 = False, p3 = False, p4 = False, vis = False):
            tile = [i, self.if_p1, self.if_p2, self.if_p3, self.if_p4, self._vis]
            return tile

        @tile.setter
        def tile(self, p1, p2, p3, p4, vis):
            self._vis = vis
            self.p1 = p1
            self.p2 = p2
            self.p3 = p3
            self.p4 = p4


    # Ściąga z czata
    # class Element:
    #     def __init__(self, hp):
    #         self.hp = hp


    # class Plansza:
    #     def __init__(self):
    #         self.pola = [
    #             [Element(100), Element(100), Element(100)],
    #             [Element(100), Element(100), Element(100)],
    #             [Element(100), Element(100), Element(100)]
    #         ]

    # plansza = Plansza()

    # plansza.pola[1][2].hp = 50
    

    class Locations(object): 
        """game grid"""

        def __init__(self):
            locations = []
            loc_numbers = ['1','2','3','4','5']
            loc_letters = ['a','b','c','d','e']
            values = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3]
            random.shuffle(values)
            for i in loc_numbers:
                for j in loc_letters:
                    locations.append(i+j)

            tiles = []
            for num in values:
                tile = Tile(i = num)
                tiles.append(tile)
            self.loci = []
            for num in range(0, 25):
                self.loci.append([locations[num], tiles[num]])
            
        def tile_flip(self, tile):
            tile._vis = True

        def show_player(self, tile):
            for player in self.players:
                if player.location == tile.loc:
                    tile.p_pnum = True
        
        def hide_player(self, tile):
            tile.p_pnum = False


        def player_present(self):
            for player in self.players:
                for tile in locations.loci:
                    if player.location == locations.loci[0]: #na przykład tak. Jeszcze nie ma tej zmiennej
                        tile_flip(tile)
                        show_player(tile)


        @property
        def grid(self):
    
            lc = self.loci
    
            grid = (f"""
                |- - - -|- - - -|- - - -|- - - -|- - - -|
                |{lc[0][0]}-{lc[0][1].i}  -|{lc[1][0]}-{lc[1][1].i}  -|{lc[2][0]}-{lc[2][1].i}  -|{lc[3][0]}-{lc[3][1].i}  -|{lc[4][0]}-{lc[4][1].i}  -| 
                |{lc[0][1].p1}-{lc[0][1].p2}-{lc[0][1].p3}-{lc[0][1].p4}|
                |- - - -|- - - -|- - - -|- - - -|- - - -|
        
            """)
                        
            return grid



    class Game(object): #rewrite all vars!

        def __init__(self, players):
    
            self.locations = Locations()
            self.players = players

        # def player_update(self):
        #     for loc in self.loci.locations[0].keys(): #ok
        #         for player in self.players:
        #             if loc == player.location:
        #                 print(player.name, "found!", loc)
        #                 self.loci.locations[0].get(f'{loc}') # nie działa
        #                 # update inaczej!!!
        #                 print(self.loci.locations[0][loc])


        def play(self):
            round_count = 0
            while round_count < 2:

                for player in self.players:
                    print(player.name, "points:", player.score)
                    player.location = '3c' #ok
                    print(player.location)

                # print(self.players)
                #print(self.locations.loci)
           #     self.player_update()
                print(self.locations.grid) #ok
                round_count +=1 #ok



    def main(): # rewrite all vars!


   



        players = []
        num_players = None
        while num_players not in range(2,4):
            num_players = int(input("How many players are there? (2-4):"))
        for i in range(1 , num_players+1):
            player = Player(name = input(f"What is the {i}. player's name?:"), p_number = i)

            players.append(player)

        print(players)
        game = Game(players)

        again = None

        while again != 'n':

            game.play()
            again = input("Do you want to play again? y/n: ")

    main()
    input("Press enter to exit")
    return


@app.cell
def _():
    return


@app.cell
def _():
    # game = Game()
    return


@app.cell
def _():
    # p1 = Player
    # p1.location = '2a'
    # grid = Grid()
    # # p1 = Player
    # # p1.location = '2a'
    # print(grid)
    return


@app.cell
def _():
    # p1.move("r")
    # p1.location
    return


if __name__ == "__main__":
    app.run()
