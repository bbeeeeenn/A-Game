import pygame, time, sys

from player import Player


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Space Impact")

        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock, self.FPS = pygame.time.Clock(), 60
        self.delta_time, self.prev_time = 0, 0

        self.running = True
        self.player: Player = Player(self)

    def game_loop(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.get_dt()
            self.handle_events()
            self.update()
            self.render()

    def get_dt(self):
        current_time = time.time()
        self.delta_time = current_time - self.prev_time
        self.prev_time = current_time

    def handle_events(self):
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
                self.running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    self.player.shoot()

    def update(self):
        self.player.update()

    def render(self):
        self.screen.fill((255, 255, 255))
        self.player.render()
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.game_loop()
