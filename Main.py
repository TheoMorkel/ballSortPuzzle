import game
import gui
import bot

import threading
import time

NUM_ROW = 4
NUM_COL = 6

# NUMBERS_LIST = [[1, 2, 3, 3], [1, 2, 2, 2], [3, 1, 3, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
# NUMBERS_LIST = [[1, 2, 3, 3], [2, 2, 3, 1], [1, 3, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0]]
# NUMBERS_LIST = [[2, 2, 1, 1], [1, 2, 3, 2], [3, 1, 3, 3], [0, 0, 0, 0], [0, 0, 0, 0]]
# NUMBERS_LIST = [[2, 2, 2, 3], [3, 1, 1, 2], [3, 1, 3, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
# NUMBERS_LIST = [[2, 3, 3, 1], [1, 2, 3, 4], [4, 2, 3, 4], [2, 1, 4, 1], [0, 0, 0, 0], [0, 0, 0, 0]]

# game.setGame(NUM_ROW, NUM_COL, NUMBERS_LIST)

NUMBERS_LIST = game.createGame(NUM_ROW, NUM_COL)
print(NUMBERS_LIST)

t1 = threading.Thread(target = gui.drawWindow, args=(NUM_ROW, NUM_COL, NUMBERS_LIST,))
t2 = threading.Thread(target = bot.startCompletion, args=(NUM_ROW, NUM_COL, NUMBERS_LIST,))

t1.start()
time.sleep(0.2)
t2.start()

t1.join()
t2.join()

