from undir_graph import UndirGraph

class Node:
    """ 
        This class represents a polyomino node,  connecting it to its root and branch forms.

        name: given to distinguish it from other polyominos, equivalent to the display represetation name
        parents: list of the polyominos "root" polyomino by a factor of 1
        children: list of the polyomino's "branch" polyomino, again by factor of 1
    """

    _root: UndirGraph # The tree that the node is a part of

    _name: str # The node id
    _level: int # The level that the node is on
    _seen: bool # If the node has been seen or not, used for size calculation

    _ancestors_size: int # The number of ancestors a given node has
    _descendant_size: int # The number of descendants a given node has

    _parents: list[str] # The immediate ancestors of the node
    _children: list[str] # The immediate descendants of the node

    def __new__(cls, root_g, name_p):
        '''Returns instance of a node'''
        return super(Node, cls).__new__(cls)

    def __init__(self, root_g, name_p):
        '''Initilization'''
        self._root = root_g
        self._name = name_p
    
    def add_child(self, child: str):
        '''Adds a child to the children list'''
        self.children.append(child)

    def add_parent(self, parent: str):
        '''Adds a parent to the parent list'''
        self.parent.append(parent)

    def get_children(self):
        '''Returns list of children'''
        return self.children
    
    def get_parents(self):
        '''Returns list of parents'''
        return self.parents
    
    def ancestor_size(self):
        '''Find the number of ancestors for a given node'''
         
        pass

    def descendent_size(self):
        '''Find the number of children* spawning from this node'''

        pass