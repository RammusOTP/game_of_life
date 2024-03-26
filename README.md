# Game of Life
v1.0.0
## Introduction
Conway's Game of Life is a simulation of a grid, in which each cell in said grid is either alive or dead.
The game runs in generations, and the rules for whether a cell lives, dies, or stays the same in the next generation is dependent on neighbouring cells.
## Rules
### Overpopulation:
If an alive cell has more than 3 adjacent alive cells, the cell will die due to overcrowding.
### Underpopulation:
If an alive cell has less than 2 adjacent alive cells, the cell will die due to loneliness.
### Survival:
If an alive cell has either 2 or 3 adjacent alive cells, the cell survives to the next generation.
### Reproduction:
If an empty cell has exactly 3 alive adjacent cells, it will come to life in the next generation.
## Components to the Game
### Grid:
The grid is the playing field for the game. It consists of rows and columns, where each cell can be either alive or dead.
### Cells:
Cells are the individual units in the grid. Each cell can be alive or dead.
### Generations:
The game progresses in discrete steps called generations. Between generations is when the status of the cells may (or may not) change.
### UI:
Users may interact with the grid cells to "set up" the game: configuring the starting status of the cells. Users can also pause and resume the simulation and modify any cell at any time they please.
