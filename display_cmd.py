import os
import time
from engine import GameOfLife


def display(board: GameOfLife):
    output = ""
    for (cell_idx, cell) in enumerate(board.grid):
        if cell_idx % board.width == 0:
            output += "\n"
        output += ("*" if cell is True else " ")
    print(output)


def run(board: GameOfLife, delay):
    os.system('cls')
    board.generate()
    display(board)
    time.sleep(delay)
    is_running = True
    iterations = 0
    while is_running:
        os.system('cls')
        board.next_generation()
        display(board)
        time.sleep(delay)
        iterations += 1
        if iterations == 200:
            is_running = False