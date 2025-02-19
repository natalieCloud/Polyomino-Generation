#!/usr/bin/env python

class Commands:

    ROOTS = []
    BRANCHES = []
    BASE_FIGURE = 0
    CURRENT_FIGURE = 0
    root_idx = 0
    branch_idx = 0

    # load in the roots for the selected polyomino
    def load_roots(event):
        Commands.CURRENT_FIGURE = Commands.ROOTS[0]

    # load in the branches for the selected polyomino
    def load_branch(event):
        Commands.CURRENT_FIGURE = Commands.BRANCHES[0]
    
    # load the next root for the selected polyomino
    def next_root(event):
        Commands.ROOTS.append(Commands.ROOTS.pop(0))
        Commands.CURRENT_FIGURE = Commands.ROOTS[0]   
    
    # load the prev root for the selected polyomino
    def prev_root(event):
        Commands.ROOTS.insert(0, Commands.ROOTS.pop)
        Commands.CURRENT_FIGURE = Commands.ROOTS[0]

    # load the next branch for the selected polyomino
    def next_branch(event):
        Commands.BRANCHES.append(Commands.BRANCHES.pop(0))
        Commands.CURRENT_FIGURE = Commands.BRANCHES[0]

    # load the prev branch for the selected polyomino
    def prev_branch(event):
        Commands.BRANCHES.insert(0, Commands.BRANCHES.pop)
        Commands.CURRENT_FIGURE = Commands.BRANCHES[0]
    
    # load the base polyomino back
    def base_figure(event):
        Commands.CURRENT_FIGURE = Commands.BASE_FIGURE