
class Item:
    """Representerar saker man kan plocka upp."""
    # default antas vara en frukt
    def __init__(self, name, value=20, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

# D. Fruktsallad - alla frukter ska vara värda 20 poäng i stället för 10.
# initiera icke-frukter med värde = 10 och jag har även gett dem en annan symbol för att enklare testa.
pickups = [Item("carrot", value=10, symbol="!"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish", value=10, symbol="!"), Item("cucumber", value=10, symbol="!"), Item("meatball", value=10, symbol="!")]


def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

