# game_state.py
from threading import Lock

class GameState:
    def __init__(self):
        self.score = 6
        self.attempts = 0
        self.correct = 0
        self.lock = Lock()

    def update_score(self, delta):
        with self.lock:
            self.score += delta

    def increment_attempts(self):
        with self.lock:
            self.attempts += 1

    def increment_correct(self):
        with self.lock:
            self.correct += 1

    def get_stats(self):
        with self.lock:
            accuracy = (self.correct / self.attempts * 100) if self.attempts > 0 else 0
            return {
                "score": self.score,
                "attempts": self.attempts,
                "correct": self.correct,
                "accuracy": round(accuracy, 2),
            }
