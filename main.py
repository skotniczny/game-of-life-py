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


def main():
    board = GameOfLife(100, 25)
    os.system('cls')
    board.generate()
    display(board)
    time.sleep(0.5)
    is_running = True
    iterations = 0
    while is_running:
        os.system('cls')
        board.next_generation()
        display(board)
        time.sleep(0.5)
        iterations += 1
        if iterations is 100:
            is_running = False
    print("Game Over")


if __name__ == '__main__':
    main()
