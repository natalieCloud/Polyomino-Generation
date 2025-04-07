import quads
tree = quads.QuadTree(
    (0,0),
    5,
    1,

)

tree.insert((0,0))
tree.insert((1,0))
tree.insert((2,0))
tree.insert((-1,0))
tree.insert((-2,0))

quads.visualize(tree)