import random


class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = width * height
        self.grid = []

    def generate(self, density=0.25):
        self.grid = [random.random() < density for _ in range(self.size)]

    def clear(self):
        return [False for _ in self.grid]

    def next_generation(self):
        def next_state(cell_idx):
            directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
            x = cell_idx % self.width
            y = int((cell_idx - x) / self.width)
            neighbours = 0
            for i in range(8):
                direction = directions[i]
                direction_x = x + direction[0]
                direction_y = y + direction[1]
                if 0 <= direction_x < self.width and 0 <= direction_y < self.height:
                    idx = direction_x + (direction_y * self.width)
                    neighbours += 1 if self.grid[idx] is True else 0
            if neighbours < 2 or neighbours > 3:
                return False
            if neighbours == 2:
                return self.grid[cell_idx]
            return True

        self.grid = [next_state(i) for i in range(self.size)]

    def toggle_cell(self, index):
        self.grid[index] = (not self.grid[index])
