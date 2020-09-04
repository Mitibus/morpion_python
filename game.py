from random import randint
from grid import Grid
import sys


class Game:
    def __init__(self, j1, j2):
        self.starter = None
        self.j1 = j1
        self.j2 = j2
        self.grid = Grid()

    def who_start(self):
        if self.starter == randint(0, 1):
            self.starter = self.j1
        else:
            self.starter = self.j2

        print(f"C'est {self.starter.name} qui commence")
        self.starter.play(self.grid)

    def who_play(self):
        if (self.j1.count_played + self.j2.count_played) == 9:
            print('Partie terminée sans vainqueurs')

        print("############################")
        print(f"J1 ({self.j1.name}) : {self.j1.count_played}")
        print(f"J2 ({self.j2.name}) : {self.j2.count_played}")
        print(f"Starter : ", self.starter.name)

        if self.j1.count_played > self.j2.count_played or (
                self.j1.count_played == self.j2.count_played and self.starter == self.j2):
            self.j2.play(self.grid)
            self.start()
        elif self.j1.count_played < self.j2.count_played or (
                self.j1.count_played == self.j2.count_played and self.starter == self.j1):
            self.j1.play(self.grid)
            self.start()

    def start(self):
        self.grid.show_grid()

        winner = self.grid.win(self)

        if winner == self.j1:
            print(f"{self.j1.name} remporte la partie")
            sys.exit()
        elif winner == self.j2:
            print(f"{self.j2.name} remporte la partie")
            sys.exit()

        self.who_play()
