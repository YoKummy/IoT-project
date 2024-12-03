# app.py
from flask import Flask, jsonify
from game_state import GameState
import threading

app = Flask(__name__)
game_state = GameState()

@app.route('/')
def index():
    stats = game_state.get_stats()
    return (
        f"<h1>Math Game Stats</h1>"
        f"<p>Score: {stats['score']}</p>"
        f"<p>Attempts: {stats['attempts']}</p>"
        f"<p>Correct: {stats['correct']}</p>"
        f"<p>Accuracy: {stats['accuracy']}%</p>"
    )

@app.route('/api/stats')
def api_stats():
    stats = game_state.get_stats()
    return jsonify(stats)

def run_flask():
    app.run(host='0.0.0.0', port=5000)
