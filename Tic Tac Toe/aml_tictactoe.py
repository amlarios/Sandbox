#!/usr/bin/python3
#Alessio Larios
# Wesleyan University
# COMP 332, Spring 2018
# Homework 1: Tic-tac-toe game

import random

class Board():
    """
    TicTacToe game board
    """

    def __init__(self, n):
        self.n = n
        self.game_board = [[' - '] * n for i in range(n)]

    def display(self):
        for row in self.game_board:
            print(' '.join([str(y) for y in row]))

class TicTacToe():
    """
    TicTacToe game
    """

    def __init__(self, n):
        self.n = n
        self.board = Board(n)

    def display(self):
        self.board.display()

    def player_x(self):
        while True:
            x = int(input("Choose column [1-{}]: ".format(self.n)))
            if x > self.n:
                print("That column does not exist, please choose a new one")
            else:
                break
        return x

    def player_y(self):
        while True:
            y = int(input("Choose row [1-{}]: ".format(self.n)))
            if y > self.n:
                print("That row does not exist, please choose a new one")
            else:
                break
        return y

    def player_move(self):
        while True:
            p_x = self.player_x()
            p_y = self.player_y()
            if(self.board.game_board[p_y-1][p_x-1]!=' - '):
                print("Please choose a spot without an o or x")
            else:
                break
        print("User move:")
        self.board.game_board[p_y-1][p_x-1] = ' o '
        self.display()
        return [p_x, p_y]

    def victory(self, x, y):
        row_y = self.board.game_board[y]
        #Checks the row of the new placement
        if(all(row_y[i] == row_y[i+1] for i in range(len(row_y)-1))):
            return True
        #Checks the column of the new placement
        elif(all(row_y[x] == row[x] for row in self.board.game_board)):
            return True
        #If the coordinates are equalivalent, then we must check the diagonal
        elif(x==y):
            return self.diag_victory()
        #If the coordinates sum n-1, then they must be on the second diagonal
        elif (x+y==self.n-1):
            return self.diag1_victory()
        #If none of the previous conditions have been met, then there is no win
        else:
            return False

    def diag_victory(self):
        diag = []
        for i in range(self.n):
            diag.append(self.board.game_board[i][i])
        if (all(diag[0] == elt for elt in diag)):
            return True
        else:
            return False

    def diag1_victory(self):
        diag = []
        for i in range(self.n):
            diag.append(self.board.game_board[self.n-1-i][i])
        if (all(diag[0] == elt for elt in diag)):
            return True

    def CPU(self):
        while True:
            x = random.randint(0, self.n-1)
            y = random.randint(0, self.n-1)
            if(self.board.game_board[y][x]==' - '):
                break
        self.board.game_board[y][x] = ' x '
        print("Server move:")
        self.display()
        return [x,y]


class Server():
    """
    Server for TicTacToe game
    """

    def __init__(self):
        print('')

    def play(self):
        print("==================")
        print("| TicTacToe Game |")
        print("==================\n")
        size = int(input("Enter number of rows in TicTacToe board: "))
        tic_tac_toe = TicTacToe(size)
        game_board = tic_tac_toe.board.game_board
        tic_tac_toe.display()
        turn = 0 #Each time the player or CPU moves, this counter increases
        while True:
            if (turn < size*size): #The maximum number of moves is n^2
                p_x, p_y = tic_tac_toe.player_move()
                if (tic_tac_toe.victory(p_x-1, p_y-1)):
                    print("Winner: o!")
                    break
                turn+=1
                if turn==size*size:
                    print("This game was a tie! Try again.")
                    break
                x, y = tic_tac_toe.CPU()
                if(tic_tac_toe.victory(x, y)):
                    print("Winner: x!")
                    break
                turn+=1
                print(turn)
            else: #After the maximum number of moves, program ends
                print("This game was a tie! Try again.")
                break

def main():
    s = Server()
    s.play()

if __name__ == '__main__':
    main()
