import time
import gui

def startCompletion(row, col, numArr):
    print("The bot is thinking...")
    
    while gui.isDone() == False:
        time.sleep(0.5)

        countArr = countNums(row, col, numArr)

        for i in range(len(numArr)):
            iTop =  getTopNum(numArr[i])

            if str(iTop[1]) == "0" :
                continue

            for j in range(len(numArr)):
                jTop =  getTopNum(numArr[j])

                if i == j :
                    continue
                
                if str(iTop[1]) == str(jTop[1]):
                 
                    if countArr[i][iTop[1]] < countArr[j][jTop[1]] and str(numArr[j][0]) == "0" and isArrMixed(numArr[j]) == False:
                        numArr = gui.swapBlocks((iTop[0], i), numArr[i][iTop[0]], (0,j), numArr[j][0])
                        
                    elif countArr[i][iTop[1]] > countArr[j][jTop[1]] and str(numArr[i][0]) == "0" and isArrMixed(numArr[i]) == False:
                        numArr = gui.swapBlocks((jTop[0], j), numArr[j][jTop[0]], (0,i), numArr[i][0])

                    elif countArr[i][iTop[1]] == countArr[j][jTop[1]]:
                        if diffNums(numArr[i]) < diffNums(numArr[j]) and str(numArr[i][0]) == "0":
                            numArr = gui.swapBlocks((jTop[0], j), numArr[j][jTop[0]], (0,i), numArr[i][0])
                        elif str(numArr[j][0]) == "0":
                            numArr = gui.swapBlocks((iTop[0], i), numArr[i][iTop[0]], (0,j), numArr[j][0])

                    elif countArr[i][iTop[1]] > countArr[j][jTop[1]] and str(numArr[j][0]) == "0" and isArrMixed(numArr[j]) == False and diffNums(numArr[j]) == 2:
                        numArr = gui.swapBlocks((iTop[0], i), numArr[i][iTop[0]], (0,j), numArr[j][0])
                        
                    elif countArr[i][iTop[1]] < countArr[j][jTop[1]] and str(numArr[i][0]) == "0" and isArrMixed(numArr[i]) == False and diffNums(numArr[i]) == 2:
                        numArr = gui.swapBlocks((jTop[0], j), numArr[j][jTop[0]], (0,i), numArr[i][0])

                    elif countArr[i][iTop[1]] < countArr[j][jTop[1]] and str(numArr[j][0]) == "0" and isArrMixed(numArr[j]) == True:
                        numArr = gui.swapBlocks((iTop[0], i), numArr[i][iTop[0]], (0,j), numArr[j][0])
                        
                    elif countArr[i][iTop[1]] > countArr[j][jTop[1]] and str(numArr[i][0]) == "0" and isArrMixed(numArr[i]) == True:
                        numArr = gui.swapBlocks((jTop[0], j), numArr[j][jTop[0]], (0,i), numArr[i][0])

                                       
                elif str(jTop[1]) == "0" and diffNums(numArr[i]) != 1 and isArrMixed(numArr[i]) == True:
                    numArr = gui.swapBlocks((iTop[0], i), numArr[i][iTop[0]], (0,j), numArr[j][0])
                    # print(numArr[i] ,diffNums(numArr[i]), isArrMixed(numArr[i]))
                    
                    
                    
                    
            


def countNums(row, col, numArr):
    countArr = []

    for c in range(len(numArr)):
        tempcnt = []

        for i in range(col-1):
            tempcnt.append(0)
        
        for r in range(len(numArr[c])):
            tempcnt[numArr[c][r]] = tempcnt[numArr[c][r]] + 1

        countArr.append(tempcnt)

    return countArr


def isLargest(arr, num):
    large = 0
    for a in arr:
        if a > large:
            large = a
    
    return large == num


def getTopNum(arr):
    for a in range(len(arr)):
        if str(arr[a]) != '0':
            return (a, arr[a])

    return (0,0)


def diffNums(arr):
    tempArr = set(arr)
    return len(tempArr)
    

def isArrMixed(arr):
    if diffNums(arr) > 2:
        return True
    elif diffNums(arr) == 2:
        num = getTopNum(arr)

        if (arr.count(num[1]) + arr.count(0)) == len(arr):
            return False
        else:
            return True
    else:
        return False

