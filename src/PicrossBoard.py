""" This will be the interactive portion of the game.
    A rectangle of TK buttons that you can left-click (filled),
    double-left-click (mark as empty). 
    Can drag the cursor while held to shade in a region. 
    
    Bordering the picross board will be the clues for each row/ column.

    This class will draw the board and configure its functionality. Different classes will implement the game's rules."""


class PicrossBoard:

    def __init__(self):
        """ Make a new picross board according to the input dimensions. """
