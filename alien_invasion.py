import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Overall class that manages game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        #initialize the background settings for Pygame
        pygame.init() 

        self.settings = Settings()

        #object asigned to self.screen is called a surface -main game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")

        
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Continually checking if keyboard or mouse input events are given
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            #Make the most recently drawn screen visible
            #Deletes the old screen instance and display the updated one
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
