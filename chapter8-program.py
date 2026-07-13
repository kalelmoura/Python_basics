tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():

    colWidths = [0] * len(tableData)
    listLen = len(tableData[0])

    for i in range(len(colWidths)):
        for x in range(listLen):
            if len(tableData[i][x]) > colWidths[i]:
                colWidths[i] = len(tableData[i][x])

    print(colWidths)

    for i in range(listLen):
        print()        
        for y in range(len(tableData)):
            print(tableData[y][i].rjust(colWidths[y]), end=" ")

printTable()
