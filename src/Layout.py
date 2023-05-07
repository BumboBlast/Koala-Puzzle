from tkinter import *
from Notation import *

"""This is a list of functions that configure the layout of the screen. Provides no functionality."""


class Layout:
    def __init__(self, root, notation):
        root.update_idletasks()
        root.grid_propagate(False)

        game_height = root.winfo_height() * 0.92
        game_width = game_height

        # Main Frame. Container that holds the entire screen.
        self.main_frame = Frame(root, bg='light blue')
        self.main_frame.pack(fill='both', expand=True)
        self.main_frame.grid_propagate(False)

        # Game frame. Container that holds all UI elements
        self.game_frame = Frame(self.main_frame, bg='light pink', width=game_width, height=game_height, padx=10)
        self.game_frame.pack(fill='none', expand=True)

        # this is so the grid cells are centered on the game frame.
        self.game_frame.grid_propagate(False)
        self.game_frame.grid_rowconfigure(0, weight=1)
        self.game_frame.grid_rowconfigure(1, weight=1)
        self.game_frame.grid_columnconfigure(0, weight=1)
        self.game_frame.grid_columnconfigure(1, weight=1)

        """ At the moment, the sizes are relative to the clue_frames, so i can input a variable number of clues. """

        column_clues_width = 600  # how many columns there are
        column_clues_height = 100  # how long is the largest column (number of clues per column)
        row_clues_width = 100  # how long is the largest row (number of clues per row)
        row_clues_height = 200  # how many rows there are

        # # vertical clues frame. Container holds the vertical clues. Rectangle above the nonogram.
        self.column_clues = Frame(self.game_frame, bg='yellow', width=column_clues_width, height=column_clues_height,
                                  highlightbackground='black', highlightthickness='2')
        self.column_clues.grid(row=0, column=1, sticky='SW')

        # horizontal clues frame. Container holds the horizontal clues. Rectangle to the left of the nonogram.
        self.row_clues = Frame(self.game_frame, bg='light green', width=row_clues_width, height=row_clues_height,
                               highlightbackground='black', highlightthickness='2')
        self.row_clues.grid(row=1, column=0, sticky='NE')

        # corner frame. Represents the empty space between the clues, complement of the picross board.
        self.corner_frame = Frame(self.game_frame, bg='cyan', width=row_clues_width, height=column_clues_height,
                                  highlightbackground='black', highlightthickness='2')
        self.corner_frame.grid(row=0, column=0, sticky='SE')

        # picross frame. Container holds the nonogram board.
        self.picross_frame = Frame(self.game_frame, bg='lavender', width=column_clues_width, height=row_clues_height,
                                   highlightbackground='black', highlightthickness='2')
        self.picross_frame.grid(row=1, column=1, sticky='NW')

        print(Notation.length_longest_row(notation))
