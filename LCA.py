tree = [3,5,1,6,2,0,8,None,None,7,4] # right side of last level is 4 Nones, but unnecessary
# according to example, trees are unsorted (in terms of values)

def LCA(binarytree, node1, node2): # assume tree passed is sorted 2d array ran through levelsort
    node1_ancestors = node1 # initialize with itself as an ancestor
    node2_ancestors = node2

    def levelfinder(binarytree, node):
        i = 1
        for level in binarytree:
            if node in level:
                return i
            i += 1
        return None # if node not in tree


    def index(binarytree, node, level):
        i = 1
        for nodes in binarytree[level]:
            if node == nodes:
                return i
            i += 1

    node1_level = levelfinder(binarytree, node1)
    node1_index = index(binarytree, node1, node1_level)
    node2_level = levelfinder(binarytree, node2)
    node2_index = index(binarytree, node2, node2_level)

    def ancestors(binarytree, nodeindex, nodelevel):
        ancestorlist = []
        while nodelevel > 0:
            nodelevel -= 1
            ancestorlist.append(binarytree[nodelevel[(nodeindex//2 + nodeindex%2)]])
    # goal: LCA
        # need: full ancestor lists
            # need: descendant index


    # also according to example, will assume no duplicate nodes
    # level with 4 sublevel 8: (1,2) (3,4) (5,6) (7,8)
    # check if ancestor through if index == ancestor index *2 or ancestor index *2 -1


def levelsort(binarytree):
    levelsize = 1
    sortedtree = [] #2d array
    while binarytree: # is not empty
        temp = binarytree[0:levelsize]
        sortedtree.append(temp)
        for node in binarytree[0:levelsize]:
            binarytree.remove(node)
        levelsize *= 2
    return sortedtree

levelsort(tree)
# print(LCA(tree))

