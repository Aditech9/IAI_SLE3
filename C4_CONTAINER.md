# C4 Level 2 – Container Diagram

The system contains four main containers.

| Container | Responsibility |
|---|---|
| Input Module | Takes graph, start node, goal node and algorithm choice |
| Search Engine | Runs BFS or DFS |
| Memory / Visited Set | Stores visited nodes and prevents unnecessary repetition |
| Output Module | Shows traversal order and/or discovered path |

### Flow

Input Module → Search Engine → Memory / Visited Set → Output Module

The Search Engine uses the visited information during processing and sends the final search result to the Output Module.

See `diagrams/c4_container.svg`.
