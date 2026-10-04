# SLE-3 C4 Architecture – Graph Search System

## 1. System Title & Short Description

The Graph Search System is a basic AI/search system for traversing a graph and finding a route from a start node to a goal node. It supports Breadth-First Search (BFS) and Depth-First Search (DFS). The user supplies the graph and search details, the Search Engine processes the graph, and the Output Module reports the result. The architecture is represented using the complete C4 Model.

## 2. Context Diagram – Level 1

**User → Graph Search System → Search/Traversal Result**

The user provides graph information, a start node, a goal node and the selected search method. The system processes the request and returns a traversal order or discovered path. No mandatory external system is required for this basic implementation.

Diagram: `diagrams/c4_context.svg`

## 3. Container Diagram – Level 2

- **Input Module:** accepts graph/search details from the user.
- **Search Engine:** executes BFS or DFS.
- **Memory / Visited Set:** stores processed nodes to avoid repeated work.
- **Output Module:** displays traversal/path results.

Diagram: `diagrams/c4_container.svg`

## 4. Component Diagram – Level 3

The Component view focuses only on the **Search Engine** container:

- **Frontier:** stores nodes waiting to be processed.
- **Explored / Closed Set:** tracks processed nodes.
- **Goal Test:** checks whether the current node is the required goal.
- **Path Reconstructor:** builds the final path using parent relationships.

Diagram: `diagrams/c4_component.svg`

## 5. Code Level Overview – Level 4

- `class Graph` : stores the graph structure and neighbors.
- `def bfs()` : performs breadth-first traversal/search.
- `def dfs()` : performs depth-first traversal/search.
- `def reconstruct_path()` : rebuilds the route from parent links.
- `def read_input()` : obtains graph/search parameters.
- `def display_result()` : presents the final result.

## 6. Design Decisions

The architecture uses four small containers because the system is educational and should remain easy to understand. The Search Engine is selected for the Level 3 Component view because it contains the main AI/search logic. A visited set is kept separate conceptually so repeated nodes can be controlled clearly. The Code level stays limited to names and responsibilities rather than large source code.

## 7. AI Contribution Note

AI tools were used to assist with architecture organization, documentation wording, diagram structure and consistency checking. The student selected and reviewed the final system structure, code-level names, and design decisions.

## 8. Conclusion

The C4 Model makes the Graph Search System easier to understand at different levels of detail. Starting from user interaction and moving toward containers, components and functions gives a clear picture of how the system works. The activity also helped connect implementation choices with architectural decisions.
