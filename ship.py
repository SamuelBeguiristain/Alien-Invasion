import pygame

from settings import Settings

class Ship:
    # I was going to make the ship originally the poop emoji
    """A class to image the \"SHIP\""""

    def __init__(self, ai_game):
        """Initalize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.transform.scale((pygame.image.load('images/ship.png')), (50, 65))
        #self.image = pygame.image.load('images/poop.bmp') # Attempting to resize some how
        self.rect = self.image.get_rect()                 # using pygame.transform.scale()


        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
