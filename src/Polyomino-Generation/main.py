#!/usr/bin/env python
import numpy as np
from tkinter import *
from draw_loop import CellGrid 
from commands import Commands
import database_pipe

def bindControls(root):
    # root.bind("<Up>", Commands.base_figure)
    pass

def loadContent():
    pass

def main():

    loadContent()

    app = Tk()

    bindControls(app)

    test_mat = database_pipe.base_mat

    grid = CellGrid(app, 6, 6, 100, test_mat)
    grid.pack()

    app.mainloop()


    pass

if __name__ == "__main__":
    main()