import minimax
from importlib import reload
reload(minimax)

class Connect4:
    def __init__(self, oldGame = None):
        self.height = 6
        self.width = 7
        self.turn = 1
        self.gameOver = False
        self.winner = 0
        self.newBoard()
        if oldGame is not None:
            self.copyBoard(oldGame)
            self.turn = oldGame.turn

    def newBoard(self):
        self.column_counts = [0 for _ in range(self.width)]
        self.board = [[0 for _ in range(self.width)] for __ in range(self.height)]
    
    def copyBoard(self, oldGame):
        for r in range(self.height):
            for c in range(self.width):
                self.board[r][c] = oldGame.board[r][c]
        self.countColumns()
    
    def countColumns(self):
        for c in range(self.width):
            count = 0
            for r in range(self.height):
                if self.board[r][c] != 0:
                    count += 1
            self.column_counts[c] = count

    def printBoard(self):
        for i in range(self.height):
            print(self.board[i])
        print('\n')
    
    def playTurn(self, column, human):
        if column < 0 or column > self.width - 1:
            if human:
                print('Not a viable turn')
                return

        fill = self.column_counts[column]
        if fill > self.height - 1:
            if human:
                print('Column is already filled')
                return

        self.board[self.height-1-fill][column] = self.turn
        self.column_counts[column] += 1
        if human:
            self.printBoard()
        self.changePlayer()
    
    def changePlayer(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
    
    def checkWin(self):
        forward, backward, vertical, horizontal = self.checkForwardDiag(), self.checkBackwardDiag(), self.checkVertical(), self.checkHorizontal()
        win = max(forward, backward, vertical, horizontal)
        if win != 0:
            self.gameOver = True
            self.winner = win   
    
    def checkForwardDiag(self):
        player = 0
        for c in range(self.width-3):
            for r in range(self.height-3):
                if self.board[r][c] != 0:
                    player = self.board[r][c]
                    if self.board[r+1][c+1] == player and self.board[r+2][c+2] == player and self.board[r+3][c+3] == player:
                        return player
                player = 0
        return player
            
    def checkBackwardDiag(self):
        player = 0
        for c in range(self.width-3):
            for r in range(3, self.height):
                if self.board[r][c] != 0:
                    player = self.board[r][c]
                    if self.board[r-1][c+1] == player and self.board[r-2][c+2] == player and self.board[r-3][c+3] == player:
                        return player
                player = 0
        return player

    def checkHorizontal(self):
        player = 0
        for c in range(self.width-3):
            for r in range(self.height):
                if self.board[r][c] != 0:
                    player = self.board[r][c]
                    if self.board[r][c+1] == player and self.board[r][c+2] == player and self.board[r][c+3] == player:
                        return player
                player = 0
        return player

    def checkVertical(self):
        player = 0
        for c in range(self.width):
            for r in range(self.height-3):
                if self.board[r][c] != 0:
                    player = self.board[r][c]
                    if self.board[r+1][c] == player and self.board[r+2][c] == player and self.board[r+3][c] == player:
                        return player
                player = 0
        return player
    
    def botTurn(self):
        game = self
        best_move = minimax.MinimaxAgent.runBot(0, self)
        self.playTurn(best_move, False)
    
    def play2Player(self):
        while not self.gameOver:
            column = input('Enter column to insert piece:')
            column = int(column)
            self.playTurn(column, True)
            self.checkWin()
        print('Player ' + str(self.winner) + ' Won!')
    
    def play1Player(self):
        while not self.gameOver:
            if(self.turn == 1):
                column = input('Enter column to insert piece:')
                column = int(column)
                self.playTurn(column, True)
                self.checkWin()
            else:
                print('Bot Turn')
                self.botTurn()
                self.printBoard()
                self.checkWin()
        print('Player ' + str(self.winner) + ' Won!')

game = Connect4()
game.play1Player()