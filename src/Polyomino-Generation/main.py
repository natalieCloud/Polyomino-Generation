#!/usr/bin/env python
import numpy as np
from tkinter import *
from draw_loop import CellGrid, Settings
from polyomino import Polyomino
from controller import Controller
from menu import TKMenu
import database_pipe

def main():

    database_pipe.load()

    _our_poly : Polyomino = database_pipe.bases.get('1a')

    app = Tk()
    app.title('Polyomino Generation')
    app.geometry('400x500')
    app.config(bg='#FAFAFA')

    grid = CellGrid(app, _our_poly)

    _our_controller = Controller(grid)
    _our_controller.loadContent()

    grid.pack()

    _our_menu = TKMenu(app, grid)
    _our_menu.load_menu()

    grid.focus_set()


    while True:
        app.update_idletasks()
        app.update()

if __name__ == "__main__":
    main()