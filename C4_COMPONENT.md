# C4 Level 3 – Component Diagram

Only the **Search Engine** container is expanded.

| Component | Responsibility |
|---|---|
| Frontier | Holds nodes waiting for processing |
| Explored / Closed Set | Records nodes already processed |
| Goal Test | Checks whether the current node is the target |
| Path Reconstructor | Rebuilds the discovered path from parent links |

### Component Flow

Frontier → Goal Test → Explored / Closed Set → Path Reconstructor

The exact internal order can vary slightly between BFS and DFS, but these components describe the main responsibilities of the Search Engine.

See `diagrams/c4_component.svg`.
