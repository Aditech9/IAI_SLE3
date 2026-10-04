# C4 Level 1 – Context Diagram

## System
**Graph Search System (BFS / DFS)**

## Actors and Systems

### User
Provides the graph, start node, goal node and selected search algorithm.

### Graph Search System
Receives the request, performs BFS or DFS, and produces the search result.

## Main Interaction

**User → Graph Search System:** graph/search request  
**Graph Search System → User:** traversal order or path result

See `diagrams/c4_context.svg` for the diagram.
