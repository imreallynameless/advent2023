f = open("day3.txt", "r")
total = 0
matrix = []
numLocations = {

}

def isSymbol(char):
    if not (char.isdigit() or char == "."):
        return True
    return False

def partNumber(rowIdx, colIdx):
    global total, colMax, rowMax
    toAdd = 0
    rowStart = rowIdx - 1
    colStart = colIdx - 1
    rowEnd = rowIdx + 1
    colEnd = colIdx + 1

    colStartHolder = colStart

    while rowStart <= rowEnd:
        colStart = colStartHolder
        while colStart <= colEnd:
            # print ("rowStart: " + str(rowStart), "colStart: " + str(colStart))
            if numLocations.get((rowStart, colStart)):
                # print (str(rowStart) + ", " + str(colStart))
                toAdd = numLocations.get((rowStart, colStart))
                total += toAdd
                # print(total)
                print("toAdd: " + str(toAdd))
                if numLocations.get((rowStart, colStart-1)):
                    colStart += min(2, len(str(toAdd)))
                else:
                    colStart += len(str(toAdd))
                toAdd = 0
            else:
                colStart += 1
        #     print ("colStart: " + str(colStart))
        # print ("rowStart: " + str(rowStart))
        rowStart += 1
            



    
    return 
 
for line in f:
    array = list(line.strip())
    matrix.append(array)

rowMax = len(matrix)
# print(rowMax)
colMax = len(matrix[0])

toAdd = 0
for row in range(rowMax):
    col = 0
    while col < colMax:
        if matrix[row][col].isdigit():
            while col < colMax and matrix[row][col].isdigit():
                toAdd = toAdd * 10 + int(matrix[row][col])
                col += 1
            for i in range(len(str(toAdd))):
                numLocations[(row, col - i + 1)] = toAdd
            toAdd = 0
        else:
            col += 1

# print(numLocations)


for row in range(rowMax):
    col = 0
    while col < colMax:
        if isSymbol(matrix[row][col]):
            # print (matrix[row][col] + " at " + str(row) + ", " + str(col))
            partNumber(row, col+1)
            col += 1
        else:
            col += 1

print(total)
