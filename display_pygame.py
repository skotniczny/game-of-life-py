from engine import GameOfLife
from decoder import parse
from typing import Tuple
import patterns
import math
import pygame


def run(board: GameOfLife, box_size):
    # Initialize Pygame.
    pygame.init()
    # Set size of pygame window.
    screen = pygame.display.set_mode((board.width * box_size, board.height * box_size))
    # Create empty pygame surface.
    background = pygame.Surface(screen.get_size())
    # Fill the background white color.
    background.fill("#ffffff")
    # Create Pygame clock object.
    clock = pygame.time.Clock()

    mainloop = True
    is_stopped = False
    # Desired framerate in frames per second. Try out other values.
    fps = 30
    # How many seconds the "game" is played.
    playtime = 0.0
    board.generate()

    def update_board():
        nonlocal background
        nonlocal board
        nonlocal box_size
        nonlocal screen
        background.fill("#ffffff")
        for i in range(board.size):
            if board.grid[i]:
                col = i % board.width
                row = int((i - col) / board.width)
                color = "#3f51b5"
                left = col * box_size + 1
                top = row * box_size + 1
                size = box_size - 1
                background.fill(color, [left, top, size, size])
        # Update Pygame display.
        # Convert Surface object to make blitting faster.
        background = background.convert()
        # Copy background to screen (position (0, 0) is upper left corner).
        screen.blit(background, (0, 0))

    def insert_pattern(pattern, offset: Tuple[int, int] = (0, 0)):
        nonlocal board
        board.clear()
        board.insert(parse(pattern), offset)
        update_board()

    while mainloop:
        # Do not go faster than this framerate.
        milliseconds = clock.tick(fps)
        playtime += milliseconds / 1000.0

        for event in pygame.event.get():
            # User presses QUIT-button.
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                # User presses SPACE-Key
                if event.key == pygame.K_SPACE:
                    is_stopped = not is_stopped
                # User presses RETURN-Key (ENTER)
                if event.key == pygame.K_RETURN:
                    board.next_generation()
                    update_board()
                if event.key == pygame.K_n:
                    board.generate()
                    update_board()
                if event.key == pygame.K_1:
                    insert_pattern(patterns.gosper_glider_gun)
                if event.key == pygame.K_2:
                    insert_pattern(patterns.new_gun)
                if event.key == pygame.K_3:
                    insert_pattern(patterns.new_gun_2)
                if event.key == pygame.K_4:
                    insert_pattern(patterns.p20_glider_gun)
                if event.key == pygame.K_5:
                    insert_pattern(patterns.period_60_glider_gun)
                if event.key == pygame.K_6:
                    insert_pattern(patterns.b52_bomber, (5, 15))
                if event.key == pygame.K_7:
                    insert_pattern(patterns.quasar3, (10, 5))
                # User presses ESCAPE-Key
                if event.key == pygame.K_ESCAPE:
                    mainloop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    (x, y) = pygame.mouse.get_pos()
                    cell_x = math.floor(x / box_size)
                    cell_y = math.floor(y / box_size)
                    cell_index = cell_x + cell_y * board.width
                    board.toggle_cell(cell_index)
                    update_board()

        # Print keys description, framerate and playtime in titlebar.
        text = "Press SPACE to stop  |  Press ENTER to make next generation  | Press N to generate new | " \
               "CLICK to edit board  | " f"FPS: {format(clock.get_fps(), '.2f')}  Playtime: {format(playtime, '.2f')}"
        pygame.display.set_caption(text)
        if not is_stopped:
            board.next_generation()
            update_board()

        pygame.display.flip()

    # Finish Pygame.
    pygame.quit()

    # At the very last:
    print(f"This game was played for {format(playtime, '.2f')} seconds")
