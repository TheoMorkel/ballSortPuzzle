import PySimpleGUI as sg
import game
import bot
import time

window = None
MAX_ROWS = None
MAX_COLS = None

def drawWindow(row, col, numArr): 
    global window
    global MAX_ROWS
    global MAX_COLS

    MAX_ROWS = row
    MAX_COL = col
    

    sg.theme('Dark Blue 3')

    layout =   [[sg.Text('Number Sort Game Thing', font='Default 25')],
                [sg.Text(text = "Number of Moves: 0", size=(20,1), key='-MOVES-', font='Default 15')],
                [sg.Text(size=(20,1), key='-MESSAGE-', font='Default 15')]]

    board = []
    for row in range(MAX_ROWS):
        layout_row = []
        for col in range(MAX_COL):
            layout_row.append(sg.Button(str(numArr[col][row]), size=(4, 2), pad=(10,0), border_width=0, key=(row,col), disabled = False, button_color=('white', getColor(numArr[col][row]))))
        board.append(layout_row)

    layout += board
    layout +=  [[sg.Button('Exit', button_color=('white', '#283b5b'))]]

    window = sg.Window('Number Sort', layout)

    
    numMoves = 0
    isSelected = False
    selected_event = tuple(())
    selected_txt = ''
    
    while True:         
        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        else:
            txt = window[event].GetText()
            # print("Pos  : {}    Text  : {}".format(event, txt))

            if len(txt) == 1 and isSelected == False and game.isSelectable(event, txt):
                window[event].update('[' + txt + ']', button_color=('white', getColor(txt)))
                window['-MESSAGE-'].update('Pick another one')
                isSelected = True
                selected_event = event
                selected_txt = txt
                
            elif len(txt) == 1 and isSelected == True:
                window[event].update(txt, button_color=('white', getColor(txt)))
                window[selected_event].update(selected_txt, button_color=('white', getColor(selected_txt)))
                
                swap = game.swapNumbers(selected_event, selected_txt, event, txt)                

                window[swap['posA']].update(swap['txtA'], button_color=('white', getColor(swap['txtA'])))
                window[swap['posB']].update(swap['txtB'], button_color=('white', getColor(swap['txtB'])))

                if swap['swap'] == True:
                    numMoves = numMoves + 1
                    window['-MOVES-'].update("Number of Moves: " + str(numMoves))

                window['-MESSAGE-'].update('')
                isSelected = False
                selected_event = tuple(())
                selected_txt = ''
                
            elif len(txt) == 1:
                window[event].update(txt[0], button_color=('white', getColor(txt[0])))
                window['-MESSAGE-'].update('')

                isSelected = False
                selected_event = tuple(())
                selected_txt = ''

            else:
                window[event].update(txt[1], button_color=('white', getColor(txt[1])))
                window['-MESSAGE-'].update('')

                isSelected = False
                selected_event = tuple(())
                selected_txt = ''

            if game.isCompleted() == True:
                window['-MESSAGE-'].update('Completed')
                
                for row in range(MAX_ROWS):
                    for col in range(MAX_COL):
                        window[(row, col)].update(disabled = True)
                                            

          
    window.close()

def getColor(num):
    if str(num) == "0":
        return '#283B5B'
    elif str(num) == "1":
        return '#0089FF'
    elif str(num) == "2":
        return '#F600FF'
    elif str(num) == "3":
        return '#FF7600'
    elif str(num) == "4":
        return '#0AFF00'
    elif str(num) == "5":
        return '#9FE2BF'
    elif str(num) == "6":
        return '#6495ED'
    elif str(num) == "7":
        return '#FF7F50'
    elif str(num) == "8":
        return '#CCCCFF'
    else:
        return '#283B5B'


def swapBlocks(posA, txtA, posB, txtB):
    # print()
    # print("Pos A: {}    Text A: {}".format(posA, txtA), "Pos B: {}    Text B: {}".format(posB, txtB), sep = "\n")
    # print()
    
    if str(window[posA].GetText()) == str(txtA) and str(window[posB].GetText()) == str(txtB):
        window[posA].Click()
        window[posB].Click()

    return game.getNumList()

def isDone():
    if window.was_closed() == True:
        return True
    else:
        return game.isCompleted()

    