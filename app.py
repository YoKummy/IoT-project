import random
from flask import Flask, render_template, request, session, redirect, url_for
import drivers
from time import sleep

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Initialize the LCD display
lcd = drivers.Lcd()

# Game state variables
current_answer = None
score = 10

def generate_problem(difficulty):
    """Generates a random math problem based on the selected difficulty."""
    if difficulty == "easy":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-"])
        problem = f"{num1} {operation} {num2}"
        correct_answer = eval(problem)

    elif difficulty == "medium":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)
        operation1 = random.choice(["+", "-", "*"])
        operation2 = random.choice(["+", "-", "*", "/"])
        problem = f"{num1} {operation1} {num2} {operation2} {num3}"
        correct_answer = eval(problem)

    elif difficulty == "hard":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 3)  # Keep exponent small
        operation = random.choice(["+", "-", "*", "/", "sqrt", "**"])

        if operation == "sqrt":
            num1 = random.randint(1, 10)
            num1 = num1**2
            problem = f"sqrt({num1})"
            correct_answer = round(num1 ** 0.5, 2)
        elif operation == "**":
            problem = f"{num1} ** {num2}"
            correct_answer = num1 ** num2
        else:
            num3 = random.randint(1, 10)
            operation2 = random.choice(["+", "-", "*", "/"])
            problem = f"{num1} {operation} {num2} {operation2} {num3}"
            correct_answer = eval(problem)

    # Format the problem for LCD (ensure it's readable and within 16 characters)
    display_problem = problem.replace("**", "^").replace("sqrt", "√")

    # Update LCD with the problem
    lcd.lcd_clear()
    lcd.lcd_display_string("Math Problem:", 1)
    lcd.lcd_display_string(display_problem[:16], 2)  # Show the problem truncated to 16 characters

    return problem, correct_answer

@app.route("/", methods=["GET", "POST"])
def index():
    global current_answer, score

    # Set the difficulty based on session
    difficulty = session.get("difficulty", "easy")

    if request.method == "POST":
        if "difficulty" in request.form:
            session["difficulty"] = request.form["difficulty"]
            return redirect(url_for("index"))

        # Handle user's answer
        try:
            user_answer = float(request.form["answer"])
        except ValueError:
            lcd.lcd_clear()
            lcd.lcd_display_string("Invalid input!", 1)
            lcd.lcd_display_string("Enter a number", 2)
            return render_template(
                "game.html",
                problem=problem,
                score=score,
                result="Invalid input! Please enter a number.",
                difficulty=difficulty,
            )

        # Check if the answer is correct
        if user_answer == current_answer:
            score += 1
            result = "Correct!"
            lcd.lcd_clear()
            lcd.lcd_display_string("Correct!", 1)
        else:
            score -= 2
            result = f"Incorrect! The answer was {current_answer}"
            lcd.lcd_clear()
            lcd.lcd_display_string("Incorrect!", 1)
            lcd.lcd_display_string(f"Ans: {current_answer}", 2)

        # Generate the next problem
        problem, correct_answer = generate_problem(difficulty)
        current_answer = correct_answer

        return render_template(
            "game.html",
            problem=problem,
            score=score,
            result=result,
            difficulty=difficulty,
        )

    # Generate the first problem
    problem, correct_answer = generate_problem(difficulty)
    current_answer = correct_answer

    return render_template(
        "game.html", problem=problem, score=score, result=None, difficulty=difficulty
    )

@app.teardown_appcontext
def cleanup_lcd(exception):
    """Ensure LCD is cleared on app exit."""
    lcd.lcd_clear()

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        print("Exiting...")
        lcd.lcd_clear()
