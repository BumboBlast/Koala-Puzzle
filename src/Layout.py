from tkinter import *

"""This is a list of functions that configure the layout of the screen. Provides no functionality."""


class Layout:
    def __init__(self, root):
        root.update_idletasks()

        game_height = root.winfo_height() * 0.92
        game_width = game_height

        # Main Frame. Container that holds the entire screen.
        self.main_frame = Frame(root, bg='light blue', pady=(root.winfo_height() - game_height) / 2)
        self.main_frame.place(x=0, y=0, width=root.winfo_width(), height=root.winfo_height())

        # Game frame. Container that holds all UI elements
        self.game_frame = Frame(self.main_frame, bg='light pink')
        self.game_frame.pack()

        """ At the moment, the sizes are relative to this empty corner.
        Later, want them to be relative to the clue_frames, so i can input a variable number of clues. """
        corner_width = game_width * 0.3
        corner_height = corner_width

        horizontal_clues_width = corner_width
        horizontal_clues_height = game_height - corner_height

        vertical_clues_width = game_width - corner_width
        vertical_clues_height = corner_height

        picross_width = vertical_clues_width
        picross_height = horizontal_clues_height

        # corner frame. Represents the empty space between the clues, complement of the picross board.
        self.corner_frame = Frame(self.game_frame, bg='light grey', width=corner_width, height=corner_height)
        self.corner_frame.grid(row=0, column=0)

        # picross frame. Container holds the nonogram board.
        self.picross_frame = Frame(self.game_frame, bg='red', width=picross_width, height=picross_height)
        self.picross_frame.grid(row=1, column=1)

        # horizontal clues frame. Container holds the horizontal clues. Rectangle to the left of the nonogram.
        self.horizontal_clues = Frame(self.game_frame, bg='purple', width=horizontal_clues_width, height=horizontal_clues_height)
        self.horizontal_clues.grid(row=1, column=0)

        # # vertical clues frame. Container holds the vertical clues. Rectangle above the nonogram.
        self.vertical_clues = Frame(self.game_frame, bg='light green', width=vertical_clues_width, height=vertical_clues_height)
        self.vertical_clues.grid(row=0, column=1)


