import random

score = 0
botScore = 0
winningScore = 0

grid = [[" "] * 8 for x in range(8)]
opGrid = [[" "] * 8 for x in range(8)]

playerGrid = [[" "] * 8 for x in range(8)]

def printBoard():
    print("B 1  2  3  4  5  6  7  8")
    for x in range(8):
        print(x + 1, end='')
        for y in range(8):
            print("[" + str(grid[x][y]) + "]", end='')
        print("")
    print("")

def printPlayerBoard():
    print("P 1  2  3  4  5  6  7  8")
    for x in range(8):
        print(x + 1, end='')
        for y in range(8):
            print("[" + str(playerGrid[x][y]) + "]", end='')
        print("")
    print("")

def makeGuess():
    global score
    global botScore

    while True:
        try:
            a = int(input("Enter row: "))
            a = a - 1
            if(a == -1):
                print("")
                printBoard()
                continue
            if (a == 9):
                print("")
                printPlayerBoard()
                continue
            if(a == 19):
                print("")
                print("Your Score: " + str(score))
                print("")
                continue
            if(a == 20):
                print("")
                print("Bot's Score: " + str(botScore))
                print("")
                continue
            if(a < 0 or a > 7):
                print("")
                print("Invalid row!")
                print("")
                continue
        except:
            print("Error!")
            continue
        try:
            b = int(input("Enter column: "))
            b = b - 1
            if(b == -1):
                printBoard()
                continue
            if (b == 9):
                printPlayerBoard()
                continue
            if (b == 19):
                print("Your Score: " + score)
                continue
            if (b == 20):
                print("Bot's Score: " + botScore)
            if(b < 0 or b > 7):
                print("Invalid column!")
                continue
        except:
            print("Error!")
            continue

        if (grid[a][b] == "O" or grid[a][b] == "X"):
            print("")
            print("You already made that guess!")
            print("")
            continue

        if(opGrid[a][b] == "S" or opGrid[a][b] == "M" or opGrid[a][b] == "L"):
            print("")
            print("Hit!")
            print("")
            grid[a][b] = "X"
            increaseScore()
            return True
        else:
            print("")
            print("Miss!")
            print("")
            grid[a][b] = "O"
            return False

def makeBotGuess():
    while True:
        try:
            a = random.randint(0, 8);
            if(a < 0 or a > 8):
                print("Bot: Invalid row!")
                continue
        except:
            print("Bot: Error!")
            continue
        try:
            b = random.randint(0, 8);
            if(b < 0 or b > 8):
                print("Bot: Invalid column!")
                continue
        except:
            print("Bot: Error!")
            continue

        if (playerGrid[a][b] == "O" or playerGrid[a][b] == "X"):
            print("Bot: You already made that guess!")
            continue

        if(playerGrid[a][b] == "S" or playerGrid[a][b] == "M" or playerGrid[a][b] == "L"):
            print("Bot: Hit!");
            print("")
            playerGrid[a][b] = "X"
            increaseBotScore()
            return True
        else:
            print("Bot: Miss!")
            print("")
            playerGrid[a][b] = "O"
            return False

def makeBoats():
    global winningScore

    for x in range(4):
        makeSmall(opGrid)
        makeSmall(playerGrid)

    for x in range(3):
        makeMedium(opGrid)
        makeMedium(playerGrid)

    for x in range(2):
        makeLarge(opGrid)
        makeLarge(playerGrid)

    winningScore /= 2

def makeSmall(xGrid):
    global winningScore
    winningScore = winningScore + 1
    while True:
        a = random.randint(0, 7)
        b = random.randint(0, 7)
        if(xGrid[a][b] == " "):
            xGrid[a][b] = "S"
            break

def makeMedium(xGrid):
    global winningScore
    winningScore = winningScore + 2
    while True:
        a = random.randint(0, 7)
        b = random.randint(0, 7)

        if(xGrid[a][b] == " " and boundaryCheck(xGrid, a, b)):
            xGrid[a][b] = "M"
            break
    while True:
        side = random.randint(0, 4)
        if(side == 0):
            if(a > 0 and xGrid[a-1][b] == " "):
                xGrid[a-1][b] = "M"
                break

        elif (side == 1):
            if (b > 0 and xGrid[a][b-1] == " "):
                xGrid[a][b-1] = "M"
                break

        elif (side == 2):
            if (a < 7 and xGrid[a + 1][b] == " "):
                xGrid[a + 1][b] = "M"
                break

        elif (side == 3):
            if (b < 7 and xGrid[a][b+1] == " "):
                xGrid[a][b+1] = "M"
                break

def makeLarge(xGrid):
    global winningScore
    winningScore = winningScore + 3
    while True:
        a = random.randint(0, 7)
        b = random.randint(0, 7)
        if(xGrid[a][b] == " " and boundaryCheck(xGrid, a, b) and boundaryCheck2(xGrid, a, b)):
            xGrid[a][b] = "L"
            break

    while True:
        side = random.randint(0, 4)
        if(side == 0):
            if(a > 1 and xGrid[a-1][b] == " " and xGrid[a-2][b] == " "):
                xGrid[a-1][b] = "L"
                xGrid[a-2][b] = "L"
                break

        elif (side == 1):
            if (b > 1 and xGrid[a][b-1] == " " and xGrid[a][b-2] == " "):
                xGrid[a][b-1] = "L"
                xGrid[a][b-2] = "L"
                break

        elif (side == 2):
            if (a < 6 and xGrid[a+1][b] == " " and xGrid[a+2][b] == " "):
                xGrid[a+1][b] = "L"
                xGrid[a+2][b] = "L"
                break

        elif (side == 3):
            if (b < 6 and xGrid[a][b+1] == " " and xGrid[a][b+2] == " "):
                xGrid[a][b+1] = "L"
                xGrid[a][b+2] = "L"
                break

def boundaryCheck(xGrid, a, b):
    try:
        if xGrid[a+1][b] == " ":
            return True
    except IndexError:
        try:
            if xGrid[a-1][b] != " ":
                return True
        except IndexError:
            try:
                if xGrid[a][b+1] != " ":
                    return True
            except IndexError:
                try:
                    if xGrid[a][b-1] != " ":
                        return True
                    else:
                        return False
                except IndexError:
                    return False

def boundaryCheck2(xGrid, a, b):
    try:
        if xGrid[a+2][b] == " ":
            return True
    except IndexError:
        try:
            if xGrid[a-2][b] != " ":
                return True
        except IndexError:
            try:
                if xGrid[a][b+2] != " ":
                    return True
            except IndexError:
                try:
                    if xGrid[a][b-2] != " ":
                        return True
                    else:
                        return False
                except IndexError:
                    return False

def increaseScore():
    global score
    score = score + 1

def increaseBotScore():
    global botScore
    botScore = botScore + 1


def playGame():
    global score
    global botScore
    global winningScore

    makeBoats()

    print("###############################################################")
    print("# Enter 0 to view the board, and 10 to view your board        #")
    print("# Enter 20 to view your score, and 21 to view the Bot's score #")
    print("# Hits required to win this game: " + str(int(winningScore)) + "                          #")
    print("# Enter a row between 1 and 8 inclusive                       #")
    print("# O represents a miss, X represents a hit                     #")
    print("###############################################################")
    print("")

    while True:
        makeGuess()
        if (score == winningScore):
            print("You sunk their Battleships!")
            printBoard()
            break
        makeBotGuess()
        if (botScore == winningScore):
            print("Your Battleships have been sunk!")
            printBoard()
            break

playGame()