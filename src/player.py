from src.grid import Grid


class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        # maybe_wall = state.g.get(x, y)
        # LS *******************  C.Man ska inte kunna gå igenom väggar.
        print(f"\n\n{x} \n\n{y} en grid \n{grid} slut grid")
        this_content = grid.get(x, y)
        print(f"innehållet i positionen är: {this_content}")
        if this_content == grid.wall:  # LS
            print("KOD FRÅN PLAYER du träffar en vägg nu, så du måste välja annan riktning...")  # LS
        #    return False
        else:
            return True
        #TODO: returnera True om det inte står något i vägen


