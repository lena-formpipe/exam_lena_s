from src.player import *
from src.grid import *
from src.pickups import *

# KLART: Flyttat denna klass till en annan fil "state.py"
class GameState:
    """Samla spelets variabler i en klass."""
    def __init__(self):
        # A. Spelaren ska börja nära mitten av rummet.
        # previous --> self.player = Player(2, 1)
        # grid X 36, Y 12, varav första och sista positionen är omgivande vägg.
        self.player = Player(17, 5)
        self.score = 0
        self.inventory = []

        self.g = Grid()
        self.g.set_player(self.player)
        self.g.make_walls()
        randomize(self.g) # pickups.randomize(self.g)


    # G. The floor is lava - för varje steg man går ska man tappa 1 poäng.
    def floor_lava(self):
        self.score -= 1


    # F. Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
    def print_inventory(self):
        if len(self.inventory) == 0:
            print("Inga föremål i listan.")
        elif len(self.inventory) > 0:
            print("Det finns följande föremål i listan: ")
            print(", ".join(self.inventory))


    # parameter in i metoden är antal steg som ska flyttas i riktning x eller y
    def move_player(self, x, y):
        # Kontrollera g (grid)
        maybe_item = self.g.get(self.player.pos_x+x, self.player.pos_y+y)
        self.player.move(x, y)
        # G. The floor is lava, för varje steg man går ska man tappa 1 poäng.
        self.floor_lava()

        if isinstance(maybe_item, Item):
            # we found something, add the value to score
            self.score += maybe_item.value
            print(f"Du har hittat {maybe_item.name}, +{maybe_item.value} poäng.")
            # E. Inventory - alla saker som man plockar upp ska sparas i en lista.
            self.inventory.append(maybe_item.name)
            """Ta bort item från position"""
            self.g.clear(self.player.pos_x, self.player.pos_y)


# flyttat denna till en annan fil
def print_status(game_grid, state):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"Du har {state.score} poäng.")
    print(game_grid)




