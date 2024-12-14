import pygame, time


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


class Player:
    def __init__(self, game: Game) -> None:
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
        if self.you_rect.right > self.game.WIDTH:
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


if __name__ == "__main__":
    game = Game()
    game.game_loop()
