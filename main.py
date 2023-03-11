import random

def randomstart():
    arr = [0] * 8
    arr2 = [0] * 8
    i = 0
    while i < 8:
        arr[i] = random.randint(1, 8)
        arr2[i] = random.randint(1, 8)
        i = i + 1
    return arr, arr2

def buildBoards(arr):
    rows, cols = (8, 8)
    Board = [[' ' for i in range(cols)] for j in range(rows)]
    return QueensOnBoard(Board, arr)

def QueensOnBoard(Board, arr):
    for i in range(len(arr)):
        row = arr[i]-1
        Board[row][i] = 'Q'
    return Board

def fitnesscheck(arr):
    board = buildBoards(arr)
    fitness = 0
    for i in range(len(arr)):
        row = arr[i]-1
        col = i
        if(clash(board, row, col) == 0):
            fitness = fitness + 1
    # printBoard(board)
    # print("fitness: ", fitness, '\n')
    return fitness

def clash(Board,row, col):
    i = 0
    j = 0
    while i < 8:
        if i != row:
            if Board[i][col] == 'Q':
                return 1
        i = i + 1
        if j != col:
            if Board[row][j] == 'Q':
                return 1
        j = j + 1

    i = row + 1
    j = col + 1
    while True:
        if ((i>7) or (j>7)):
            break
        if Board[i][j] == 'Q':
            return 1
        i = i + 1
        j = j + 1

    i = row - 1
    j = col - 1
    while True:
        if ((i < 0) or (j < 0)):
            break
        if Board[i][j] == 'Q':
            return 1
        i = i - 1
        j = j - 1

    i = row + 1
    j = col - 1
    while True:
        if ((i > 7) or (j < 0)):
            break
        if Board[i][j] == 'Q':
            return 1
        i = i + 1
        j = j - 1

    i = row - 1
    j = col + 1
    while True:
        if ((i < 0) or (j > 7)):
            break
        if Board[i][j] == 'Q':
            return 1
        i = i - 1
        j = j + 1

    return 0

def printBoard(Board):
    for row in Board:
        print(row)


def crossover(arr, arr2):
    i = 0
    arr3 = [0] * 8
    arr4 = [0] * 8
    while i < 8:
        if i <= 3:
            arr3[i] = arr[i]
            arr4[i] = arr2[i]
        elif i > 3:
            arr3[i] = arr2[i]
            arr4[i] = arr[i]
        i = i + 1
    return mutation(arr3, arr4)

def mutation(arr, arr2):
    r1 = random.randint(0, 3)
    r2 = random.randint(4, 7)
    arr[r1], arr[r2] = arr[r1], arr[r1]
    arr2[r1], arr2[r2] = arr2[r2], arr2[r1]
    r3 = random.randint(0, 7)
    if(arr[r3]>1):
        arr[r3] = arr[r3]-1
    if(arr2[r3]<8):
        arr2[r3] = arr2[r3] + 1
    return arr, arr2

def takeSecond(elem):
    return elem[1]

def Survival(MyList):
    MyList.pop(7)
    MyList.pop(6)
    return MyList

def Loop(MyList):
    i = 0
    while i < 1000:
        L1 = MyList[0]
        L2 = MyList[1]
        array1, array2 = crossover(L1[0], L2[0])
        fit1 = fitnesscheck(array1)
        fit2 = fitnesscheck(array2)
        newl, newl2 = [array1, fit1], [array2, fit2]




        MyList.append(newl)
        MyList.append(newl2)
        MyList.sort(key=takeSecond, reverse=True)


        if len(MyList) >= 8:
            MyList = Survival(MyList)


        if (fit1 == 8) or (fit2 == 8):
            break


        i = i + 1

    print(MyList)
    print("Best = ", MyList[0])
    best = MyList[0]
    print("")
    printBoard(buildBoards(best[0]))


#Drivers Class
arr, arr2 = randomstart()
print(arr)
fitness1 = fitnesscheck(arr)
l1 = [arr, fitness1]
print(arr2)
fitness2 = fitnesscheck(arr2)
l2 = [arr2, fitness2]
Listss = []
Listss.append(l1)
Listss.append(l2)
Loop(Listss)





