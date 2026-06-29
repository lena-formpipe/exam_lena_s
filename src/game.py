
from src.state import * # GameState

def start(state):
    command = "a"
    # Loopa tills användaren trycker Q eller X.
    while not command.casefold() in ["q", "x"]:
        print_status(state.g, state)
        print("Använd följande tangenter:\n- WASD för att förflytta dig, \n- Q/X för att avsluta spelet,\n- I för att skriva ut inventarielistan.")
        command = input("Din input:")
        command = command.casefold()[:1]

        # C.Man ska inte kunna gå igenom väggar --> se tillägget AND can_move()
        # # klart: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
        if command == "d" and state.player.can_move(state.player.pos_x + 1, state.player.pos_y, state.g):  # move right
            state.move_player(1, 0)

        elif command == "s" and state.player.can_move(state.player.pos_x, state.player.pos_y+1, state.g):  # move down
            state.move_player(0, 1)

        elif command == "w" and state.player.can_move(state.player.pos_x, state.player.pos_y-1, state.g):  # move down
            state.move_player(0, -1)

        elif command == "a" and state.player.can_move(state.player.pos_x-1, state.player.pos_y, state.g):  # move down
            state.move_player(-1, 0)

        # F. Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
        elif command == "i":
            state.print_inventory()

    # Hit kommer vi när while-loopen slutar
    print("Tack för att du spelat!")


# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    start(game_state)