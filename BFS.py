from collections import deque

#the example output does not correspond to the example maze which was confusing

# operate under assumption you can only move down the tree vertically (no diagonal or jumping)
def BFSmaze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])

    #key: up, down, left, right
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    queue = deque()
    queue.append([start])
    solutions = 0

    while queue:
        path = queue.popleft()
        r, c = path[-1]  # newest item
        if (r, c) == goal:
            solutions += 1
            print(f"at goal with {len(path) - 1} moves")
            print_path(maze, path)
            continue

        #neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc # assign neighbors

            if (0 <= nr < rows and # main bfs logic
                0 <= nc < cols and
                maze[nr][nc] == 1 and
                (nr, nc) not in path):  # avoid cycles

                new_path = path + [(nr, nc)]
                queue.append(new_path)

    print("total recursion solutions:", solutions)


def print_path(maze, path):
    rows, cols = len(maze), len(maze[0])
    grid = [[0] * cols for _ in range(rows)]

    for r, c in path:
        grid[r][c] = 1

    for row in grid:
        print(" ".join(str(x) for x in row))
    print()

maze = [
    [1,1,1,1,1],
    [0,1,1,1,1],
    [0,0,0,0,1],
    [1,0,1,1,1],
    [0,0,0,1,1],
]

BFSmaze(maze, (0,0), (4,4))


