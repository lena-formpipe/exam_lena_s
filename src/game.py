from src.grid import *
# from src import player #Player
from src.state import * # GameState
# from src import pickups
from src.pickups import *

def start(state):
    command = "a"
    # Loopa tills användaren trycker Q eller X.
    while not command.casefold() in ["q", "x"]:
        print_status(state.g, state)
        # LS: denna skriver ut innehållet i positionen, till exempel om det är en vägg så visar den det.
        position_content = state.g.get(state.player.pos_x, state.player.pos_y) #TODO remove
        print(position_content)

        command = input("Use WASD to move, Q/X to quit. Or I to print inventory list of items found.")
        command = command.casefold()[:1]

        # LS *******************  C.Man ska inte kunna gå igenom väggar, se tillägget AND can_move()
        # # klart: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
        if command == "d" and state.player.can_move(state.player.pos_x + 1, state.player.pos_y, state.g):  # move right
            print("flyttar D")
            state.find_item(1, 0)

        elif command == "s" and state.player.can_move(state.player.pos_x, state.player.pos_y+1, state.g):  # move down
            print("flyttar S")
            state.find_item(0, 1)

        elif command == "w" and state.player.can_move(state.player.pos_x, state.player.pos_y-1, state.g):  # move down
            print("flyttar W")
            state.find_item(0, -1)

        elif command == "a" and state.player.can_move(state.player.pos_x-1, state.player.pos_y, state.g):  # move down
            print("flyttar A")
            state.find_item(-1, 0)

        # F. Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
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

def find_any_item(pos_x, pos_y):
    find_item = state.g.get(pos_x + 1, pos_y)
    # G. The floor is lava - för varje steg man går ska man tappa 1 poäng.
    state.floor_lava()

    if isinstance(find_item, Item):  # isinstance(maybe_item, pickups.Item):
        # we found something
        # metod i state där score och inventory tillhör
        state.score += find_item.value
        print(f"You found a {find_item.name}, +{find_item.value} points.")
        # LS E.	Inventory - alla saker som man plockar upp ska sparas i en lista.
        state.inventory.append({find_item.name})
        # g.set(player.pos_x, player.pos_y, g.empty)
        state.g.clear(state.player.pos_x, state.player.pos_y)