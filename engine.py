import random
from typing import Tuple


class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = width * height
        self.grid = []
        self._adjacency = []

    def generate(self):
        # Make grid as one-dimensional array of Boolean
        self.make_grid()

        # Make array of neighbours of each cell
        def make_adjacency(cell_idx):
            adjacent = []
            directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
            x = cell_idx % self.width
            y = int((cell_idx - x) / self.width)
            for i in range(8):
                direction = directions[i]
                direction_x = x + direction[0]
                direction_y = y + direction[1]
                if 0 <= direction_x < self.width and 0 <= direction_y < self.height:
                    idx = direction_x + (direction_y * self.width)
                    adjacent.append(idx)
            return adjacent
        self._adjacency = [make_adjacency(i) for i in range(self.size)]

    def make_grid(self, density=0.25):
        # Make grid as one-dimensional array of Boolean
        self.grid = [random.random() < density for _ in range(self.size)]

    def clear(self):
        self.grid = [False for item in self.grid]

    def next_generation(self):
        def next_state(cell_idx):
            neighbours_state = [self.grid[idx] for idx in self._adjacency[cell_idx]]
            neighbours = sum(neighbours_state)
            if neighbours < 2 or neighbours > 3:
                return False
            if neighbours == 2:
                return self.grid[cell_idx]
            return True

        self.grid = [next_state(i) for i in range(self.size)]

    def toggle_cell(self, index):
        self.grid[index] = (not self.grid[index])

    def insert(self, pattern, offset: Tuple[int, int] = (0, 0)):
        for y in range(len(pattern)):
            for x in pattern[y]:
                idx = (x + offset[0]) + ((y + offset[1]) * self.width)
                self.grid[idx] = True
