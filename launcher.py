import pygame
from src.constants import SCREEN_W, SCREEN_H, FPS # source constant location
from pygame.locals import QUIT
from src.game import Game

def main():
    
    pygame.init()

    # Create the window for the game
    display = pygame.display.set_mode((SCREEN_W, SCREEN_H), 0, 32) #dimensions
    font = pygame.font.SysFont("Arial", 24)

    running = True
    game = Game()
    game_clock = pygame.time.Clock()
    while running:

        # Behaviour needed
        delta = game_clock.tick(FPS)
        events = pygame.event.get() # Return all the events occured since last check --> get a list of events
        game.handle_input(events)  # process input
        game.update(delta) # Update game world
        game.render(display, font) # render game world
        pygame.display.update()

        # Quit game
        for e in events:
            if e.type == QUIT:
                running = False


if __name__ == "__main__":
    main()