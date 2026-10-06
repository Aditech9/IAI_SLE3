# C4 Level 3 – Component Diagram

## Selected Container
**Search Engine**

The guideline says to choose one important container, usually the Search Engine, and show its internal components. Components should not be drawn for every container. fileciteturn0file0L64-L71

## Components

1. **Frontier / Queue / Stack** – Holds nodes waiting to be explored.
2. **Explored / Closed Set** – Tracks nodes already processed.
3. **Goal Test** – Checks whether the current node is the destination.
4. **Path Reconstructor** – Builds the route from the goal back to the start.

## Component Diagram

~~~mermaid
flowchart TB
    SE[Search Engine]
    F[Frontier - Queue for BFS / Stack for DFS]
    E[Explored / Closed Set]
    G[Goal Test]
    P[Path Reconstructor]
    SE --> F
    SE --> E
    F --> G
    G -->|Goal found| P
    E --> P
    P --> SE
~~~

## Short Explanation

The Search Engine controls the actual maze search. The frontier stores nodes that still need to be explored, while the explored set prevents unnecessary repeated visits. The goal test identifies the destination. When the goal is found, the path reconstructor uses parent/path information to generate the final route.
