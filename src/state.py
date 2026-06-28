
from src.player import *  # Player
from src.pickups import *
from src.grid import *


# KLART: Flyttat denna klass till en annan fil "state.py"
class GameState:
    """Samla spelets variabler i en klass."""
    def __init__(self):
        # klart
        # A. Spelaren ska börja nära mitten av rummet.
        # previous --> self.player = Player(2, 1)
        # grid X 36, varav första och sista är vägg. 34/2 = 17
        # grid Y 12, varav första och sista är vägg. 10/2 = 5
        self.player = Player(17, 5)
        self.score = 0
        self.inventory = []

        self.g = Grid()
        self.g.set_player(self.player)
        self.g.make_walls()
        randomize(self.g) # pickups.randomize(self.g)

    def floor_lava(self):
        self.score -= 1
        print(f"You have {self.score} points.")

    def print_inventory(self):
        print("längden på listan är:")
        print(len(self.inventory))
        if len(self.inventory) == 0:
            print("No items in list.")
        elif len(self.inventory) > 0:
            print("there are items in list: ")
            for item in self.inventory:
                print(item)


# klart flyttat denna till en annan fil
def print_status(game_grid, state):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {state.score} points.")
    print(game_grid)