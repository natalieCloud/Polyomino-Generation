#!/usr/bin/env python
import matplotlib.pyplot as plt
from polyomino import Polyomino
import numpy as np
import os
import csv

""" This is an eh implementation imo and WILL BE REFACTORED"""

root_dict = {
    '1a': [], '2a': ['1a'], '3a': ['2a'], '3b': ['2a'],
    '4a': ['3a'], '4b': ['3b'], '4c': ['3a'], '4d': ['3a', '3b'], '4e': ['3a', '3b'],
    '5a': ['4a', '4d'], '5b': ['4b', '4d'], '5c': ['4b'],
    '5d': ['4b', '4d', '4e'], '5e': ['4a', '4c', '4d', '4e'], '5f': ['4d'],
    '5g': ['4a', '4d', '4e'], '5h': ['4d', '4e'], '5i': ['4a'],
    '5j': ['4d'], '5k': ['4e'], '5l': ['4d']}

branch_dict = {
    '1a': ['2a'], '2a': ['3a', '3b'], '3a': ['4a', '4c', '4d', '4e'], '3b': ['4b', '4d', '4e'],
    '4a': ['5a', '5e', '5g', '5i'], '4b': ['5b', '5c', '5d'],
    '4c': ['5e'], '4d': ['5a', '5b', '5d', '5e', '5f', '5g', '5h', '5j', '5l'],
    '4e': ['5d', '5e', '5g', '5h', '5k'],
    '5a': [], '5b': [], '5c': [],
    '5d': [], '5e': [], '5f': [],
    '5g': [], '5h': [], '5i': [],
    '5j': [], '5k': [], '5l': []}

bases = {}

""" This is an eh implementation imo and WILL BE REFACTORED"""

def export(new_rep: np.array):
    np.save('data', new_rep)

def load():
    filep = os.path.join('data', 'polyominos.csv')
    with open(filep, mode='r') as file:
        csvF = csv.reader(file)
        datarr = list(csvF)
        for subarr in datarr:
            base_path = os.path.abspath(os.path.join('data',subarr[2]).replace('\\ ', '/')) # This is gross find a better way
            tmparr = np.load(base_path)
            bases[subarr[1]] = Polyomino(subarr[1], tmparr, branch_dict.get(subarr[1]), root_dict.get(subarr[1]))

load()

