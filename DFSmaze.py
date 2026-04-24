from BFS import * # my program for the bfs version with the print_path function

def DFSmaze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    solutions = 0

    def dfs(path):
        nonlocal solutions

        r, c = path[-1]

        #base
        if (r, c) == goal:
            solutions += 1
            print(f"at the goal with {len(path) - 1} moves")
            print_path(maze, path)
            return


        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and
                    0 <= nc < cols and
                    maze[nr][nc] == 1 and
                    (nr, nc) not in path):  # avoid cycles

                dfs(path + [(nr, nc)])

    # recurse
    dfs([start])

    print("total recursion solutions:", solutions)

maze = [
    [1,1,1,1,1],
    [0,1,1,1,1],
    [0,0,0,0,1],
    [1,0,1,1,1],
    [0,0,0,1,1],
]

DFSmaze(maze, (0,0), (4,4))
