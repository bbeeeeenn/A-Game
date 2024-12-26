import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game


class Ship:
    def __init__(self, game) -> None:
        self.game: Game = game
        self.surf = pygame.image.load("assets/sprites/ship.png").convert_alpha()
        self.rect = self.surf.get_rect(
            midbottom=(self.game.WIDTH / 2, self.game.HEIGHT - 10)
        )
        self.speed = 400

    def update(self, dt):
        x_movement = (
            (self.game.actions["right"] - self.game.actions["left"]) * self.speed * dt
        )
        self.rect.move_ip(x_movement, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.game.WIDTH:
            self.rect.right = self.game.WIDTH

    def render(self, display: pygame.Surface):
        display.blit(self.surf, self.rect)
