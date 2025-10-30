# filesystem.py

class Node:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size
        self.children = children or []


def total_size(node):
    
    if node is None:
        return 0
    # If no children, it’s a file
    if not node.children:
        return node.size
    # Otherwise, folder: sum of its own size (usually 0) + all descendants
    return node.size + sum(total_size(child) for child in node.children)


def folder_sizes(node):
    
    result = {}
    if node is None:
        return result

    # If it's a folder (has children)
    if node.children:
        result[node.name] = total_size(node)
        for child in node.children:
            result.update(folder_sizes(child))

    return result


from collections import deque

def level_order(node):
    """Return list of levels, each level a list of node names."""
    if node is None:
        return []

    result = []
    q = deque([node])

    while q:
        level_size = len(q)
        level_names = []
        for _ in range(level_size):
            current = q.popleft()
            level_names.append(current.name)
            for child in current.children:
                q.append(child)
        result.append(level_names)
    return result
