"""Breadth-first search with path reconstruction and expansion metrics."""
from collections import deque

def bfs(start, goal, graph):
    """Return path, expanded_nodes, and found status."""
    if start not in graph or goal not in graph:
        return {"path": [], "expanded_nodes": 0, "found": False}
    queue = deque([start])
    visited = {start}
    parent = {}
    expanded_nodes = 0
    while queue:
        node = queue.popleft()
        expanded_nodes += 1
        if node == goal:
            path = [goal]
            while path[-1] != start:
                path.append(parent[path[-1]])
            path.reverse()
            return {"path": path, "expanded_nodes": expanded_nodes, "found": True}
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
    return {"path": [], "expanded_nodes": expanded_nodes, "found": False}
