import pygame
from states.state import State
from classes.ship import Ship


class Play(State):
    def __init__(self, game):
        super().__init__(game)

        self.ship = Ship(self.game)

    def update(self, dt, actions):
        if self.game.actions["back"]:
            self.exit_state()
            self.game.reset_keys()
        self.ship.update(dt)

    def render(self, display: pygame.Surface):
        display.fill((255, 255, 255))
        self.ship.render(display)
