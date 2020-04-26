import pygame

from settings import Settings

class Ship:
    # I was going to make the ship originally the poop emoji
    """A class to image the \"SHIP\""""

    def __init__(self, ai_game):
        """Initalize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.transform.scale((pygame.image.load('images/poop.bmp').convert_alpha()), (1500, 1500))
        #self.image = pygame.image.load('images/poop.bmp') # Attempting to resize some how
        self.rect = self.image.get_rect()                 # using pygame.transform.scale()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
