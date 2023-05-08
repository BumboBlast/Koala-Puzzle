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

        # how many columns there are
        column_clues_width = Notation.how_many_columns(notation) * 50

        # how long is the largest column (number of clues per column)
        column_clues_height = Notation.length_longest_column(notation) * 50

        # how long is the largest row (number of clues per row)
        row_clues_width = Notation.length_longest_row(notation) * 50

        # how many rows there are
        row_clues_height = Notation.how_many_columns(notation) * 50

        # # vertical clues frame. Container holds the vertical clues. Rectangle above the nonogram.
        self.column_clues = Frame(self.game_frame, bg='yellow', width=column_clues_width, height=column_clues_height,
                                  highlightbackground='black', highlightthickness='2')
        self.column_clues.grid(row=0, column=1, sticky='SW')
        self.column_clues.grid_propagate(False)

        # horizontal clues frame. Container holds the horizontal clues. Rectangle to the left of the nonogram.
        self.row_clues = Frame(self.game_frame, bg='light green', width=row_clues_width, height=row_clues_height,
                               highlightbackground='black', highlightthickness='2')
        self.row_clues.grid(row=1, column=0, sticky='NE')
        self.row_clues.grid_propagate(False)

        # corner frame. Represents the empty space between the clues, complement of the picross board.
        self.corner_frame = Frame(self.game_frame, bg='cyan', width=row_clues_width, height=column_clues_height,
                                  highlightbackground='black', highlightthickness='2')
        self.corner_frame.grid(row=0, column=0, sticky='SE')
        self.corner_frame.grid_propagate(False)

        # picross frame. Container holds the nonogram board.
        self.picross_frame = Frame(self.game_frame, bg='lavender', width=column_clues_width, height=row_clues_height,
                                   highlightbackground='black', highlightthickness='2')
        self.picross_frame.grid(row=1, column=1, sticky='NW')
        self.picross_frame.grid_propagate(False)

        """ Tile the clue frames."""

        # (these values - index of current clue) to put the grid's cell relative to the bottom.
        # Otherwise, the grid would be upside down.
        invert_col = Notation.length_longest_column(notation)
        invert_clue = Notation.how_many_columns(notation)

        # button dimensions
        button_height = 1
        button_width = 2

        for this_column in range(0, len(Notation.all_columns(notation))):
            for clue in range(0, len(Notation.all_columns(notation)[this_column])):

                # make a button for this clue and put it in a column
                new_button = Button(self.column_clues, text=Notation.all_columns(notation)[this_column][clue], height=button_height, width=button_width)
                new_button.grid(row=invert_col - clue, column=invert_clue - this_column)
