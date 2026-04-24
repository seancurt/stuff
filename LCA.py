import math

tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4] # right side of last level is 4 nones, but unnecessary
#  according to example, trees are unsorted (in terms of value)


def LCA(binarytree, node1, node2): # assume tree passed is 2d sorted array ran through levelsort
    # also assume no duplicate nodes
    def levelfinder(binarytree, node):
        for i, level in enumerate(binarytree):  # 0-based
            if node in level:
                return i
        return None

    def index(binarytree, node, level):
        for i, val in enumerate(binarytree[level]):  # 0-based
            if node == val:
                return i
        return None

    def ancestors(binarytree, nodeindex, nodelevel):
        global_index = (2 ** nodelevel - 1) + nodeindex

        path = []

        while global_index >= 0:
            # convert global index → (level, index)
            level = int(math.floor(math.log2(global_index + 1)))
            level_start = 2 ** level - 1
            index = global_index - level_start

            path.append(binarytree[level][index])

            if global_index == 0:
                break

            global_index = (global_index - 1) // 2

        path.reverse()
        return path

    def LCACalc(node1_ancestors, node2_ancestors):
        lca = None
        for a, b in zip(node1_ancestors, node2_ancestors):
            if a == b:
                lca = a
            else:
                break
        return lca

    node1_level = levelfinder(binarytree, node1)
    node1_index = index(binarytree, node1, node1_level)

    node2_level = levelfinder(binarytree, node2)
    node2_index = index(binarytree, node2, node2_level)

    node1_ancestors = ancestors(binarytree, node1_index, node1_level)
    node2_ancestors = ancestors(binarytree, node2_index, node2_level)
    lowestCommon = LCACalc(node1_ancestors, node2_ancestors)

    return lowestCommon


def levelsort(binarytree):
    levelsize = 1
    sortedtree = []

    i = 0
    n = len(binarytree)

    while i < n:
        sortedtree.append(binarytree[i:i + levelsize])
        i += levelsize
        levelsize *= 2

    return sortedtree


tree = levelsort(tree)
print(LCA(tree, 5, 4))