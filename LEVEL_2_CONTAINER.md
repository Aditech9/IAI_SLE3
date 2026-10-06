# C4 Level 2 – Container Diagram

## Main Containers

The guideline recommends 4–7 boxes for a Maze/Search system. fileciteturn0file0L55-L63

| Container | Responsibility |
|---|---|
| Input Module | Accepts and validates the maze, start and goal |
| Search Engine | Runs BFS or DFS to explore the maze |
| Visited Set / Memory | Stores visited nodes to avoid repeated exploration |
| Goal Test | Checks whether the current node is the destination |
| Path Reconstructor | Builds the final path after reaching the goal |
| Output Module | Displays the path, status and result |

## Container Diagram

~~~mermaid
flowchart LR
    U[User]
    I[Input Module]
    S[Search Engine]
    V[Visited Set / Memory]
    G[Goal Test]
    P[Path Reconstructor]
    O[Output Module]
    U -->|Maze + start + goal| I
    I --> S
    S <--> V
    S --> G
    G -->|Goal reached| P
    P --> O
    G -->|Not reached| S
    O --> U
~~~

## Container Explanation

- **Input Module:** Receives the maze and validates the basic input.
- **Search Engine:** Performs BFS or DFS and controls the search process.
- **Visited Set / Memory:** Prevents repeated processing of already explored nodes.
- **Goal Test:** Determines whether the current node is the required destination.
- **Path Reconstructor:** Uses stored parent/path information to construct the final route.
- **Output Module:** Presents the final path or indicates that no path was found.
