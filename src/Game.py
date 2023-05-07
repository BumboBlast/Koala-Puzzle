from tkinter import *
from Layout import *


class Game:

    def __init__(self, root):
        """ Makes a new game (picross) with rows/columns as param. Eventually take in a picross-FEN """

        layout = Layout(root)

        # nonogram notation 1.
        '2, 1,. 2, 1, 3,. 7,. 1, 3,. 2, 1... 2,. 2, 1,. 1, 1,. 3,. 1, 1,. 1, 1,. 2,. 1, 1,. 1, 2,. 2, ...'

        """ each value ends with a comma. Each group (column or row) ends with a period. 
            All COLUMNS are listed first, and then an ellipses (three periods), then all ROWS are listed 
            End with three periods. """



        # make the buttons
        # for a in range(10):
        #     for b in range(10):
        #         new_button = Button(layout.main_frame, height=3, width=6)
        #         new_button.grid(row=a, column=b)
