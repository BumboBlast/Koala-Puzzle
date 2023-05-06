from tkinter import *

"""This is a list of functions that configure the layout of the screen. Provides no functionality."""


class Layout:
    def __init__(self, root):
        # Main Frame. Container that holds the entire screen.
        self.main_frame = Frame(root, bg='light blue')
        self.main_frame.pack()

        # horizontal clues frame. Container holds the horizontal clues. Rectangle to the left of the nonogram.
        self.horizontal_clues = Frame(self.main_frame, bg='pink', width=100, height=100)
        self.horizontal_clues.pack(padx=10, pady=10)

        # vertical clues frame. Container holds the vertical clues. Rectangle above the nonogram.
        self.vertical_clues = Frame(self.main_frame, bg='light green', width=100, height=100)
        self.vertical_clues.pack(padx=10, pady=10)
