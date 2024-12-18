from game import Game

if __name__ == "__main__":
    configs = {
        "WIDTH": 800,
        "HEIGHT": 600,
        "FPS": 60,
    }
    game: Game = Game(configs)
    if game.running:
        game.game_loop()
