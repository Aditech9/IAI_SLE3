"""Simple BFS and DFS graph-search example for SLE-3.

The program is intentionally small so the code-level architecture can
be mapped directly to the C4 documentation.
"""

from collections import deque


class Graph:
    def __init__(self, adjacency):
        self.adjacency = adjacency

    def neighbors(self, node):
        return self.adjacency.get(node, [])


def reconstruct_path(parent, start, goal):
    if goal != start and goal not in parent:
        return None

    path = []
    current = goal

    while current is not None:
        path.append(current)
        if current == start:
            break
        current = parent.get(current)

    path.reverse()
    return path


def bfs(graph, start, goal):
    frontier = deque([start])
    visited = {start}
    parent = {start: None}
    order = []

    while frontier:
        current = frontier.popleft()
        order.append(current)

        if current == goal:
            return order, reconstruct_path(parent, start, goal)

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                frontier.append(neighbor)

    return order, None


def dfs(graph, start, goal):
    frontier = [start]
    visited = {start}
    parent = {start: None}
    order = []

    while frontier:
        current = frontier.pop()
        order.append(current)

        if current == goal:
            return order, reconstruct_path(parent, start, goal)

        # Reverse insertion keeps the displayed order predictable.
        for neighbor in reversed(graph.neighbors(current)):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                frontier.append(neighbor)

    return order, None


def read_input():
    graph = Graph({
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    })

    start = input("Enter start node (A-F): ").strip().upper()
    goal = input("Enter goal node (A-F): ").strip().upper()
    method = input("Choose BFS or DFS: ").strip().upper()

    if start not in graph.adjacency or goal not in graph.adjacency:
        raise ValueError("Start/goal must be one of A-F.")

    if method not in {"BFS", "DFS"}:
        raise ValueError("Choose BFS or DFS.")

    return graph, start, goal, method


def display_result(order, path, method):
    print(f"\nSearch Method: {method}")
    print("Traversal Order:", " -> ".join(order))
    if path:
        print("Path Found:", " -> ".join(path))
    else:
        print("Path Found: No path")


def main():
    try:
        graph, start, goal, method = read_input()
        if method == "BFS":
            order, path = bfs(graph, start, goal)
        else:
            order, path = dfs(graph, start, goal)
        display_result(order, path, method)
    except ValueError as exc:
        print(f"Input Error: {exc}")


if __name__ == "__main__":
    main()
