# C4 Level 4 – Code Level Overview

## Main Classes / Functions

The guideline asks for names of the main classes/functions and short responsibilities, not a large source-code listing. fileciteturn0file0L72-L80

| Code Element | Responsibility |
|---|---|
| class Node | Represents a maze/search state or position |
| class Maze | Stores the maze and validates positions |
| def bfs() | Performs Breadth-First Search |
| def dfs() | Performs Depth-First Search |
| def get_neighbors() | Finds valid neighbouring positions |
| def goal_test() | Checks whether the goal is reached |
| def reconstruct_path() | Builds the final path |
| def display_result() | Shows the path or failure message |

## Small Code-Level Relationship

~~~mermaid
classDiagram
    class Node
    class Maze
    class SearchEngine {
        +bfs()
        +dfs()
        +get_neighbors()
        +goal_test()
        +reconstruct_path()
    }
    class Output {
        +display_result()
    }
    Maze --> Node
    SearchEngine --> Maze
    SearchEngine --> Node
    SearchEngine --> Output
~~~

## Code-Level Summary

The code level identifies the main program elements without reproducing the full implementation. BFS and DFS are alternative search functions. The supporting functions manage neighbours, goal checking, path reconstruction and result display.
