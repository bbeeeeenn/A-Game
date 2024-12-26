import pygame
from states.state import State
from states.play import Play


class Title(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self, delta_time, actions):
        if actions["enter"]:
            # Insert new state
            play_state = Play(self.game)
            play_state.enter_state()
        self.game.reset_keys()

    def render(self, display: pygame.Surface):
        # Render Title screen
        display.fill((100, 0, 0))
