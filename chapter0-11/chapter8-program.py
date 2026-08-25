tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):

    colWidths = [0] * len(table)
    listLen = len(table[0])

    for i in range(len(colWidths)):
        for x in range(listLen):
            if len(table[i][x]) > colWidths[i]:
                colWidths[i] = len(table[i][x])

    print(colWidths)

    for i in range(listLen):
        print()        
        for y in range(len(table)):
            print(table[y][i].rjust(colWidths[y]), end=" ")

printTable(tableData)
