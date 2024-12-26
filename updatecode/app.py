import random
import threading
import drivers
from time import sleep
import RPi.GPIO as GPIO
from flask import Flask, redirect, render_template, request, url_for

# Initialize Flask app
app = Flask(__name__)

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
questions_answered = 0
time_up = False
game_over = False
win = False
player_data = {
    "name": "",
    "difficulty": 1,
}

def set_servo_angle(angle):
    """Set the servo motor to a specific angle (0-180 degrees)."""
    duty_cycle = 2 + (angle / 18)  # Map angle to duty cycle
    servo.ChangeDutyCycle(duty_cycle)
    sleep(0.5)
    servo.ChangeDutyCycle(0)  # Stop sending signal to prevent jitter

def generate_problem(difficulty):
    """Generates a random math problem based on the selected difficulty."""
    if difficulty == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-"])
        problem = f"{num1}{operation}{num2}"
        correct_answer = eval(problem)
        
    elif difficulty == 2:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)
        operation1 = random.choice(["+", "-", "*"])
        operation2 = random.choice(["+", "-", "*", "/"])
        problem = f"{num1}{operation1}{num2}{operation2}{num3}"
        correct_answer = eval(problem)

    elif difficulty == 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 3)  # Keep exponent small
        operation = random.choice(["+", "-", "*", "", "sqrt", "**"])

        if operation == "sqrt":
            num1 = random.randint(1, 10)
            num1 = num1**2
            problem = f"sqrt({num1})"
            correct_answer = round(num1 ** 0.5, 2)
        elif operation == "**":
            problem = f"{num1}**{num2}"
            correct_answer = num1 ** num2
        else:
            num3 = 2#random.randint(1, 10)
            operation2 = random.choice(["+", "-", "*", "/"])
            problem = f"{num1}{operation}{num2}{operation2}{num3}"
            correct_answer = eval(problem)

    if isinstance(correct_answer, float):
        correct_answer = round(correct_answer, 2)

    return problem, correct_answer

def update_lcd(problem, score, time_left=None):
    """Updates the LCD display with the current problem, score, and optional timer."""
    display.lcd_clear()
    display.lcd_display_string(f"Problem:{problem}", 1)
    if time_left is not None:
        display.lcd_display_string(f"Score:{score} Time:{time_left}s", 2)
    else:
        display.lcd_display_string(f"Score:{score}", 2)

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
    global score, game_over, win
    if score <= 0:
        set_servo_angle(180)
        display.lcd_clear()
        display.lcd_display_string("Game Over!", 1)
        display.lcd_display_string("Score: 0", 2)
        sleep(3)
        set_servo_angle(0)
        game_over = True
    elif score >= 12:
        display.lcd_clear()
        display.lcd_display_string("You Win!", 1)
        display.lcd_display_string("Score: 12", 2)
        sleep(3)
        win = True
'''
@app.route('/')
def home():
    """Home page displaying player stats."""
    global score, questions_answered, game_over, win
    return render_template('stats.html', score=score, questions_answered=questions_answered, game_over=game_over, win=win)
'''
@app.route('/', methods=['GET','POST'])
def home():
    """Home page to enter player name and difficulty level."""
    if request.method == 'POST':
        name = request.form['name']
        difficulty = int(request.form['difficulty'])

        # Store the player data
        player_data["name"] = name
        player_data["difficulty"] = difficulty
        
        return redirect(url_for('start_game'))
    
    return render_template('index.html')

'''
@app.route('/start_game')
def start_game():
    """Start the game by resetting variables."""
    global score, questions_answered, game_over, win
    score = 6
    questions_answered = 0
    game_over = False
    win = False
    threading.Thread(target=game_loop, daemon=True).start()
    return "Game Started! <a href='/'>Go back</a>"
'''

@app.route('/start_game', methods=['GET','POST'])
def start_game():
    """Start the game after submitting the name and difficulty."""
    global score, questions_answered, game_over, win
    if request.method == 'POST':
        score = 6
        questions_answered = 0
        game_over = False
        win = False
        
        # Start the game in a new thread
        threading.Thread(target=game_loop, daemon=True).start()
        
        # Redirect to the game status page
        return redirect(url_for('game_status'))
    

@app.route('/game_status')
def game_status():
    """Page displaying game status and player stats."""
    return render_template('stats.html', score=score, questions_answered=questions_answered, game_over=game_over, win=win, player_name=player_data['name'])



# Main game loop
def game_loop():
    global current_problem, current_answer, score, questions_answered, time_up
    #difficulty = int(input("Enter difficulty: 1~3"))  # Choose difficulty level
    #display.lcd_clear()
    #display.lcd_display_string("Enter difficulty", 1)
    #display.lcd_display_string("Enter:" + str(difficulty), 2)
    #sleep(3)
    #display.lcd_clear()
    set_servo_angle(0)
    difficulty = player_data['difficulty']

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
                questions_answered += 1
                result = "Correct!"
            else:
                score -= 2
                questions_answered += 1
                result = f"Wrong!Correct:{current_answer}"

        except TimeoutError:
            score -= 2
            result = "Time's up!"
            time_up = True

        # Wait for the timer thread to finish (ensure clean exit)
        timer_thread.join()

        # Display result and wait before showing the next question
        update_lcd(result, score)
        sleep(2)

        # Check if the game should end
        check_score()

        if game_over or win:
            break

if __name__ == '__main__':
    # Start the game in a separate thread
    threading.Thread(target=game_loop, daemon=True).start()

    # Start the Flask app
    app.run(host='0.0.0.0', port=5000)