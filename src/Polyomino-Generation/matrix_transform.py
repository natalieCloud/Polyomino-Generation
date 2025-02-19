#!/usr/bin/env python
import numpy as np # type: ignore

class MatTform:

    CURR_REP = []

    def flip_x():
        MatTform.CURR_REP = np.fliplr(MatTform.CURR_REP)

    def flip_y():
        MatTform.CURR_REP = np.flipud(MatTform.CURR_REP)

    def rot_right():
        MatTform.CURR_REP = np.rot90(MatTform.CURR_REP, 3)

    def rot_left():
        MatTform.CURR_REP = np.rot90(MatTform.CURR_REP)