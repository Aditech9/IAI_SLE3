# SLE-3: Architectural Design using Full C4 Model

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Program:** SY B.Tech. CSE (AI & ML)  
**Student:** Aditya Sanjay Patil  
**Repository:** IAI_SLE3

## 1. System Title
### Maze Solving System using BFS / DFS

This SLE-3 work presents the architecture of a Maze Solving System using the complete C4 Model. The system accepts a maze and a start/goal position, applies a search algorithm such as BFS or DFS, and produces a path/result. The architecture is documented at Context, Container, Component, and Code levels.

The SLE-3 guideline requires all four C4 levels, a short system explanation, design decisions, and an honest AI contribution note. fileciteturn0file0L16-L28

## 2. Repository Structure

| File | Purpose |
|---|---|
| LEVEL_1_CONTEXT.md | C4 Level 1 – Context Diagram |
| LEVEL_2_CONTAINER.md | C4 Level 2 – Container Diagram |
| LEVEL_3_COMPONENT.md | C4 Level 3 – Component Diagram |
| LEVEL_4_CODE.md | C4 Level 4 – Code Level Overview |
| CONTRIBUTION_LOG.md | Work and AI contribution record |
| README.md | Project overview and submission guidance |

## 3. C4 Levels

1. Context – Shows the Maze Solving System and its interaction with the user.
2. Container – Shows the major internal building blocks.
3. Component – Shows important internal parts of the Search Engine.
4. Code – Lists the main classes/functions and responsibilities.

The guideline specifically recommends 4–7 containers and only one main container expanded at Component level. fileciteturn0file0L55-L80

## 4. Suggested Design

User → Input Module → Search Engine → Output Module

For BFS/DFS, the Search Engine maintains the frontier and an explored/visited set, checks the goal condition, and reconstructs the final path.

## 5. Design Decisions

- Continue with a search/maze system because it is connected to the previous SLE work.
- Keep the architecture small and readable.
- Use the Search Engine as the single container expanded at Component level.
- Keep the Code level limited to main names and responsibilities instead of large source code.

## 6. AI Contribution Note

AI assistance may be used for organizing the architecture, improving explanations, and checking the C4 structure. The student should verify every diagram and explanation and should be able to explain the design independently.

## 7. Submission Checklist

- [x] Level 1 Context
- [x] Level 2 Container
- [x] Level 3 Component
- [x] Level 4 Code
- [x] Design decisions
- [x] AI contribution note
- [x] Contribution log
- [ ] Add PRN, division, and submission date
- [ ] Export/insert diagrams into the final 2–3 page Word/PDF submission

The official guideline specifies a maximum of four pages and asks for clear, short diagrams and explanations. fileciteturn0file0L87-L129
