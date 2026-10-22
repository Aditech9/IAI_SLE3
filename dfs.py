"""Iterative depth-first search with path and expansion metrics."""

def dfs(start, goal, graph):
    """Return path, expanded_nodes, and found status."""
    if start not in graph or goal not in graph:
        return {"path": [], "expanded_nodes": 0, "found": False}
    stack = [(start, [start])]
    visited = set()
    expanded_nodes = 0
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        expanded_nodes += 1
        if node == goal:
            return {"path": path, "expanded_nodes": expanded_nodes, "found": True}
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return {"path": [], "expanded_nodes": expanded_nodes, "found": False}
