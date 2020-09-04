class Grid:

    def __init__(self):
        self.cases = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def show_grid(self):
        print(f"----------------------------- \n [ {self.cases[0]} ]  [ {self.cases[1]} ]  [ {self.cases[2]} ] \n [ {self.cases[3]} ]  [ {self.cases[4]} ]  [ {self.cases[5]} ] \n [ {self.cases[6]} ]  [ {self.cases[7]} ]  [ {self.cases[8]} ] \n -----------------------------")

    def add_pad(self, line, colon, player):
        if self.cases[(line - 1) * 3 + colon - 1] == '' or self.cases[(line - 1) * 3 + colon - 1] == ' ':
            self.cases[(line - 1) * 3 + colon - 1] = player.symbol
            return True
        else:
            return False

    def win(self, game):
        winner = ''

        if (self.cases[0] == self.cases[1] and self.cases[1] == self.cases[2]) and '' != self.cases[0]:
            winner = self.cases[0]
        elif (self.cases[3] == self.cases[4] and self.cases[4] == self.cases[5]) and '' != self.cases[3]:
            winner = self.cases[3]
        elif (self.cases[6] == self.cases[7] and self.cases[7] == self.cases[8]) and '' != self.cases[6]:
            winner = self.cases[6]
        elif (self.cases[0] == self.cases[4] and self.cases[4] == self.cases[8]) and '' != self.cases[0]:
            winner = self.cases[0]
        elif (self.cases[2] == self.cases[4] and self.cases[4] == self.cases[6]) and '' != self.cases[0]:
            winner = self.cases[2]
        elif (self.cases[0] == self.cases[3] and self.cases[3] == self.cases[6]) and '' != self.cases[0]:
            winner = self.cases[0]
        elif (self.cases[1] == self.cases[4] and self.cases[4] == self.cases[7]) and '' != self.cases[7]:
            winner = self.cases[1]
        elif (self.cases[2] == self.cases[5] and self.cases[5] == self.cases[8]) and '' != self.cases[2]:
            winner = self.cases[2]

        if winner != '' and winner == game.j1.symbol:
            return game.j1
        elif winner != '' and winner == game.j2.symbol:
            return game.j2
