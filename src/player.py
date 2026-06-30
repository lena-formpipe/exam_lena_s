
class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y


    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        self.pos_x += dx
        self.pos_y += dy


    # C.Man ska inte kunna gå igenom väggar.
    @staticmethod
    def can_move(x, y, grid):  #  def can_move(self, x, y, grid)
        this_content = grid.get(x, y)
        if this_content == grid.wall:
            print("Du kan inte flytta eftersom du går in i en vägg!")  # LS
            return False
        else:
            return True
        # returnera True om det inte står något i vägen



