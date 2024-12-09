#Task 1: BFS Without Queue & Without Node
def bfs_without_queue(graph, start):
    visited = []
    to_visit = [start]

    while to_visit:
        current = to_visit.pop(0)
        visited.append(current)
        to_visit.extend(graph[current]) 

    return visited

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

result = bfs_without_queue(graph, 1)
print("BFS Traversal:", result)

#Task 2: BFS with Queue & Node
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs_with_queue(root):
    queue = [root]
    visited = []

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.append(current.value)
            for child in current.children:
                queue.append(child)

    return visited

root = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)
child4 = Node(5)

root.children = [child1, child2]
child1.children = [child3, child4]

result = bfs_with_queue(root)
print("BFS Traversal:", result)
