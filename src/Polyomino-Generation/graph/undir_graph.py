class UndirGraph:
    """ This class represents an undirected graph, allows for traversal 
    from parent -> child and vice versa. Designed for classification of polyomino relationships"""

    _tree_size: int # Size of the tree from the root node

    def __new__(cls):
        '''Returns instance of and undirected graph'''
        return super(cls, UndirGraph).__new__(cls)

    def __init__(self):
        '''Initilize the graph'''
        pass

    def sub_tree(self, node):
        '''Grabs a tree spawning at the specififed node'''
        pass

    def size(self):
        '''Gets the size of the tree spawning at the root node'''
        pass

    def clear_self(self):
        '''Resets the 'seen' value of al the nodes in the graph'''