import connect4
import random

class MinimaxAgent:
    def runBot(self, game):
        return minimax(game, 5, -1 * float('inf'),float('inf'),True)[1]

def minimax(game, depth, alpha, beta, player):
    game.checkWin()
    if depth == 0:
        return scorer(game), None
    if game.gameOver:
        return terminalState(game)
    if player:
        return maxPlayer(game, depth, alpha, beta, player)
    else:
        return minPlayer(game, depth, alpha, beta, player)

def scorer(game):
    score = 0
    for r in range(game.height):
        for c in range(game.width-3):
            score += evaluateArea(game.board[r][c:c+3])

    for r in range(game.height-3):
        for c in range(game.width):
            score += evaluateArea([game.board[r][c], game.board[r+1][c], game.board[r+2][c], game.board[r+3][c]])

    for r in range(game.height-3):
        for c in range(game.width-3):
            score +=  evaluateArea([game.board[r][c], game.board[r+1][c+1], game.board[r+2][c+2], game.board[r+3][c+3]])
    
    for r in range(3, game.height):
        for c in range(game.width-3):
            score +=  evaluateArea([game.board[r][c], game.board[r-1][c+1], game.board[r-2][c+2], game.board[r-3][c+3]])

    return score

def evaluateArea(locations):
    bot, player = 0, 0
    for location in locations:
        if location == 1:
            player += 1
        if location == 2:
            bot += 1
    score =  5*bot - 2*player
    return score

def terminalState(game):
    if game.winner == 1:
        return (-10000000000, None)
    if game.winner == 2:
        return (10000000000, None)
    else:
        return (0, None)

def viablePermuation(game):
    columns = []
    for i in range(game.width):
        if game.column_counts[i] > game.height - 1:
            continue
        columns.append(i)
    random.shuffle(columns)
    return columns

def maxPlayer(game, depth, alpha, beta, player):
    column = 0
    best_score = -1 * float('inf')
    options = viablePermuation(game)
    for option in options:
        game_copy = connect4.Connect4(game)
        game_copy.playTurn(option, False)
        score = minimax(game_copy, depth-1, alpha, beta, False)[0]
        if score > best_score:
            best_score = score
            column = option
        alpha = max(alpha, score)
        if alpha >= beta:
            break
    return (best_score, column)

def minPlayer(game, depth, alpha, beta, player):
    column = 0
    best_score = float('inf')
    options = viablePermuation(game)
    for option in options:
        game_copy = connect4.Connect4(game)
        game_copy.playTurn(option, False)
        score = minimax(game_copy, depth-1, alpha, beta, True)[0]
        if score < best_score:
            best_score = score
            column = option
        beta = min(beta, score)
        if alpha >= beta:
            break
    return (best_score, column)