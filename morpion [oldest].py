from random import randint

lines = []
colons = []
pad = []
cases = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
starter = 0


def show_grid():
    for i in range(len(pad)):
        cases[(lines[i] - 1) * 3 + colons[i] - 1] = pad[i]

    print(f"----------------------------- \n [ {cases[0]} ]  [ {cases[1]} ]  [ {cases[2]} ] \n [ {cases[3]} ]  [ {cases[4]} ]  [ {cases[5]} ] \n [ {cases[6]} ]  [ {cases[7]} ]  [ {cases[8]} ] \n -----------------------------")


def player_play():
    print("C'est votre tour, placer un pion à l'endroit de votre choix (ligne,colone) : ")
    position = str(input('-->'))
    line = int(position.split(',')[0])
    colon = int(position.split(',')[1])

    if cases[(line - 1) * 3 + colon - 1] == ' ':
        lines.append(line)
        colons.append(colon)
        pad.append('X')

        print(f"Le joueur joue en {line}, {colon}")
    else:
        print('La case demandée est déjà remplie')
        player_play()


def computer_play():
    line = randint(1, 3)
    colon = randint(1, 3)

    if cases[(line - 1) * 3 + colon - 1] == ' ':
        lines.append(line)
        colons.append(colon)
        pad.append('O')

        print(f"L'ordinateur joue en {line}, {colon}")
    else:
        computer_play()


def game():
    print('La partie de morpion va débuter')
    rand = randint(1, 2)
    if rand == 1:
        print("Le tirage au sort désigne l'ordinateur pour démarrer")
        starter = 1
        computer_play()
    else:
        print("Le turage au sort vous désigne pour démarrer")
        starter = 0
        player_play()

    while True:
        show_grid()

        # -----------------------------
        # [ 0 ]  [ 1 ]  [ 2 ]
        # [ 3 ]  [ 4 ]  [ 5 ]
        # [ 6 ]  [ 7 ]  [ 8 ]
        # -----------------------------

        if (cases[0] == cases[1] and cases[1] == cases[2]) and (cases[0] != '' or cases[0] != ' '):
            winner = cases[0]
        elif (cases[3] == cases[4] and cases[4] == cases[5]) and (cases[3] != '' or cases[3] != ' '):
            winner = cases[3]
        elif (cases[6] == cases[7] and cases[7] == cases[8]) and (cases[6] != '' or cases[6] != ' '):
            winner = cases[6]
        elif (cases[0] == cases[4] and cases[4] == cases[8]) and (cases[0] != '' or cases[0] != ' '):
            winner = cases[0]
        elif (cases[2] == cases[4] and cases[4] == cases[6]) and (cases[2] != '' or cases[0] != ' '):
            winner = cases[2]
        elif (cases[0] == cases[3] and cases[3] == cases[6]) and (cases[0] != '' or cases[0] != ' '):
            winner = cases[0]
        elif (cases[1] == cases[4] and cases[4] == cases[7]) and (cases[1] != '' or cases[7] != ' '):
            winner = cases[1]
        elif (cases[2] == cases[5] and cases[5] == cases[8]) and (cases[2] != '' or cases[2] != ' '):
            winner = cases[2]

        if winner == 'X':
            print('Le joueur remporte la partie')
            break
        elif winner == 'O':
            print("L'ordinateur remporte la partie")
            break

        computer = 0
        player = 0
        for i in range(len(pad)):
            if pad[i] == 'X':
                player += 1
            else:
                computer += 1

        if (computer + player) == 9:
            print('Partie terminée sans vainqueurs')
            break

        winner = ''

        if computer > player or (computer == player and starter == 0):
            player_play()
        elif computer < player or (computer == player and starter == 1):
            computer_play()


game()
