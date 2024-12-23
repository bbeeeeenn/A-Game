import pygame, time, sys


class Game:
    def __init__(self, configs) -> None:
        pygame.init()
        self.WIDTH = configs["WIDTH"]
        self.HEIGHT = configs["HEIGHT"]
        self.FPS = configs["FPS"]

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.prev_time = 0

        self.running = True
        self.actions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False,
            "enter": False,
            "back": False,
            "shoot": False,
        }

        self.state_stack: list = []
        self.load_states()

    def game_loop(self) -> None:
        self.clock.tick(self.FPS)
        self.get_dt()
        self.handle_events()
        self.update()
        self.render()

    def get_dt(self):
        now = time.time()
        self.delta_time = now - self.prev_time
        self.prev_time = now

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.actions["left"] = True
                if event.key == pygame.K_d:
                    self.actions["right"] = True
                if event.key == pygame.K_w:
                    self.actions["up"] = True
                if event.key == pygame.K_s:
                    self.actions["down"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.actions["left"] = False
                if event.key == pygame.K_d:
                    self.actions["right"] = False
                if event.key == pygame.K_w:
                    self.actions["up"] = False
                if event.key == pygame.K_s:
                    self.actions["down"] = False

    def update(self):
        pass

    def render(self):
        pass

    def load_states(self):
        pass

    def quit_game(self):
        self.running = False
        pygame.quit()
        sys.exit()
