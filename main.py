from engine import GameOfLife
import display_tkinter
import display_cmd

WIDTH = 50
HEIGHT = 20
DELAY = 0
BLOCK_SIZE = 25

def main():
    board = GameOfLife(WIDTH, HEIGHT)
    display_tkinter.run(board, BLOCK_SIZE, DELAY)
    # display_cmd.run(board, DELAY)
    print("Game Over")

if __name__ == '__main__':
    main()
