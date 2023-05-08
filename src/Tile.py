from tkinter import *
from Notation import *


class Tile:

    def __init__(self, master_frame):
        self.width = 4
        self.height = 2
        self.button_text = ''


class ClueTile(Tile):

    def __init__(self, master_frame):
        super().__init__(master_frame)

        self.button = Button(
            master_frame,
            width=self.width,
            height=self.height,
            relief='raised',
            state='disabled'
        )


class ButtonTile(Tile):
    states = ['empty', 'filled', 'explicitly_unmarked']

    empty = {
        'text': '',
        'color': '#FFD9DF'
    }
    filled = {
        'text': '',
        'color': '#BFFFCB'
    }
    explicitly_unmarked = {
        'text': '',
        'color': '#FFC0CB'
    }

    def __init__(self, master_frame):
        super().__init__(master_frame)

        self.button = Button(
            master_frame,
            width=self.width,
            height=self.height
        )

        self.button.bind('<Enter>', lambda event: self.highlight_tile())
        self.button.bind('<Leave>', lambda event: self.de_highlight_tile())

    def highlight_tile(self):
        self.button.config(relief='solid')

    def de_highlight_tile(self):
        self.button.config(relief='raised')

    def show_empty(self):
        """ Change how this tile looks to being empty. """
        self.button.config(relief='raised')
        self.button.config(state='normal')
        self.button.config(bg=self.empty['color'])
        self.button.config(text=self.empty['text'])

    def show_filled(self):
        """ Change how this tile looks to being filled. """
        self.button.config(relief='raised')
        self.button.config(state='normal')
        self.button.config(bg=self.filled['color'])
        self.button.config(text=self.filled['text'])

    def show_explicitly_unmarked(self):
        """ Change how this tile looks to being explicitly_unmarked (x). """
        self.button.config(relief='raised')
        self.button.config(state='normal')
        self.button.config(bg=self.explicitly_unmarked['color'])
        self.button.config(text=self.explicitly_unmarked['text'])
