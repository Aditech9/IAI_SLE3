# SLE-3: Architectural Design using Full C4 Model

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Student:** Aditya Patil  
**Repository:** Aditech9/IAI_SLE3  
**System:** Graph Search System (BFS / DFS)

## Overview

SLE-3 presents the architecture of a Graph Search System using all four C4 levels: Context, Container, Component, and Code.

## Repository Contents

- `README.md` – project overview
- `CONTRIBUTION_LOG.md` – contribution and AI-use record
- `ARCHITECTURE.md` – combined C4 architecture
- `C4_CONTEXT.md` – Level 1
- `C4_CONTAINER.md` – Level 2
- `C4_COMPONENT.md` – Level 3
- `C4_CODE.md` – Level 4
- `DESIGN_DECISIONS.md` – architecture decisions
- `AI_CONTRIBUTION.md` – AI contribution note
- `graph_search.py` – BFS/DFS reference implementation
- `diagrams/c4_context.svg` – Context diagram
- `diagrams/c4_container.svg` – Container diagram
- `diagrams/c4_component.svg` – Component diagram

## System Description

The Graph Search System takes a graph, a starting node, a goal node, and a search method from the user. The Search Engine performs BFS or DFS. A visited set prevents repeated processing, and the Output Module shows the result.

## Run

Requires Python 3.

```bash
python graph_search.py
```

## C4 Summary

**Level 1 – Context:** User interacts with the Graph Search System and receives a result.  
**Level 2 – Container:** Input Module, Search Engine, Memory/Visited Set, and Output Module.  
**Level 3 – Component:** Frontier, Explored Set, Goal Test, and Path Reconstructor inside Search Engine.  
**Level 4 – Code:** Main classes/functions such as `Graph`, `bfs()`, `dfs()`, and `reconstruct_path()`.

## Learning Outcome

The project shows how one search system can be explained from the big-picture context down to its main code elements using a simple C4 architecture.
