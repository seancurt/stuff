class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def left_view(root):
    if not root:
        return []

    from collections import deque
    q = deque([root])
    result = []

    while q:
        level_size = len(q)

        for i in range(level_size):
            node = q.popleft()

            # first node of this level
            if i == 0:
                result.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)

print(left_view(root))