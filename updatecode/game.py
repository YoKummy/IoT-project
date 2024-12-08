import random
import RPi.GPIO as GPIO
import drivers
from time import sleep

# Numpad setup
NUMPAD_PIN_MAPPING = {
    1: [17, 27],  # example GPIO pins for numpad button 1
    2: [22, 5],   # example GPIO pins for numpad button 2
    # add the rest of the numpad pins
}

class Game:
    def __init__(self):
        # LCD Initialization
        self.display = drivers.Lcd()
        # Servo Initialization
        self.servo_pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.servo_pin, 50)  # 50 Hz PWM
        self.servo.start(0)

        self.difficulty = "easy"
        self.score = 6
        self.attempts = 0
        self.correct_attempts = 0

    def generate_problem(self):
        if self.difficulty == "easy":
            num1, num2 = random.randint(1, 10), random.randint(1, 10)
            operation = random.choice(["+", "-"])
        elif self.difficulty == "medium":
            num1, num2 = random.randint(10, 50), random.randint(10, 50)
            operation = random.choice(["+", "-", "*"])
        else:  # Hard
            num1, num2 = random.randint(50, 100), random.randint(50, 100)
            operation = random.choice(["+", "-", "*", "/"])
        
        problem = f"{num1} {operation} {num2}"
        answer = eval(problem)
        return problem, round(answer, 2) if isinstance(answer, float) else answer

    def update_score(self, points):
        self.score += points
        if self.score <= 0:
            self.set_servo_angle(90)  # Servo for Game Over
            self.display_message("Game Over!", "Score: 0")
            sleep(3)
            raise SystemExit("Game Over! You lost.")
        elif self.score >= 12:
            self.set_servo_angle(180)  # Servo for Game Win
            self.display_message("You Win!", "Score: 12")
            sleep(3)
            raise SystemExit("You Win! Congratulations.")

    def record_attempt(self, is_correct):
        self.attempts += 1
        if is_correct:
            self.correct_attempts += 1

    def get_stats(self):
        accuracy = (self.correct_attempts / self.attempts) * 100 if self.attempts > 0 else 0
        return {
            "score": self.score,
            "attempts": self.attempts,
            "correct": self.correct_attempts,
            "accuracy": round(accuracy, 2),
        }

    def set_servo_angle(self, angle):
        """Set the servo motor to a specific angle (0-180 degrees)."""
        duty_cycle = 2 + (angle / 18)  # Map angle to duty cycle
        self.servo.ChangeDutyCycle(duty_cycle)
        sleep(0.5)
        self.servo.ChangeDutyCycle(0)  # Stop sending signal to prevent jitter

    def display_message(self, line1, line2):
        """Update the LCD display."""
        self.display.lcd_clear()
        self.display.lcd_display_string(line1, 1)
        self.display.lcd_display_string(line2, 2)

    def read_numpad_input(self):
        """Simulate reading input from the numpad."""
        # Implement the GPIO logic to read input from your numpad here
        pass  # You would return the numpad input, e.g., '5'

# Function to run the game
def run_game():
    game = Game()
    while True:
        problem, answer = game.generate_problem()  # Get a new problem
        game.display_message(problem, str(game.score))  # Display the problem

        user_input = None
        while user_input is None:
            user_input = game.read_numpad_input()  # Read input from numpad

        if user_input == str(answer):
            game.record_attempt(True)
            game.update_score(1)  # Correct answer: increase score
            result = "Correct!"
        else:
            game.record_attempt(False)
            game.update_score(-1)  # Incorrect answer: decrease score
            result = f"Incorrect! Correct: {answer}"

        game.display_message(result, str(game.score))
        sleep(2)  # Pause before next problem
