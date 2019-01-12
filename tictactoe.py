import random

boardValues = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
compSym = 'X'
playerSym = 'O'
pScore = 0
cScore = 0


def displayBoard():
    print(' ', boardValues[0], ' | ', boardValues[1], ' | ', boardValues[2])
    print('-----------------')
    print(' ', boardValues[3], ' | ', boardValues[4], ' | ', boardValues[5])
    print('-----------------')
    print(' ', boardValues[6], ' | ', boardValues[7], ' | ', boardValues[8])


def firstturn():
    if random.randint(0, 1):
        return 'Computer'
    else:
        return 'Player'


def ifWon():
    if boardValues[0] == boardValues[1] == boardValues[2] != ' ' or \
        boardValues[3] == boardValues[4] == boardValues[5] != ' ' or \
        boardValues[6] == boardValues[7] == boardValues[8] != ' ' or \
        boardValues[3] == boardValues[0] == boardValues[6] != ' ' or \
        boardValues[1] == boardValues[4] == boardValues[7] != ' ' or \
        boardValues[2] == boardValues[5] == boardValues[8] != ' ' or \
        boardValues[0] == boardValues[4] == boardValues[8] != ' ' or \
        boardValues[2] == boardValues[4] == boardValues[6] != ' ':
        return True
    else:
        return False


def GuessCompMove():
    arr = [moveCondition_a(0, 1, 2), 
    moveCondition_a(3, 4, 5),
    moveCondition_a(6, 7, 8),
    moveCondition_a(0, 3, 6),
    moveCondition_a(1, 4, 7),
    moveCondition_a(2, 5, 8),
    moveCondition_a(2, 4, 6),
    moveCondition_a(0, 4, 8),
    moveCondition_b(0, 1, 2),
    moveCondition_b(3, 4, 5),
    moveCondition_b(6, 7, 8),
    moveCondition_b(0, 3, 6),
    moveCondition_b(1, 4, 7),
    moveCondition_b(2, 5, 8),
    moveCondition_b(2, 4, 6),
    moveCondition_b(0, 4, 8)]

    for i in range(0,16):
        if arr[i] != -1:
            return arr[i]
    else:
        return random.randint(0, 8)


def moveCondition_a(i, j, k):
    if (boardValues[i] == boardValues[j] == compSym and boardValues[k] == ' '):
        return k
    elif (boardValues[i] == boardValues[k] == compSym and boardValues[j] == ' '):
        return j
    elif (boardValues[k] == boardValues[j] == compSym and boardValues[i] == ' '):
        return i
    else:
        return -1

def moveCondition_b(i, j, k):
    if (boardValues[i] == boardValues[j] == playerSym and boardValues[k] == ' '):
        return k
    elif (boardValues[i] == boardValues[k] == playerSym and boardValues[j] == ' '):
        return j
    elif (boardValues[k] == boardValues[j] == playerSym and boardValues[i] == ' '):
        return i
    else:
        return -1

    

def computerTurn():
    num = GuessCompMove()
    while boardValues[num] != ' ':
        num = GuessCompMove()
    boardValues[num] = compSym
    displayBoard()        


def playerTurn():
    num = int(input('Your move on [1-9]: ').strip())
    while boardValues[num-1] != ' ':
        print('Already filled. Enter again!')
        num = int(input('Your move on: ').strip())
    boardValues[num-1] = playerSym
    print()
    displayBoard()

        
def makeYourTurn(turn):
    if turn == 'Computer':
        computerTurn()
    else:
        playerTurn()


def nextTurn(turn):
    if turn == 'Computer':
        return 'Player'
    else:
        return 'Computer'

def isDraw():
    if ' ' not in boardValues:
        print("MATCH DRAWN!")
        return True
    else:
        return False


def checkWinner(currentTurn):
    global pScore
    global cScore
    if ifWon():
        if currentTurn is 'Player':
            print("CONGRATS! WOU WON!\n")
            pScore += 1
        else:
            print("BAD LUCK! YOU LOST!\n")
            cScore += 1
        return True
    else:
        return False


if __name__ == '__main__':
    more = "y"
    while more == "Y" or more == 'y' :
        boardValues = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        displayBoard()
        currentTurn = firstturn()
        print("First turn is  of " + currentTurn)
        while(True):
            print('\n {} turn.\n'.format(currentTurn))
            makeYourTurn(currentTurn)
            if checkWinner(currentTurn):
                break
            currentTurn = nextTurn(currentTurn)
            if isDraw():
                break
        print('Player: {} \t Computer: {}'.format(pScore, cScore))
        more = str(input('Continue Playing? (Y/N): '))
    print('\n FINAL SCORE: \n PLAYER = {} \n COMPUTER = {}'.format(pScore, cScore))
