#!/usr/bin/env python
import numpy as np
import database_pipe as dp
from polyomino import Polyomino
from draw_loop import CellGrid

class Controller:

    local_bind : CellGrid = None


    def __init__(self, cell_bind):
        self.local_bind = cell_bind

    def loadContent(self):
        self.local_bind.bind("d", self.rotRight)
        self.local_bind.bind("a", self.rotLeft)
        self.local_bind.bind("w", self.flipX)
        self.local_bind.bind("s", self.flipY)
        self.local_bind.bind("<Up>", self.moveUp)
        self.local_bind.bind("<Down>", self.moveDown)
        self.local_bind.bind("<Left>", self.moveLeft)
        self.local_bind.bind("<Right>", self.moveRight)
        self.local_bind.bind("k", self.nextRoot)
        self.local_bind.bind("j", self.prevRoot)
        self.local_bind.bind("i", self.nextBranch)
        self.local_bind.bind("u", self.prevBranch)
        self.local_bind.bind("b", self.redisp_base)

    def rotRight(self, event):
        self.local_bind.get_poly().rotate_right()
        self.local_bind.flip_cells(self.local_bind.get_poly().get_rep())

    def rotLeft(self, event):
        self.local_bind.get_poly().rotate_left()
        self.local_bind.flip_cells(self.local_bind.get_poly().get_rep())

    def flipX(self, event):
        self.local_bind.get_poly().flip_x()
        self.local_bind.flip_cells(self.local_bind.get_poly().get_rep())

    def flipY(self, event):
        self.local_bind.get_poly().flip_y()
        self.local_bind.flip_cells(self.local_bind.get_poly().get_rep())

    def moveUp(self, event):
        self.local_bind.get_poly().move_plane(-1, 0)
        self.local_bind.flip_cells(self.local_bind.get_poly().get_rep())

    def moveDown(self, event):
        self.local_bind.get_poly().move_plane(1, 0)
        self.local_bind.flip_cells(self.local_bind.get_poly().get_rep())

    def moveLeft(self, event):
        self.local_bind.get_poly().move_plane(-1, 1)
        self.local_bind.flip_cells(self.local_bind.get_poly().get_rep())

    def moveRight(self, event):
        self.local_bind.get_poly().move_plane(1, 1)
        self.local_bind.flip_cells(self.local_bind.get_poly().get_rep())

    def saveInFile(self, event):
        pass

    def redisp_base(self, event):
        self.local_bind.redisp_poly(self.local_bind.get_poly())

    def nextRoot(self, event):
        root = self.local_bind.get_poly().get_list_root(1)
        if root:
            self.local_bind.redisp_poly(dp.bases[root])

    def prevRoot(self, event):
        root = self.local_bind.get_poly().get_list_root(0)
        if root:
            self.local_bind.redisp_poly(dp.bases[root])

    def nextBranch(self, event):
        branch = self.local_bind.get_poly().get_list_branch(1)
        if branch:
            self.local_bind.redisp_poly(dp.bases[branch])

    def prevBranch(self, event):
        branch = self.local_bind.get_poly().get_list_branch(0)
        if branch:
            self.local_bind.redisp_poly(dp.bases[branch])

    


 

