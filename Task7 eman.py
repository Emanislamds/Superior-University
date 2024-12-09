class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0  
        self.h = 0  
        self.f = 0 

def heuristic(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def get_neighbors(node, grid):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = node.x + dx, node.y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append(Node(nx, ny, node))
    return neighbors

def reconstruct_path(node):
    path = []
    while node:
        path.append((node.x, node.y))
        node = node.parent
    return path[::-1]

def a_star(start, goal, grid):
    open_list = [start]  # Nodes to explore
    closed_list = []     # Nodes already explored

    while open_list:
        current_node = min(open_list, key=lambda n: n.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        if current_node.x == goal.x and current_node.y == goal.y:
            return reconstruct_path(current_node)
        for neighbor in get_neighbors(current_node, grid):
            if neighbor in closed_list:
                continue
            
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor, goal)
            neighbor.f = neighbor.g + neighbor.h
            for open_node in open_list:
                if neighbor.x == open_node.x and neighbor.y == open_node.y and neighbor.g >= open_node.g:
                    break
            else:
                open_list.append(neighbor)

    return None  
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = Node(0, 0)
goal = Node(4, 4)

path = a_star(start, goal, grid)
if path:
    print("Path found:", path)
else:
    print("No path found")
