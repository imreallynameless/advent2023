f = open("day3.txt", "r")
total = 0
matrix = []
digitFlag = False
toAdd = 0
digitLen = 0

def isSymbol(char):
    if not (char.isdigit() or char == "."):
        return True
    return False

def partNumber(startIdx, endIdx, rowIdx):
    global total, toAdd, rowMax, colMax
    if startIdx - 2 >= 0:
        startIdx -= 1
    if endIdx + 2 <= colMax:
        endIdx += 1
    for col in range(startIdx - 1, endIdx + 1):
        if 0 <= col <  colMax+1:
            if isSymbol(matrix[rowIdx][col]):
                total += toAdd
                print (toAdd)
                toAdd = 0
                return
            if rowIdx + 1 < rowMax and isSymbol(matrix[rowIdx + 1][col]):
                total += toAdd
                print (toAdd)
                toAdd = 0
                return
            if rowIdx - 1 >= 0 and isSymbol(matrix[rowIdx - 1][col]):
                total += toAdd
                print (toAdd)
                toAdd = 0
                return
    toAdd = 0

for line in f:
    array = list(line.strip())
    matrix.append(array)

rowMax = len(matrix)
colMax = len(matrix[0])

for row in range(rowMax):
    col = 0
    while col < colMax:
        if matrix[row][col].isdigit():
            while col < colMax and matrix[row][col].isdigit():
                toAdd = toAdd * 10 + int(matrix[row][col])
                col += 1
            partNumber(col - len(str(toAdd)), col - 1, row)
        else:
            col += 1

print(total)
