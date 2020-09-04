import random


class Player:
    count_played: int
    is_computer: bool
    name: str
    symbol: str

    def __init__(self, symbol, computer=False):
        self.is_computer = computer
        self.name = None
        self.symbol = symbol
        self.count_played = 0

    def get_is_computer(self):
        return self.is_computer

    def set_name(self):
        if self.get_is_computer():
            self.name = 'ordinateur'
        else:
            print('Saisissez votre nom : ')
            self.name = str(input('-->'))

    def play(self, grid):
        if self.get_is_computer():
            line = random.randint(1, 3)
            colon = random.randint(1, 3)
            if grid.add_pad(line, colon, self):
                print(f"L'ordinateur a joué en {line}, {colon}")
                self.count_played += 1
            else:
                self.play(grid)
        else:
            print("C'est votre tour, placez un pion à l'endroit de votre choix (ligne,colone) : ")
            position = str(input('-->'))
            line = int(position.split(',')[0])
            colon = int(position.split(',')[1])

            if grid.add_pad(line, colon, self):
                print(f"Le joueur joue en {line}, {colon}")
                self.count_played += 1
            else:
                print('La case demandée est déjà remplie')
                self.play(grid)