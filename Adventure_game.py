import marimo

__generated_with = "0.24.0"
app = marimo.App(width="columns")


app._unparsable_cell(
    """
    # # Simple game about traveling to different places. 
    # I want to make a grid of random place names, like a chess board. Than maybe a Dice roll for distance and choice of direction. 
    # Location will have random points 1-3, and after five rolls the player with most points wins. 

    # print the dict as a grid. decided to use f-string. Manual writing sucks.
    # if_player should be added to dictionary, based on location. Can I edit the dict value? 
    # my_dict.update({'key1': 'value1', 'key2': 'value2'})

    #lg('2a')
    # for key, value in locations.items():
    #     print(f\"{key}: {value}\")

    #print(locations, end = '\\n')

    # Written by Domanskil

    # import gry
    import random

    \"\"\"
    Location - grid 5x5 dictionary {location:value}
        values = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3]
        25pcs, 15x1, 6x2, 4x3.
        locations = {1-5, a-e : random value}


        Hidden reps - after discovery - remain visible
        Random points
        Move options - grid
        More players at the same spot <-nested dict?



    Player - depend on location
        points
        Dice roll - > move direction ->
        Score update    

    Round count

    \"\"\"



    # Class Game (turn counter, player and score display), Locations (all shit happen here), Grid (just display), Player ( move -> locations update, score count)


    class Grid(object):   

        def __init__(self, locations = None):
            self._locations = locations

        @property
        def locations(self):

            return self._locations

        @locations.setter
        def locations(self, locations):
            self._locations = locations
            return self._location

        def __str__(self):

            \"\"\"define alias for function get() to fit the commands on screen :)\"\"\"

            #locations update!!!

            lg = self.locations.get 

            self.grid = (f\"\"\"
                |- - - -|- - - -|- - - -|- - - -|- - - -|
                |{lg('1a')[0]}-    -|{lg('1b')[0]}-    -|{lg('1c')[0]}-    -|{lg('1d')[0]}-    -|{lg('1e')[0]}-    -|
                |{lg('1a')[1]} {lg('1a')[2]} {lg('1a')[3]} {lg('1a')[4]}|{lg('1b')[1]} {lg('1b')[2]} {lg('1b')[3]} {lg('1b')[4]}|{lg('1c')[1]} {lg('1c')[2]} {lg('1c')[3]} {lg('1c')[4]}|{lg('1d')[1]} {lg('1d')[2]} {lg('1d')[3]} {lg('1d')[4]}|{lg('1e')[1]} {lg('1e')[2]} {lg('1e')[3]} {lg('1e')[4]}|
                |- - - -|- - - -|- - - -|- - - -|- - - -|
                |{lg('2a')[0]}-    -|{lg('2b')[0]}-    -|{lg('2c')[0]}-    -|{lg('2d')[0]}-    -|{lg('2e')[0]}-    -|
                |{lg('2a')[1]} {lg('2a')[2]} {lg('2a')[3]} {lg('2a')[4]}|{lg('2b')[1]} {lg('2b')[2]} {lg('2b')[3]} {lg('2b')[4]}|{lg('2c')[1]} {lg('2c')[2]} {lg('2c')[3]} {lg('2c')[4]}|{lg('2d')[1]} {lg('2d')[2]} {lg('2d')[3]} {lg('2d')[4]}|{lg('2e')[1]} {lg('2e')[2]} {lg('2e')[3]} {lg('2e')[4]}|
                |- - - -|- - - -|- - - -|- - - -|- - - -|
                |{lg('3a')[0]}-    -|{lg('3b')[0]}-    -|{lg('3c')[0]}-    -|{lg('3d')[0]}-    -|{lg('3e')[0]}-    -|
                |{lg('3a')[1]} {lg('3a')[2]} {lg('3a')[3]} {lg('3a')[4]}|{lg('3b')[1]} {lg('3b')[2]} {lg('3b')[3]} {lg('3b')[4]}|{lg('3c')[1]} {lg('3c')[2]} {lg('3c')[3]} {lg('3c')[4]}|{lg('3d')[1]} {lg('3d')[2]} {lg('3d')[3]} {lg('3d')[4]}|{lg('3e')[1]} {lg('3e')[2]} {lg('3e')[3]} {lg('3e')[4]}|
                |- - - -|- - - -|- - - -|- - - -|- - - -|
                |{lg('4a')[0]}-    -|{lg('4b')[0]}-    -|{lg('4c')[0]}-    -|{lg('4d')[0]}-    -|{lg('4e')[0]}-    -|
                |{lg('4a')[1]} {lg('4a')[2]} {lg('4a')[3]} {lg('4a')[4]}|{lg('4b')[1]} {lg('4b')[2]} {lg('4b')[3]} {lg('4b')[4]}|{lg('4c')[1]} {lg('4c')[2]} {lg('4c')[3]} {lg('4c')[4]}|{lg('4d')[1]} {lg('4d')[2]} {lg('4d')[3]} {lg('4d')[4]}|{lg('4e')[1]} {lg('4e')[2]} {lg('4e')[3]} {lg('4e')[4]}|
                |- - - -|- - - -|- - - -|- - - -|- - - -|
                |{lg('5a')[0]}-    -|{lg('5b')[0]}-    -|{lg('5c')[0]}-    -|{lg('5d')[0]}-    -|{lg('5e')[0]}-    -|
                |{lg('5a')[1]} {lg('5a')[2]} {lg('5a')[3]} {lg('5a')[4]}|{lg('5b')[1]} {lg('5b')[2]} {lg('5b')[3]} {lg('5b')[4]}|{lg('5c')[1]} {lg('5c')[2]} {lg('5c')[3]} {lg('5c')[4]}|{lg('5d')[1]} {lg('5d')[2]} {lg('5d')[3]} {lg('5d')[4]}|{lg('5e')[1]} {lg('5e')[2]} {lg('5e')[3]} {lg('5e')[4]}|
                |- - - -|- - - -|- - - -|- - - -|- - - -|
                \"\"\")

            return(self.grid)





    class Player(object):  # obrobić!!! ---  Pseudokod

        def __init__(self, name, p_number, score =0, location = None):
            self.score = score
            self.name = name
            self.p_number = f\"p{p_number}\"
            self._location = location


        @property 
        def location(self):

            return self._location


        @location.setter
        def location(self, location):
            self._location = location
            return self._location

        # def move(self, direction =  None, roll = 2):

        #     while direction not in [\"u\", \"d\", \"l\", \"r\"]:
        #         direction = input(\"\"\"Which direction do you want to move?
        #         \"u\" - up
        #         \"d\" - down
        #         \"l\" - left
        #         \"r\" - right
        #         ...?\"\"\")
        #         return direction

        #     if direction == \"u\":
        #         self.loc = self.loci.locations[1][-roll * 5]  # to jest zła składnia
        #     if direction == \"d\":
        #         self.loc = self.loci.locations[1][+roll * 5]  # to jest zła składnia
        #     if direction == \"l\":
        #         self.loc = self.loci.locations[1][-roll]  # to jest zła składnia
        #     if direction == \"r\":
        #         self.loc = self.loci.locations[1][+roll]  # to jest zła składnia

        #     return self.loc



    class Locations(object):

    # Rethink this class. Maybe split into tile and location. Need to know which tile is which, not just list attached to coords. 
        # This is the original. 
    

        # @property
        # def tiles(self, p1 = False, p2 = False, p3 = False, p4 = False, vis = False):

        #     values = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3]
        #     random.shuffle(values)

        #     # player = True


        #     if_p1 = \"A\" if p1 else \" \"
        #     if_p2 = \"B\" if p2 else \" \"
        #     if_p3 = \"C\" if p3 else \" \"
        #     if_p4 = \"D\" if p4 else \" \"
        #     _vis = vis
        #     tiles = []
        #     for i in values:
        #         i = i if __vis else \"X\"
        #         tiles.append([i, if_p1, if_p2, if_p3, if_p4, _vis])

        #     return tiles

        # @tiles.setter
        # def tiles(self, p1, p2, p3, p4, vis):
        #     self._vis = vis
        #     self.p1 = p1 if p1 else False
        #     self.p2 = p2 if p2 else False
        #     self.p3 = p3 if p3 else False
        #     self.p4 = p4 if p4 else False



        # @property
        # def locations(self):

        #     loc_numbers = ['1','2','3','4','5']
        #     loc_letters = ['a','b','c','d','e']
        #     loc_list = []
        #     for i in loc_numbers:
        #         for j in loc_letters:
        #             loc_list.append(i+j)

        #     locations = dict(zip(loc_list, self.tiles))

        #     return locations, loc_list


    class Tiles(object):

        def __init__(self):
            values = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3]
            random.shuffle(values)

            loc_numbers = ['1','2','3','4','5']
            loc_letters = ['a','b','c','d','e']
            loc_list = []
            for i in loc_numbers:
                for j in loc_letters:
                    loc_list.append(i+j)

        

        @property
        def tiles(self, p1 = False, p2 = False, p3 = False, p4 = False, vis = False):

        

            # player = True


            if_p1 = \"A\" if p1 else \" \"
            if_p2 = \"B\" if p2 else \" \"
            if_p3 = \"C\" if p3 else \" \"
            if_p4 = \"D\" if p4 else \" \"
            _vis = vis
            tiles = []
            for i in values:
                i = i if _vis else \"X\"
                tiles.append([i, if_p1, if_p2, if_p3, if_p4, _vis])

            return tiles

        @tiles.setter
        def tiles(self, p1, p2, p3, p4, vis):
            self._vis = vis
            self.p1 = p1 if p1 else False
            self.p2 = p2 if p2 else False
            self.p3 = p3 if p3 else False
            self.p4 = p4 if p4 else False



        @property
        def locations(self):

            # locations = []
            #     for i in loc_list:
            #         for j in values:
            #             locus = [i,j]
            #             locations.append(locus)  to na końcu

            # return locations

    

    





    class Game(object): #rewrite all vars!

        def __init__(self, players):
            self.players = players
            self.loci = Locations()
            self.grid = Grid(self.loci.locations[0])

        def player_update(self):
            for loc in self.loci.locations[0].keys(): #ok
                for player in self.players:
                    if loc == player.location:
                        print(player.name, \"found!\", loc)
                        self.loci.locations[0].get(f'{loc}') # nie działa
                        # update inaczej!!!
                        print(self.loci.locations[0][loc])


        def play(self):
            round_count = 0
            while round_count < 5:
    
                for player in self.players:
                    print(player.name, \"points:\", player.score)
                    player.location = '3c' #ok
                    print(player.location)

                # print(self.players)
                # print(self.loci.locations)
                self.player_update()
                print(self.grid) #ok
                round_count +=1 #ok



    def main(): # rewrite all vars!


   



        players = []
        num_players = None
        while num_players not in range(2,4):
            num_players = int(input(\"How many players are there? (2-4):\"))
        for i in range(1 , num_players+1):
            player = Player(name = input(f\"What is the {i}. player's name?:\"), p_number = i)

            players.append(player)

        print(players)
        game = Game(players)

        again = None

        while again != 'n':

            game.play()
            again = input(\"Do you want to play again? y/n: \")

    main()
    input(\"Press enter to exit\")
    """,
    name="_"
)


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


