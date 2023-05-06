from tkinter import *
from Layout import *


class Game:

    def __init__(self, root):
        """ Makes a new game (picross) with rows/columns as param. Eventually take in a picross-FEN """

        layout = Layout(root)

        # make the buttons
        # for a in range(10):
        #     for b in range(10):
        #         new_button = Button(layout.main_frame, height=3, width=6)
        #         new_button.grid(row=a, column=b)
