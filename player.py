from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from game import Game


class Player:
    def __init__(self, game) -> None:
        position_offset = 10
        self.game: Game = game
        self.image = pygame.image.load("assets/sprites/player.png").convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=(self.game.WIDTH / 2, self.game.HEIGHT - position_offset)
        )
        self.you = [
            pygame.image.load("assets/sprites/You.png").convert_alpha(),
            pygame.image.load("assets/sprites/You-rev.png").convert_alpha(),
        ]
        self.you_index = 0
        self.you_rect = self.you[0].get_rect()

        self.beams: list[Beam] = []

    def update(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_a]:
            self.move_left()

        if keypressed[pygame.K_d]:
            self.move_right()

        self.you_rect.midleft = self.rect.right, self.rect.centery
        if self.rect.centerx > self.game.WIDTH / 2:
            self.you_rect.midright = self.rect.left, self.rect.centery
            self.you_index = 1
        else:
            self.you_index = 0

        self.beams = [beam for beam in self.beams if beam.rect.y > -beam.rect.height]
        for beam in self.beams:
            beam.update()

    def render(self):
        for beam in self.beams:
            beam.render()
        self.game.screen.blit(self.image, self.rect)
        self.game.screen.blit(self.you[self.you_index], self.you_rect)

    def move_left(self):
        self.rect.move_ip(-400 * self.game.delta_time, 0)
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.move_ip(400 * self.game.delta_time, 0)
        if self.rect.right > self.game.WIDTH:
            self.rect.right = self.game.WIDTH

    def shoot(self) -> None:
        beam: Beam = Beam(self)
        self.beams.append(beam)


class Beam:
    def __init__(self, player: Player) -> None:
        self.game: Game = player.game
        self.player: Player = player
        self.image = pygame.image.load("assets/sprites/Beam-1.png").convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=(self.player.rect.centerx, self.player.rect.centery)
        )

    def update(self):
        self.rect.move_ip(0, -500 * self.game.delta_time)

    def render(self):
        self.game.screen.blit(self.image, self.rect)
