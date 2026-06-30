import random


class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor.
        # Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.player = None
        # istället för x och y används variabelnamn _ vilket är pythonkonventionen för - den här variabeln struntar jag i
        self.data = [[self.empty for _ in range(self.width)] for _ in range(
            self.height)]

    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        # LS: används till exempel i funktionen make_walls()
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs

    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""

        # lodrätt: range 0 till hela self.height för det finns ingen vägg innan denna första vägg
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        # vågrätt: börjar på 1 för att första och sista positionen redan är en lodrät vägg
        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)


        # H. Använd for-loopar för att skapa flera, sammanhängande väggar på kartan.
        # lodräta väggar med fast avstånd till vågräta ytterväggarna, repeteras med fast inbördes avstånd så många som ryms
        leave_space_from_outerwall = 3
        for k in range(leave_space_from_outerwall, self.height - leave_space_from_outerwall):
            position = 6
            x_delta = 8
            y_delta = 4
            # upprepa lodräta innerväggar så länge som det finns utrymme kvar mot ytterväggen
            while position <= self.width - leave_space_from_outerwall:
                self.set(position, k, self.wall)
                # upprepa vågräta innerväggar så länge som det finns utrymme kvar mot ytterväggen
                if (position + y_delta) <= (self.width - leave_space_from_outerwall):
                   for j in range(position, position + y_delta):
                        self.set(j, y_delta, self.wall)
                position += x_delta

    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)

    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty

