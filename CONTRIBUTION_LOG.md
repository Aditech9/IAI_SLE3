# Contribution Log — SLE-3

**Project:** Graph Search Profiling Engine (BFS vs DFS)  
**Student:** Aditya Sanjay Patil  
**PRN:** 25UAM026  
**Course:** 02AML204 — Introduction to Artificial Intelligence

## Work completed

| Area | Contribution |
|---|---|
| Graph generation | Added a deterministic adjacency-list graph generator with sequential edges and forward shortcuts. |
| BFS | Implemented iterative Breadth-First Search using a FIFO queue, visited set, and parent mapping for path reconstruction. |
| DFS | Implemented iterative Depth-First Search using a LIFO stack and visited-node tracking. |
| Profiling | Added a command-line runner using timeit.repeat to report best, worst, and average runtime, path length, and expanded-node count. |
| Testing | Added unit tests for graph creation, traversal, unreachable goals, invalid nodes, and timing output. |
| Documentation | Added setup/run instructions and a project architecture overview to the README. |

## AI contribution note

AI tools (ChatGPT/Gemini) may assist with structuring BFS/DFS profiling methods, timing routines, node-expansion counting, tests, and C4 documentation. The student should personally run the code, inspect the generated graph, verify the results, understand traversal mechanics, and record actual benchmark observations before submission.

## Verification checklist

- [ ] Run python profile.py and inspect both algorithms' metrics.
- [ ] Run python -m unittest discover -s tests -v.
- [ ] Confirm the start and goal nodes are valid for the selected graph size.
- [ ] Record actual benchmark results in the report; results can vary by machine and run.
- [ ] Review the code and be prepared to explain queue versus stack behavior.
