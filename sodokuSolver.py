#game board global so it cAN BE USEed by everthing
global gameBoard 
gameBoard = [[0 for x in range(9)]for y in range(9)]


def initializeGameBoard():
    gameBoard = [[0 for x in range(9)]for y in range(9)]


# Reads file in form of a matrix to populate game board
def enterBoard(file):
    for x in range(9):
        line = file.readline().split()
        for y in range(9):
            gameBoard[x][y] =int(line[y])
            
            
#recursive function that backtracks to find all solutions and prints out solution
def solve(place):
    global gameBoard
    for x in range(9):
        for y in range(9):
           if gameBoard[x][y]==0:
                for num in range(1,10):
                    if(safeToPlace(x,y , num)):
                        gameBoard[x][y] = num
                        #printGameBoard()
                        #print(' ')
                        solve(place)
                        gameBoard[x][y]= 0
                return
    
    printGameBoard()
    print('\n')
    input('More?')

#checks to see if placing num will break any rules of the game
def safeToPlace(x,y, num):
    #check row
    for col in range(9):
           if gameBoard[x][col] == num:
               return False

    
           

    #check col
    for row in range(9):
           if gameBoard[row][y] == num:
               return False

           
    #check square
    row = (x//3)*3
    col = (y//3)*3

    for r in range(0,3):
           for c in range(0,3):
               if gameBoard[row+r][col+c] == num:
                   return False

    return True

# prints game board in a matrix form
def printGameBoard():
    for r in range(9):
        for c in range(9):
            print(gameBoard[r][c], end =' ')
        print('\n')
                
def main():

    file = open("file.txt",'r')
    place = [0,0]

    initializeGameBoard()
    enterBoard(file)
    printGameBoard()
    print('\n')
    solve(place)
    file.close()


main()

