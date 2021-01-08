from engine import GameOfLife
import pygame


def run(board: GameOfLife, box_size):
    # Initialize Pygame.
    pygame.init()
    # Set size of pygame window.
    screen = pygame.display.set_mode((board.width * box_size, board.height * box_size))
    # Create empty pygame surface.
    background = pygame.Surface(screen.get_size())
    # Fill the background white color.
    background.fill((255, 255, 255))
    pygame.draw.rect(background, "#ff0000", [50, 50, 50, 50])
    # # Convert Surface object to make blitting faster.
    # background = background.convert()
    # # Copy background to screen (position (0, 0) is upper left corner).
    # screen.blit(background, (0, 0))
    # Create Pygame clock object.
    clock = pygame.time.Clock()

    pygame.draw.rect(background, "#ff0000", [50, 50, 50, 50])

    mainloop = True
    # Desired framerate in frames per second. Try out other values.
    FPS = 30
    # How many seconds the "game" is played.
    playtime = 0.0
    board.generate()
    while mainloop:
        # Do not go faster than this framerate.
        milliseconds = clock.tick(FPS)
        playtime += milliseconds / 1000.0

        for event in pygame.event.get():
            # User presses QUIT-button.
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                # User presses ESCAPE-Key
                if event.key == pygame.K_ESCAPE:
                    mainloop = False

        # Print framerate and playtime in titlebar.
        text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
        pygame.display.set_caption(text)
        board.next_generation()
        background.fill("#ffffff")
        for i in range(board.size):
            if board.grid[i]:
                col = i % board.width
                row = int((i - col) / board.width)
                color = "#3f51b5" if board.grid[i] else "#ffffff"
                left = col * box_size
                top = row * box_size
                background.fill(color, [left, top, box_size, box_size])
        # Update Pygame display.
        # Convert Surface object to make blitting faster.
        background = background.convert()
        # Copy background to screen (position (0, 0) is upper left corner).
        screen.blit(background, (0, 0))
        pygame.display.flip()

    # Finish Pygame.
    pygame.quit()

    # At the very last:
    print("This game was played for {0:.2f} seconds".format(playtime))

