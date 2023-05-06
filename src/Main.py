from tkinter import *
from Game import *

root = Tk()
root.title('Koala Puzzle')
root.geometry('1440x900')
root.bind('<Escape>', lambda kill: root.destroy())

game = Game(root)

# opens the window
root.mainloop()
