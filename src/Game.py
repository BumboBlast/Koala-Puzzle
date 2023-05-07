from tkinter import *
from Layout import *


class Game:

    def __init__(self, root, notation):
        """ Makes a new game (picross) with rows/columns as param. Eventually take in a picross-FEN """

        layout = Layout(root, notation)


