#!/usr/bin/env python
import numpy as np
from collections import deque


class Polyomino:
    """ This class contains a matrix representation of the polyomino quad tree structure"""

    _name: str # This string contains the id for the fixed form of the polyomino, used to retrieve the branches and roots
    _grid_rep: np.array # The current matrix representation of the polyomino
    _grid_roots = [] # The associated roots for our current figure's representation
    _grid_branches = [] # The associated brances for our figures representation
    # TODO when switching between roots make it so that the it matches the transform

    def __new__(cls, name_p, array_p, branches_p, roots_p):
        instance = super(Polyomino, cls).__new__(cls)
        return instance

    def __init__(self, name_p, array_p, branches_p, roots_p):
        """ Class initilizer """
        self._name = name_p
        self._grid_rep = array_p
        self._grid_roots = deque(roots_p)
        self._grid_branches = deque(branches_p)

    def init_selection(self, id):
        """ Pulls user desired graph from the database"""
        pass

    def init_from_tree(self):
        """ Loads the matrix representation from a quad tree struct """
        pass

    def pass_to_tree(self):
        """ Exports the matrix represenation to a quad tree, if able """
        pass

    def rotate_right(self):
        """ Rotates the current representation 90 deg clockwise"""
        self._grid_rep = np.rot90(self._grid_rep, k=1, axes=(1,0))

    def rotate_left(self):
        """ Rotates the current representation 90 deg counter-clockwise"""
        self._grid_rep = np.rot90(self._grid_rep, k=1, axes=(0,1))

    def flip_y(self):
        """ Flips the current representation on the y axis """
        self._grid_rep = np.flipud(self._grid_rep)

    def flip_x(self):
        """ Flips the current representation on the x axis """
        self._grid_rep = np.fliplr(self._grid_rep)

    def move_plane(self, direction_p, axis_p):
        self._grid_rep = np.roll(self._grid_rep, direction_p, axis_p)

    def get_list_root(self, dir):
        root_ref = ''
        if self._grid_roots and dir:
            root_ref = self._grid_roots.popleft()
            self._grid_roots.append(root_ref)
        if self._grid_roots and not dir:
            root_ref = self._grid_roots.pop()
            self._grid_roots.appendleft(root_ref)
        return root_ref
    
    def get_list_branch(self, dir):
        root_ref = ''
        if self._grid_branches and dir:
            root_ref = self._grid_branches.popleft()
            self._grid_branches.append(root_ref)
        if self._grid_branches and not dir:
            root_ref = self._grid_branches.pop()
            self._grid_branches.appendleft(root_ref)
        return root_ref

    # def save_to_file(self):
    #     """ Saves the current representation to a db file"""
    #     DP.export(self._grid_rep)

    def get_rep(self):
        return self._grid_rep
    
    def get_size(self):
        """Should this help?"""
        return self._grid_rep.shape