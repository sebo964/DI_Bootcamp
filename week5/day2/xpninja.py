# Instructions

# These are the rules of the Game of Life (as stated in Wikipedia):

# The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively).

# Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
# Using these rules, implement the Game. (Hint: use Classes !!!!)
# Use a few different initial states to see how the game ends.

# Notes:

# Display the grid after each generation
# The end of the game is fully determined by the initial state. So have it pass through your program and see how it ends.
# Be creative, but use classes
# The game can have fixed borders and can also have moving borders. First implement the fixed borders. Each “live” cell that is going out of the border, exits the game.
# Bonus: Make the game with ever expandable borders, make the maximum border size a very large number(10,000) so you won’t cause a memory overflow
import numpy as np


class GameOfLife:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.next_grid = np.zeros((size, size), dtype=int)

    def randomize(self, p=0.5):
        self.grid = np.random.choice([0, 1], size=(self.size, self.size), p=[1 - p, p])

    def step(self):
        for i in range(self.size):
            for j in range(self.size):
                num_neighbors = self.count_neighbors(i, j)
                if self.grid[i, j] == 1:
                    if num_neighbors < 2 or num_neighbors > 3:
                        self.next_grid[i, j] = 0
                    else:
                        self.next_grid[i, j] = 1
                else:
                    if num_neighbors == 3:
                        self.next_grid[i, j] = 1
        self.grid = self.next_grid.copy()
        self.next_grid = np.zeros((self.size, self.size), dtype=int)

    def count_neighbors(self, i, j):
        count = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                ni = i + di
                nj = j + dj
                if ni < 0 or nj < 0 or ni >= self.size or nj >= self.size:
                    continue
                if self.grid[ni, nj] == 1:
                    count += 1
        return count

    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                print("*" if self.grid[i, j] == 1 else ".", end="")
            print()


# example usage
game = GameOfLife(10)
game.randomize(0.3)
for i in range(10):
    print("Generation:", i)
    game.display()
    game.step()
