from engine import GameOfLife
import display_tkinter
import display_cmd
import display_pygame

WIDTH = 100
HEIGHT = 60
DELAY = 0
BLOCK_SIZE = 10


def main():
    board = GameOfLife(WIDTH, HEIGHT)
    # display_tkinter.run(board, BLOCK_SIZE, DELAY)
    # display_cmd.run(board, DELAY)
    display_pygame.run(board, BLOCK_SIZE)
    print("Game Over")


if __name__ == '__main__':
    main()
