from game import Game
from player import Player

player = Player('X')
computer = Player('O', True)

player.set_name()
computer.set_name()

print('La partie de morpion va débuter')

game = Game(player, computer)
game.who_start()
game.start()
