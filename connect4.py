
class Connect4():
    def __init__(self, oldGame = None):
        self.height = 6
        self.width = 7
        self.turn = 1
        self.gameOver = False

        if oldGame == None:
            self.newBoard()
        else:
            self.board = oldGame.board
            self.column_counts = oldGame.column_counts

    def newBoard(self):
        self.column_counts = [0 for _ in range(self.width)]
        self.board = [[0 for _ in range(self.width)] for __ in range(self.height)]

    def printBoard(self):
        for i in range(self.height):
            print(self.board[i])
    
    def playTurn(self, column):
        fill = self.column_counts[column]
        if column < 0 or column > self.width - 1:
            print('Not a viable turn')
            return
        if fill > self.height - 1:
            print('Column is already filled')
            return

        self.board[self.height-1-fill][column] = self.turn
        self.column_counts[column] += 1
        self.printBoard()
        self.changePlayer()
    
    def changePlayer(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
    
    def checkWin(self):
        forward, backward, vertical, horizontal = self.checkForwardDiag(), self.checkBackwardDiag(), self.checkVertical(), self.checkHorizontal()
        winner = max(forward, backward, vertical, horizontal)
        if winner != 0:
            self.gameOver = True
            print('Player ' + str(winner) + ' Won!')
    
    def checkForwardDiag(self):
        player = 0
        for c in range(self.width-3):
            for r in range(self.height-3):
                if self.board[r][c] != 0:
                    player = self.board[r][c]
                    if self.board[r+1][c+1] == player and self.board[r+2][c+2] == player and self.board[r+3][c+3] == player:
                        return player
        return player
            
    def checkBackwardDiag(self):
        player = 0
        for c in range(3, self.width):
            for r in range(3, self.height):
                if self.board[r][c] != 0:
                    player = self.board[r][c]
                    if self.board[r-1][c-1] == player and self.board[r-2][c-2] == player and self.board[r-3][c-3] == player:
                        return player
        return player

    def checkHorizontal(self):
        player = 0
        for c in range(self.width-3):
            for r in range(self.height):
                if self.board[r][c] != 0:
                    player = self.board[r][c]
                    if self.board[r][c+1] == player and self.board[r][c+2] == player and self.board[r][c+3] == player:
                        return player
        return player

    def checkVertical(self):
        player = 0
        for c in range(self.width):
            for r in range(self.height-3):
                if self.board[r][c] != 0:
                    player = self.board[r][c]
                    if self.board[r+1][c] == player and self.board[r+2][c] == player and self.board[r+3][c] == player:
                        return player
        return player

game = Connect4()
for i in range(4):
    game.playTurn(i)
    print('\n')

    game.playTurn(i+1)
    print('\n')

game.checkWin()