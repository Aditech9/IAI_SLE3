# C4 Level 1 – Context Diagram

## System
**Maze Solving System using BFS / DFS**

## Purpose

The Context level shows the complete system as one main box and the outside user interacting with it. The guideline requires the system, user/operator, optional external systems, and interaction arrows. fileciteturn0file0L47-L54

## Context Diagram

~~~mermaid
flowchart LR
    U[User / Operator]
    S[Maze Solving System]
    R[Path / Search Result]
    U -->|Enter maze, start and goal| S
    S -->|Display solved path / result| R
    R --> U
~~~

## Interaction

1. The user provides the maze and start/goal information.
2. The Maze Solving System processes the search problem.
3. The system returns the path or search result to the user.

## Short Explanation

The Maze Solving System is the central system. The user supplies a maze and required input. The system performs the selected search algorithm and provides the resulting path or failure result to the user.
