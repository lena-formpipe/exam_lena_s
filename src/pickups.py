
class Item:
    """Representerar saker man kan plocka upp."""
    # default ges value = 10
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

# D. Fruktsallad - alla frukter ska vara värda 20 poäng i stället för 10.
# skapa två listor, listan med frukt value = 20, samt att jag sätter symbol = "!" på icke-frukt för att enklare kunna testa :-)
# slå sedan ihop listorna till en enda lista som heter pickups.
pickups_fruits = [Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon")]
for item in pickups_fruits:
    item.value = 20
pickups_other = [Item("carrot", symbol="!"), Item("radish", symbol="!"), Item("cucumber", symbol="!"), Item("meatball", symbol="!")]
for item in pickups_other:
    item.symbol = "!"
pickups = pickups_fruits + pickups_other

def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

