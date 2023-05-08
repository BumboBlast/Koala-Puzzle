from tkinter import *
from Notation import *


class Tile:

    def __init__(self, master_frame):
        self.width = 4
        self.height = 2

        self.button_text = ''

        self.button = Button(
            master_frame,
            height=self.height,
            width=self.width
        )
