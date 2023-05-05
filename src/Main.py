from tkinter import *
from Game import *

root = Tk()
root.title('Koala Puzzle')
root.bind('<Escape>', lambda kill: root.destroy())

'''
number_rows = 10
number_columns = 15
amount_bombs = 0.25 * number_rows * number_columns
game = Game(number_rows, number_columns, amount_bombs)
'''

game = Game()

# opens the window
root.mainloop()
