from tkinter import *
from Game import *

root = Tk()
root.title('Koala Puzzle')
root.geometry('1440x900')
root.resizable(width=False, height=False)
root.bind('<Escape>', lambda kill: root.destroy())


notation = '2, 1,. 2, 1, 3,. 7,. 1, 3,. 2, 1... 2,. 2, 1,. 1, 1,. 3,. 1, 1,. 1, 1,. 2,. 1, 1,. 1, 2,. 2, ...'
game = Game(root, notation)


# opens the window
root.mainloop()
