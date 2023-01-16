Board = [['-','-','-'],['-','-','-'],['-','-','-']]
#case1 = Board[0][0]
#case2 = Board[0][1]
#case3 = Board[0][2]
#case4 = Board[1][0]
#case5 = Board[1][1]
#case6 = Board[1][2]
#case7 = Board[2][0]
#case8 = Board[2][1]
#case9 = Board[2][2]

def printBoard(): 
    print("\n")
    print(' _________________')
    print('|     |     |     |')
    print("|  {}  |  {}  |  {}  |".format(Board[0][0], Board[0][1], Board[0][2]))
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print("|  {}  |  {}  |  {}  |".format(Board[1][0], Board[1][1], Board[1][2]))
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print("|  {}  |  {}  |  {}  |".format(Board[2][0], Board[2][1], Board[2][2]))
    print('|_____|_____|_____|')
    print("\n")
printBoard()

def check_combinaison():
    if Board[0][0] == Board[0][1] == Board[0][2] != '-':
        return True
    elif Board[1][0] == Board[1][1] == Board[1][2] != '-':
        return True
    elif Board[2][0] == Board[2][1] == Board[2][2] != '-':
        return True
    elif Board[0][0] == Board[1][0] == Board[2][0] != '-':
        return True
    elif Board[0][1] == Board[1][1] == Board[2][1] != '-':
        return True
    elif Board[0][2] == Board[1][2] == Board[2][2] != '-':
        return True
    elif Board[0][0] == Board[1][1] == Board[2][2] != '-':
        return True
    elif Board[0][2] == Board[1][1] == Board[2][0] != '-':
        return True
    else:
        return False

def game():
    player = "X"
    count = 0
    while count<9:
    #while (check_availability()==True):
            #printBoard()
            
        move_row = input("Au tour de "+player+" de selectionner la ligne à jouer: ")
        move_col = input("Au tour de "+player+" de selectionner la colonne à jouer: ")
        #if 1 > int(move_row) > 3:
         #   print("Entrez une valeur entre 1 et 3 !!!")
          #  continue
        #if 1 > int(move_col) > 3:
         #   print("Entrez une valeur entre 1 et 3 !!!")
          #  continue
        if Board[int(move_row)-1][int(move_col)-1] != '-':
            print("Cette case est déjà jouée.")
            continue
        if check_combinaison()==True:
            print(player+ " a gagné la partie.")
            break
        else:
            Board[int(move_row)-1][int(move_col)-1] = player
            printBoard()
        if check_combinaison()==True:
            print(player+ " a gagné la partie.")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"
        count += 1
        if count ==9:
            print("Match nul.")
        #printBoard()
        print(check_combinaison())
game()