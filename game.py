from random import randint

number_list = list(())
row_size = 0
col_size = 0

def createGame(row, col):
    global number_list
    global row_size
    global col_size

    row_size = row
    col_size = col

    tempNums = list(())
    for c in range(col - 2):
        for r in range(row):
            tempNums.append(c + 1)

    for c in range(col - 2):
        temp = list(())
        for r in range(row):
            temp.append(tempNums.pop(randint(0, len(tempNums) - 1)))
        
        number_list.append(temp)

    for c in range(2):
        temp = list(())
        for r in range(row):
            temp.append(0)
        
        number_list.append(temp)

    return number_list

def setGame(row, col, arr):
    global number_list
    global row_size
    global col_size
    
    number_list = arr
    row_size = row
    col_size = col


def isSelectable(pos, txt):
    row = pos[0]
    col = pos[1]

    if str(txt) == '0':
        return False
    elif row == 0:
        return True
    elif str(number_list[col][row-1]) == '0':
        return True
    else:
        return False
        
def swapNumbers(posA, txtA, posB, txtB):
    rowA = posA[0]
    colA = posA[1]

    rowB = posB[0]
    colB = posB[1]

    newLocations = {
        'posA': '',
        'txtA': '',
        'posB': '',
        'txtB': '',
        'swap': True
    }
    
    if str(number_list[colA][rowA]) == str(txtA) and str(number_list[colB][rowB]) == str(txtB) and str(txtB) == '0':
        index = rowVal(colB, txtA)
        
        if index < 0:
            newLocations = {
                'posA': posA,
                'txtA': str(txtA),
                'posB': posB,
                'txtB': str(txtB),
                'swap': True
            }
            return newLocations

        number_list[colA][rowA] = int(txtB)
        number_list[colB][index] = int(txtA)

        newLocations = {
            'posA': (index, colB),
            'txtA': str(txtA),
            'posB': posA,
            'txtB': str(txtB),
            'swap': True
        }

        return newLocations
        
    else:
        newLocations = {
            'posA': posA,
            'txtA': str(txtA),
            'posB': posB,
            'txtB': str(txtB),
            'swap': False
        }
        return newLocations

def rowVal(colB, txtA):
    for i in range(len(number_list[colB]) - 1):
        if str(number_list[colB][i]) == '0':
            if str(number_list[colB][i+1]) == '0':
                if (i+1) == (row_size-1):
                    return i+1
                else:
                    pass
            elif str(number_list[colB][i+1]) == str(txtA):
                return i
            
        elif str(number_list[colB][i+1]) == str(txtA):
            return i

    return -1

def isCompleted():
    complete = True

    for rowlist in number_list:
        num = rowlist[0]
        if rowlist.count(num) != row_size:
            complete = False

    return complete

def getNumList():
    return number_list