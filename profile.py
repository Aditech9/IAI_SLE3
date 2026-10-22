"""Command-line benchmark comparing BFS and DFS."""
import argparse
import timeit
from bfs import bfs
from dfs import dfs
from graph import build_graph

def profile_search(search_fn, start, goal, graph, repeat=3):
    """Measure repeated runs and return timing plus the search result."""
    if repeat < 1:
        raise ValueError("repeat must be at least 1")
    timings = timeit.repeat(lambda: search_fn(start, goal, graph), repeat=repeat, number=1)
    result = search_fn(start, goal, graph)
    milliseconds = [elapsed * 1000 for elapsed in timings]
    return {
        "result": result,
        "best_ms": min(milliseconds),
        "worst_ms": max(milliseconds),
        "average_ms": sum(milliseconds) / len(milliseconds),
        "runs": repeat,
    }

def main():
    parser = argparse.ArgumentParser(description="Compare BFS and DFS graph traversal performance.")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--goal", type=int, default=999)
    parser.add_argument("--nodes", type=int, default=1000)
    parser.add_argument("--repeat", type=int, default=3)
    parser.add_argument("--algorithm", choices=("bfs", "dfs", "both"), default="both")
    args = parser.parse_args()
    if args.nodes < 1:
        parser.error("--nodes must be at least 1")
    if not (0 <= args.start < args.nodes and 0 <= args.goal < args.nodes):
        parser.error("start and goal must be within the generated graph")
    if args.repeat < 1:
        parser.error("--repeat must be at least 1")
    graph = build_graph(args.nodes)
    algorithms = {"bfs": bfs, "dfs": dfs}
    selected = algorithms.items() if args.algorithm == "both" else [(args.algorithm, algorithms[args.algorithm])]
    print(f"Graph nodes: {args.nodes} | Start: {args.start} | Goal: {args.goal}")
    for name, search_fn in selected:
        metrics = profile_search(search_fn, args.start, args.goal, graph, args.repeat)
        result = metrics["result"]
        print(f"\n{name.upper()}")
        print(f"Found: {result['found']}")
        print(f"Path length (nodes): {len(result['path'])}")
        print(f"Nodes expanded: {result['expanded_nodes']}")
        print(f"Best time: {metrics['best_ms']:.4f} ms")
        print(f"Worst time: {metrics['worst_ms']:.4f} ms")
        print(f"Average time: {metrics['average_ms']:.4f} ms")

if __name__ == "__main__":
    main()
