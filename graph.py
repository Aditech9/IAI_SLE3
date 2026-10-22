"""Deterministic graph generator for the BFS vs DFS profiling project."""

def build_graph(size=1000):
    """Build an adjacency-list graph with sequential edges and shortcuts."""
    if size < 1:
        raise ValueError("size must be at least 1")
    graph = {node: [] for node in range(size)}
    for node in range(size):
        if node + 1 < size:
            graph[node].append(node + 1)
        for jump in (10, 50, 100):
            destination = node + jump
            if destination < size:
                graph[node].append(destination)
    return graph
