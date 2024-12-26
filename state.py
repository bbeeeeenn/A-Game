import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game


class State:
    def __init__(self, game) -> None:
        self.game: Game = game
        self.prev_state = None

    def update(self):
        pass

    def render(self, display: pygame.Surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()
