from tkinter import *
from Game import *

root = Tk()
root.title('Koala Puzzle')
root.bind('<Escape>', lambda kill: root.destroy())

game = Game()

# opens the window
root.mainloop()
