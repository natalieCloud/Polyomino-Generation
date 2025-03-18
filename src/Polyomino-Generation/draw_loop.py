#!/usr/bin/env python
from tkinter import Tk, Canvas
from polyomino import Polyomino

import numpy as np

class Settings():
    FILLED_COLOR_BG = "purple"
    EMPTY_COLOR_BG = "white"
    FILLED_COLOR_BORDER = "black"
    EMPTY_COLOR_BORDER = "black"

class Cell():

    def __init__(self, master, x, y, size, isFill):
        """ Constructor of the object called by Cell(...) """
        self.master = master
        self.abs = x
        self.ord = y
        self.size= size
        self.fill = isFill

    def _switch(self):
        """ Switch if the cell is filled or not. """
        self.fill= not self.fill

    def draw(self):
        """ order to the cell to draw its representation on the canvas """
        if self.master:
            fill = Settings.FILLED_COLOR_BG
            outline = Settings.FILLED_COLOR_BORDER

            if not self.fill:
                fill = Settings.EMPTY_COLOR_BG
                outline = Settings.EMPTY_COLOR_BORDER

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)
                

class CellGrid(Canvas):

    cellSize = 50
    polyname: str
    _our_poly: Polyomino

    def __init__(self, master, grand_poly : Polyomino, *args, **kwargs):
        self._our_poly : Polyomino = grand_poly
        rowNumber, columnNumber = self._our_poly.get_size()
        Canvas.__init__(self, master, width = self.cellSize * columnNumber , height = self.cellSize * rowNumber, *args, **kwargs)
       
        self.loc_rep = self._our_poly.get_rep()
        self.edit_mode = False

        self.grid = []
        for row in range(rowNumber):

            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, self.cellSize, self.loc_rep[row][column]))

            self.grid.append(line)

        #memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []

        #bind click action
        self.bind("<Button-1>", self.handleMouseClick)  
        #bind moving while clicking
        self.bind("<B1-Motion>", self.handleMouseMotion)
        #bind release button action - clear the memory of midified cells.
        self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())
        self.bind("e", lambda event: self.switch_edit())
        self.draw()

    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def switch_edit(self):
        self.edit_mode = not self.edit_mode

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column
    
    def flip_cells(self, new_rep: np.array):
        updated_state = self.diff_mat(self.loc_rep, new_rep)
        self.loc_rep = new_rep
        changed_x, changed_y = np.where(updated_state == True)
        for x, y in zip(changed_x, changed_y):
            cell = self.grid[x][y]
            cell._switch()
            cell.draw()

    def get_poly(self):
        return self._our_poly

    def diff_mat(self, curr_grid, new_rep):
        return np.logical_xor(curr_grid, new_rep)    

    def redef_poly(self, poly_p: Polyomino):
        self._our_poly = poly_p
        rowNumber, columnNumber = self._our_poly.get_size()

        Canvas.config(self, width = self.cellSize * columnNumber , height = self.cellSize * rowNumber)

        self.loc_rep = self._our_poly.get_rep()
        self.edit_mode = False

        self.grid = []
        for row in range(rowNumber):

            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, self.cellSize, self.loc_rep[row][column]))

            self.grid.append(line)

        #memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []
        self.draw()

    def redisp_poly(self, poly_p: Polyomino):
        rowNumber, columnNumber = poly_p.get_size()

        Canvas.config(self, width = self.cellSize * columnNumber , height = self.cellSize * rowNumber)

        self.loc_rep = poly_p.get_rep()
        self.edit_mode = False

        self.grid = []
        for row in range(rowNumber):

            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, self.cellSize, self.loc_rep[row][column]))

            self.grid.append(line)

        #memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []
        self.draw()

    def handleMouseClick(self, event):
        if self.edit_mode:
            row, column = self._eventCoords(event)
            cell = self.grid[row][column]
            cell._switch()
            cell.draw()
            self.switched.append(cell)

    def handleMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if cell not in self.switched:
            cell._switch()
            cell.draw()
            self.switched.append(cell)