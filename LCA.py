tree = [3,5,1,6,2,0,8,None,None,7,4] # right side of last level is 4 Nones, but unnecessary
# according to example, trees are unsorted (in terms of values)

def LCA(binarytree, node1, node2): # assume tree passed is sorted 2d array ran through levelsort
    node1_ancestors = [node1] # initialize with itself as an ancestor
    node2_ancestors = [node2]

    def levelfinder(node):
        i = 1
        for level in binarytree:
            if node in level:
                return i
            i += 1

    node1_level = levelfinder(node1)
    node2_level = levelfinder(node2)

    def find_ancestors(node):



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

print(levelsort(tree))
# print(LCA(tree))