@app.cell
def _():
    # grid.locations
    return


@app.cell
def _():
    # # ====================================   OLD GRID  ===============================================
    # # print(f"""
    # # |- - - -|- - - -|- - - -|- - - -|- - - -|
    # # |{locations.get('1a')}-    -|{locations.get('1b')}-    -|{locations.get('1c')}-    -|{locations.get('1d')}-    -|{locations.get('1e')}-    -|
    # # |{if_p1} {if_p2} {if_p3} {if_p4}|{if_p1} {if_p2} {if_p3} {if_p4}|{if_p1} {if_p2} {if_p3} {if_p4}|{if_p1} {if_p2} {if_p3} {if_p4}|{if_p1} {if_p2} {if_p3} {if_p4}|
    # values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
    # # |{locations.get('2a')}-    -|{locations.get('2b')}-    -|{locations.get('2c')}-    -|{locations.get('2d')}-    -|{locations.get('2e')}-    -|
    # random.shuffle(values)
    # player = True
    # # |{locations.get('3a')}-    -|{locations.get('3b')}-    -|{locations.get('3c')}-    -|{locations.get('3d')}-    -|{locations.get('3e')}-    -|
    # p1_1 = 'A' if player else ' '
    # if_p1 = p1_1
    # # |{locations.get('4a')}-    -|{locations.get('4b')}-    -|{locations.get('4c')}-    -|{locations.get('4d')}-    -|{locations.get('4e')}-    -|
    # if_p2 = ' '
    # if_p3 = ' '
    # # |{locations.get('5a')}-    -|{locations.get('5b')}-    -|{locations.get('5c')}-    -|{locations.get('5d')}-    -|{locations.get('5e')}-    -|
    # if_p4 = ' '
    # vis = False
    # # """)
    # tiles = []
    # for i in values:
    # # ====================================  OLD TEST CODE  ============================================
    #     tiles.append([i, if_p1, if_p2, if_p3, if_p4, vis])
    # # print(locations.keys())
    # loc_numbers = ['1', '2', '3', '4', '5']
    # # print(tiles)
    # loc_letters = ['a', 'b', 'c', 'd', 'e']
    # # print(tiles[0][0])
    # loc_list = []
    # # print(locations.get('1a')[0])
    # for i in loc_numbers:
    # # locations.get('1a')[0]
    #     for j in loc_letters:
    # # lg('1a')[1:]
    #         loc_list.append(i + j)
    # # ====================================  TEST CODE  ===============================================#
    # locations = dict(zip(loc_list, tiles))
    # lg = locations.get
    # # a = print(locations.get('1a')[0])
    # # b = locations.get('1a')[0]
    # # print(a == b)
    # # False
    # # print(a == print(b))
    # # 1
    # # True
    # print(f"\n            |- - - -|- - - -|- - - -|- - - -|- - - -|\n            |{lg('1a')[0]}-    -|{lg('1b')[0]}-    -|{lg('1c')[0]}-    -|{lg('1d')[0]}-    -|{lg('1e')[0]}-    -|\n            |{lg('1a')[1]} {lg('1a')[2]} {lg('1a')[3]} {lg('1a')[4]}|{lg('1b')[1]} {lg('1b')[2]} {lg('1b')[3]} {lg('1b')[4]}|{lg('1c')[1]} {lg('1c')[2]} {lg('1c')[3]} {lg('1c')[4]}|{lg('1d')[1]} {lg('1d')[2]} {lg('1d')[3]} {lg('1d')[4]}|{lg('1e')[1]} {lg('1e')[2]} {lg('1e')[3]} {lg('1e')[4]}|\n            |- - - -|- - - -|- - - -|- - - -|- - - -|\n            |{lg('2a')[0]}-    -|{lg('2b')[0]}-    -|{lg('2c')[0]}-    -|{lg('2d')[0]}-    -|{lg('2e')[0]}-    -|\n            |{lg('2a')[1]} {lg('2a')[2]} {lg('2a')[3]} {lg('2a')[4]}|{lg('2b')[1]} {lg('2b')[2]} {lg('2b')[3]} {lg('2b')[4]}|{lg('2c')[1]} {lg('2c')[2]} {lg('2c')[3]} {lg('2c')[4]}|{lg('2d')[1]} {lg('2d')[2]} {lg('2d')[3]} {lg('2d')[4]}|{lg('2e')[1]} {lg('2e')[2]} {lg('2e')[3]} {lg('2e')[4]}|\n            |- - - -|- - - -|- - - -|- - - -|- - - -|\n            |{lg('3a')[0]}-    -|{lg('3b')[0]}-    -|{lg('3c')[0]}-    -|{lg('3d')[0]}-    -|{lg('3e')[0]}-    -|\n            |{lg('3a')[1]} {lg('3a')[2]} {lg('3a')[3]} {lg('3a')[4]}|{lg('3b')[1]} {lg('3b')[2]} {lg('3b')[3]} {lg('3b')[4]}|{lg('3c')[1]} {lg('3c')[2]} {lg('3c')[3]} {lg('3c')[4]}|{lg('3d')[1]} {lg('3d')[2]} {lg('3d')[3]} {lg('3d')[4]}|{lg('3e')[1]} {lg('3e')[2]} {lg('3e')[3]} {lg('3e')[4]}|\n            |- - - -|- - - -|- - - -|- - - -|- - - -|\n            |{lg('4a')[0]}-    -|{lg('4b')[0]}-    -|{lg('4c')[0]}-    -|{lg('4d')[0]}-    -|{lg('4e')[0]}-    -|\n            |{lg('4a')[1]} {lg('4a')[2]} {lg('4a')[3]} {lg('4a')[4]}|{lg('4b')[1]} {lg('4b')[2]} {lg('4b')[3]} {lg('4b')[4]}|{lg('4c')[1]} {lg('4c')[2]} {lg('4c')[3]} {lg('4c')[4]}|{lg('4d')[1]} {lg('4d')[2]} {lg('4d')[3]} {lg('4d')[4]}|{lg('4e')[1]} {lg('4e')[2]} {lg('4e')[3]} {lg('4e')[4]}|\n            |- - - -|- - - -|- - - -|- - - -|- - - -|\n            |{lg('5a')[0]}-    -|{lg('5b')[0]}-    -|{lg('5c')[0]}-    -|{lg('5d')[0]}-    -|{lg('5e')[0]}-    -|\n            |{lg('5a')[1]} {lg('5a')[2]} {lg('5a')[3]} {lg('5a')[4]}|{lg('5b')[1]} {lg('5b')[2]} {lg('5b')[3]} {lg('5b')[4]}|{lg('5c')[1]} {lg('5c')[2]} {lg('5c')[3]} {lg('5c')[4]}|{lg('5d')[1]} {lg('5d')[2]} {lg('5d')[3]} {lg('5d')[4]}|{lg('5e')[1]} {lg('5e')[2]} {lg('5e')[3]} {lg('5e')[4]}|\n            |- - - -|- - - -|- - - -|- - - -|- - - -|\n            ")
    return


if __name__ == "__main__":
    app.run()
