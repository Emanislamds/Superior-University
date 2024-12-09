class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs_with_stack(root):
    stack = [root]
    visited = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current.value)

            for child in reversed(current.children):
                stack.append(child)

    return visited
root = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)
child4 = Node(5)

root.children = [child1, child2]
child1.children = [child3, child4]

result = dfs_with_stack(root)
print("DFS Traversal:", result)
