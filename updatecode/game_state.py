from game import Game

class GameState:
    def __init__(self):
        self.game = Game()

    def get_stats(self):
        return self.game.get_stats()

    def set_difficulty(self, difficulty):
        self.game.difficulty = difficulty
