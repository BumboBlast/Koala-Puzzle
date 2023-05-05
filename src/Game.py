from tkinter import *


class Game:

    def __init__(self):
        """ Makes a new game (picross) with rows/columns as param. Eventually take in a picross-FEN """

        for a in range(10):
            for b in range(10):
                new_button = Button(height=3, width=6)
                new_button.grid(row=a, column=b)
