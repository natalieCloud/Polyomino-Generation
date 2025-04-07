from tkinter import *
from draw_loop import Settings, CellGrid
from polyomino import Polyomino
from controller import Controller
import database_pipe as DP

class TKMenu:
    """Defines the menu for the application"""

    _tk_ref: Tk = None
    _grid_ref: CellGrid = None

    COLORS = [
        "black",
        "white",
        "red",
        "blue",
        "purple",
        "yellow",
        "orange"
    ]
    BASES = [
        "1a",
        "2a",
        "3a",
        "3b",
        "4a",
        "4b",
        "4c",
        "4d",
        "4e",
        "5a",
        "5b",
        "5c",
        "5d",
        "5e",
        "5f",
        "5g",
        "5h",
        "5i",
        "5j",
        "5k",
        "5l",
    ]

    def __init__(self, tkmain, gridref):
        self._tk_ref = tkmain
        self._grid_ref = gridref
        

    def load_menu(self):

        # Grid nomino picker, main
        self._grid_ref.polyname = StringVar(self._tk_ref)
        self._grid_ref.polyname.set(self.BASES[0])
        _polyomino_m = OptionMenu(self._tk_ref, self._grid_ref.polyname, *self.BASES, command=self.select_base)
        self.select_base("1a")
        _polyomino_m.pack()

        # Color Picker, main
        Settings.FILLED_COLOR_BG = StringVar(self._tk_ref)
        Settings.FILLED_COLOR_BG.set(self.COLORS[4])
        _options_m = OptionMenu(self._tk_ref, Settings.FILLED_COLOR_BG, *self.COLORS, command=self.change_color)
        self.change_color(self.COLORS[4])
        _options_m.pack()

        # Guide text
        _text_m = Text(self._tk_ref, height=50, width=400)
        _text_m.pack()
        _text_m.insert(END, 
                     "Right Rotate: d\nLeft Rotate: a\n"
                     "X Axis Flip: w\nY Axis Flip: s\n"
                     "Edit Mode Toggle: e\n"
                     "Movement: Arrow Keys\n"
                     "---------------------------------\n"
                     "Warning - b to resume transformations/translations after these:\n"
                     "Branches <- u i ->\n"
                     "Roots <- j k ->\n")


    def change_color(self, choice):
        Settings.FILLED_COLOR_BG = choice
        self._grid_ref.draw()

    def select_base(self, choice):
        self._grid_ref.redef_poly(DP.bases.get(choice))
