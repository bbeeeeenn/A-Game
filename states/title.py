import pygame
from states.state import State
from states.play import Play


class Title(State):
    def __init__(self, game):
        super().__init__(game)
        self.title = self.game.write_text(
            "Stellar Impact",
            42,
            (self.game.WIDTH // 2, self.game.HEIGHT // 2),
            (255, 255, 255),
        )
        self.bottom_text = self.game.write_text(
            "- press [ENTER] to play -", 10, (0, 0), (255, 255, 255)
        )
        self.bottom_text[1].midtop = self.title[1].midbottom

    def update(self, delta_time, actions):
        if actions["enter"]:
            # Insert new state
            play_state = Play(self.game)
            play_state.enter_state()
        self.game.reset_keys()

    def render(self, display: pygame.Surface):
        # Render Title screen
        display.fill((0, 0, 0))
        display.blit(self.title[0], self.title[1])
        display.blit(self.bottom_text[0], self.bottom_text[1])
