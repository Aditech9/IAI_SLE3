# Design Decisions

## Decision 1 – Select Graph Search System

**Decision:** Use the Graph Search System with BFS and DFS.

**Reason:** It is simple, directly connected to search-system work, and easy to represent at all four C4 levels.

## Decision 2 – Keep 4 Containers

**Decision:** Use Input Module, Search Engine, Memory / Visited Set, and Output Module.

**Reason:** The guideline recommends a readable architecture with a limited number of containers.

## Decision 3 – Expand Only Search Engine at Component Level

**Decision:** Create components only for the Search Engine.

**Reason:** The Search Engine contains the central search logic, so expanding it gives the most useful architectural detail without making the diagram crowded.

## Decision 4 – Keep Code Level Short

**Decision:** List names and responsibilities instead of source code.

**Reason:** The SLE-3 requirement asks for a code-level overview, not a large code listing.
