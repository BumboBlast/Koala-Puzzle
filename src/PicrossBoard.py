""" This will be the interactive portion of the game.
    A rectangle of TK buttons that you can left-click (filled),
    double-left-click (mark as empty). 
    Can drag the cursor while held to shade in a region. 
    
    Bordering the picross board will be the clues for each row/ column.

    This class will draw the board and configure its functionality. Different classes will implement the game's rules."""

from Notation import *
from Tile import *
from Layout import *


class PicrossBoard:

    def __init__(self, notation, picross_frame):
        """ Make a new picross board according to the input dimensions. """

        # put as many buttons in the picross board as there are rows * columns
        for row in range(0, len(Notation.all_rows(notation))):
            for col in range(0, len(Notation.all_columns(notation))):
                new_button = ButtonTile(picross_frame)
                new_button.button.grid(row=row, column=col)
