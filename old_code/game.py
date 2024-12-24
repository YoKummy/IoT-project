import random
import threading
import drivers
from time import sleep
import RPi.GPIO as GPIO


# Initialize LCD display
display = drivers.Lcd()
servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)  # 50 Hz PWM
servo.start(0)

# Game state variables
current_problem = None
current_answer = None
score = 6
time_up = False

def set_servo_angle(angle):
    """Set the servo motor to a specific angle (0-180 degrees)."""
    duty_cycle = 2 + (angle / 18)  # Map angle to duty cycle
    servo.ChangeDutyCycle(duty_cycle)
    sleep(0.5)
    servo.ChangeDutyCycle(0)  # Stop sending signal to prevent jitter

def generate_problem(difficulty):
    """Generates a random math problem based on the selected difficulty."""
    if difficulty == "easy":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-"])
        problem = f"{num1} {operation} {num2}"
        correct_answer = eval(problem)

    if isinstance(correct_answer, float):
        correct_answer = round(correct_answer, 2)

    return problem, correct_answer

def update_lcd(problem, score, time_left=None):
    """Updates the LCD display with the current problem, score, and optional timer."""
    display.lcd_clear()
    display.lcd_display_string(f"Problem: {problem}", 1)
    if time_left is not None:
        display.lcd_display_string(f"Score: {score} Time: {time_left}s", 2)
    else:
        display.lcd_display_string(f"Score: {score}", 2)

def countdown_timer():
    """Manages the 5-second countdown timer."""
    global time_up
    time_left = 5  # Set the countdown duration
    while time_left > 0 and not time_up:  # Stop the timer early if answered
        update_lcd(current_problem, score, time_left)
        sleep(1)
        time_left -= 1
    if time_left == 0:
        time_up = True  # Signal that time is up
        

def check_score():
    """Checks if the game should end based on the score."""
    global score
    if score <= 0:
        set_servo_angle(180)
        display.lcd_clear()
        display.lcd_display_string("Game Over!", 1)
        display.lcd_display_string("Score: 0", 2)
        sleep(3)
        raise SystemExit("Game Over! You lost.")
    elif score >= 12:
        display.lcd_clear()
        display.lcd_display_string("You Win!", 1)
        display.lcd_display_string("Score: 12", 2)
        sleep(3)
        raise SystemExit("You Win! Congratulations.")

# Main game loop
try:
    difficulty = "easy"  # Choose difficulty level
    set_servo_angle(0)

    while True:
        # Generate a new problem
        current_problem, current_answer = generate_problem(difficulty)
        time_up = False

        # Start the countdown timer in a separate thread
        timer_thread = threading.Thread(target=countdown_timer)
        timer_thread.start()

        try:
            # Wait for user input or time out
            user_answer = input(f"Solve:{current_problem}=")
            if time_up:
                raise TimeoutError  # Raise an error if time is up
            time_up = True  # Stop the timer if answered
            user_answer = float(user_answer)  # Convert input to a number

            # Check the answer
            if user_answer == current_answer:
                score += 1
                result = "Correct!"
            else:
                score -= 2
                result = f"Incorrect! Correct:{current_answer}"

        except TimeoutError:
            score -= 2
            result = "Time's up! Score decreased!"
            time_up = True

        # Wait for the timer thread to finish (ensure clean exit)
        timer_thread.join()

        # Display result and wait before showing the next question
        update_lcd(result, score)
        sleep(2)

        # Check if the game should end
        check_score()

except KeyboardInterrupt:
    # Cleanup on exit
    display.lcd_clear()
    print("Game Over")