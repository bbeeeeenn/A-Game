import pygame
from state import State


class Title(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self, delta_time, actions):
        print(self.game.state_stack, self.prev_state)
        if actions["enter"]:
            # Insert new state
            pass
        self.game.reset_keys()

    def render(self, display: pygame.Surface):
        # Render Title screen
        display.fill((100, 0, 0))
