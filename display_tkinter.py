import time
from engine import GameOfLife
from tkinter import *


def make_board(ctx, board: GameOfLife, box_size = 10):
    cells = []
    for i in range(board.size):
        col = i % board.width
        row = int((i - col) / board.width)
        color = "#3f51b5" if board.grid[i] else "#ffffff"
        cell = ctx.create_rectangle(col * box_size, row * box_size, (col + 1) * box_size, row * box_size + box_size, fill=color, outline="#dddddd")
        cells.append(cell)
    return cells


def display_canvas(ctx, cells, board: GameOfLife):
    for i, value in enumerate(cells):
        color = "#3f51b5" if board.grid[i] else "#ffffff"
        ctx.itemconfig(value, fill = color)
    ctx.update()


def run(board: GameOfLife, box_size, delay):
    master = Tk()
    master.title("Game Of Life")
    ctx = Canvas(master, width=board.width * box_size, height=board.height * box_size)
    ctx.pack()
    board.generate()
    cells = make_board(ctx, board, box_size)
    display_canvas(ctx, cells, board)
    time.sleep(delay)
    is_running = True
    iterations = 0

    def next_frame():
        nonlocal is_running
        if not is_running:
            return
        board.next_generation()
        display_canvas(ctx, cells, board)
        nonlocal iterations
        iterations += 1
        ctx.after(delay, next_frame)
        if iterations == 500:
            is_running = False
            print(iterations)
    next_frame()
    master.mainloop()
