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