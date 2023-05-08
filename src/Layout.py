from tkinter import *
from Notation import *
from Tile import *

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
        # # vertical clues frame. Container holds the vertical clues. Rectangle above the nonogram.
        self.column_clues = Frame(self.game_frame, bg='yellow',
                                  highlightbackground='black', highlightthickness='2')
        self.column_clues.grid(row=0, column=1, sticky='SW')
        self.column_clues.grid_propagate()

        # horizontal clues frame. Container holds the horizontal clues. Rectangle to the left of the nonogram.
        self.row_clues = Frame(self.game_frame, bg='light green',
                               highlightbackground='black', highlightthickness='2')
        self.row_clues.grid(row=1, column=0, sticky='NE')
        self.row_clues.grid_propagate()

        # corner frame. Represents the empty space between the clues, complement of the picross board.
        self.corner_frame = Frame(self.game_frame, bg='cyan',
                                  highlightbackground='black', highlightthickness='2')
        self.corner_frame.grid(row=0, column=0, sticky='SE')
        self.corner_frame.grid_propagate()

        # picross frame. Container holds the nonogram board.
        self.picross_frame = Frame(self.game_frame, bg='lavender',
                                   highlightbackground='black', highlightthickness='2')
        self.picross_frame.grid(row=1, column=1, sticky='NW')
        self.picross_frame.grid_propagate()

        """ Tile the row clue frame."""

        # (this value - index of current clue) to put the grid's cell relative to the bottom.
        # Otherwise, the grid would be upside down.
        invert_row = Notation.length_longest_column(notation)

        # column data from notation [[1,1], [1,1]...]
        column_data = Notation.all_columns(notation)

        # reverse each column because grid is putting them in upside down
        for col in column_data:
            col.reverse()

        for this_column in range(0, len(column_data)):
            for clue in range(0, len(column_data[this_column])):
                # make a button for this clue and put it in a column
                new_button = ClueTile(self.column_clues)
                new_button.button.config(text=column_data[this_column][clue])
                new_button.button.grid(row=invert_row - clue, column=this_column)

        """ Tile the row frame!"""

        # (this value - index of current clue) to put the grid's cell relative to the bottom.
        # Otherwise, the grid would be upside down.
        invert_col = Notation.length_longest_row(notation)

        # row data from notation [[1,1], [1,1]...]
        row_data = Notation.all_rows(notation)

        # reverse each row because grid is putting them in backwards
        for row in row_data:
            row.reverse()

        for this_row in range(0, len(row_data)):
            for clue in range(0, len(row_data[this_row])):
                # make a button for this clue and put it in a column
                new_button = ClueTile(self.row_clues)
                new_button.button.config(text=row_data[this_row][clue])
                new_button.button.grid(row=this_row, column=invert_col - clue)

        # re-evaluate the frame dimensions.
        self.column_clues.update_idletasks()
        self.row_clues.update_idletasks()
        self.picross_frame.config(width=self.column_clues.winfo_width(), height=self.row_clues.winfo_height())
        self.corner_frame.config(width=self.row_clues.winfo_width(), height=self.column_clues.winfo_height())

        """ put as many buttons in the picross board as there are rows * columns """

        for row in range(0, len(Notation.all_rows(notation))):
            for col in range(0, len(Notation.all_columns(notation))):

                new_button = ButtonTile(self.picross_frame)
                new_button.button.grid(row=row, column=col)
