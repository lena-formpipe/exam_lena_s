from src.grid import * # Grid
from src import player #Player
from src.state import * # GameState
# from src import pickups
from src.pickups import *

# KLART: Flyttat denna klass till en annan fil "state.py"
#class GameState:
    #Samla spelets variabler i en klass.
    #def __init__(self):
        # self.player = Player(17, 5)
        # self.score = 0
        # self.inventory = []

        # self.g = Grid()
        # self.g.set_player(self.player)
        # self.g.make_walls()
        # pickups.randomize(self.g)"""

# KLART: flytta denna till en annan fil
#def print_status(game_grid, state):
    #Visa spelvärlden och antal poäng.
    #print("--------------------------------------")
    #print(f"You have {state.score} points.")
    #print(game_grid)


def start(state):
    command = "a"
    # Loopa tills användaren trycker Q eller X.
    # inventory = []          # LS E.	Inventory - alla saker som man plockar upp ska sparas i en lista.
    while not command.casefold() in ["q", "x"]:
        print_status(state.g, state)
        # LS: denna skriver ut innehållet i positionen, till exempel om det är en vägg så visar den det.
        position_content = state.g.get(state.player.pos_x, state.player.pos_y)
        print(position_content)

        command = input("Use WASD to move, Q/X to quit. Or I to print inventory list of items found.")
        command = command.casefold()[:1]
        x= state.player.pos_x   # LS
        y= state.player.pos_y   # LS

        if command == "d" and state.player.can_move(x + 1, y, state.g):  # move right
            # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
            # Kontrollera g (grid)
            print("du får flytta höger") # LS
            maybe_item = state.g.get(state.player.pos_x + 1, state.player.pos_y)
            # LS *******************  C.Man ska inte kunna gå igenom väggar.
            # if maybe_item == state.g.wall:                                          # LS
            #    print("du träffar en vägg nu, så du måste välja annan riktning...") # LS
            state.player.move(1, 0)
            state.floor_lava()

            if isinstance(maybe_item, Item):   # isinstance(maybe_item, pickups.Item):
                # we found something
                state.score += maybe_item.value
                print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                # LS E.	Inventory - alla saker som man plockar upp ska sparas i en lista.
                state.inventory.append({maybe_item.name})
                print(len(state.inventory)) # TODO ta bort denna rad
                print(state.inventory[-1])    # TODO ta bort denna rad
                #g.set(player.pos_x, player.pos_y, g.empty)
                state.g.clear(state.player.pos_x, state.player.pos_y)
        elif command == "i":
            state.print_inventory()


    # Hit kommer vi när while-loopen slutar
    print("Thank you for playing!")


# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    start(game_state)
