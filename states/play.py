import pygame
from state import State


class Play(State):
    def __init__(self, game):
        super().__init__(game)
