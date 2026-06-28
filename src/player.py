from src.grid import Grid


class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        self.pos_x += dx # horisontell förflyttning, vänster till höger
        self.pos_y += dy # vertikal förflyttning, uppifrån och ned

    def can_move(self, x, y, grid):
        # LS *******************  C.Man ska inte kunna gå igenom väggar.
        # print(f"\n\n{x} \n\n{y} en grid \n{grid} slut grid")
        this_content = grid.get(x, y)
        print(f"innehållet i positionen är: {this_content}")
        if this_content == grid.wall:  # LS
            print("Du träffar en vägg nu, så du måste välja annan riktning...")  # LS
            return False
        else:
            return True
        #KLART: returnera True om det inte står något i vägen


