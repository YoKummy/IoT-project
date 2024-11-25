import random
from flask import Flask, render_template, request, session, redirect, url_for

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Game state variables
current_answer = None
score = 10


def generate_problem(difficulty):
    """Generates a random math problem based on the selected difficulty."""
    if difficulty == "easy":
        # Two numbers and one operation
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-"])
        problem = f"{num1} {operation} {num2}"
        correct_answer = eval(problem)

    elif difficulty == "medium":
        # Three numbers and two operations
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)
        operation1 = random.choice(["+", "-", "*"])
        operation2 = random.choice(["+", "-", "*", "/"])
        problem = f"{num1} {operation1} {num2} {operation2} {num3}"
        correct_answer = eval(problem)

    elif difficulty == "hard":
        # Mixed operations, including sqrt and **
        operations = ["+", "-", "*", "/", "sqrt", "**"]
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 3)  # Keep exponent small
        operation = random.choice(operations)

        # Handle special cases for sqrt and **
        if operation == "sqrt":
            num1 = random.randint(1, 10)  # Ensure positive values for sqrt
            num1 = num1**2
            problem = f"sqrt({num1})"
            correct_answer = round(num1 ** 0.5, 2)
        elif operation == "**":
            problem = f"{num1} ** {num2}"
            correct_answer = num1 ** num2
        else:
            # General case for other operations
            num3 = random.randint(1, 10)
            operation2 = random.choice(["+", "-", "*", "/"])
            problem = f"{num1} {operation} {num2} {operation2} {num3}"
            correct_answer = eval(problem)

    # Round the answer to 2 decimal places for division problems
    if isinstance(correct_answer, float):
        correct_answer = round(correct_answer, 2)

    return problem, correct_answer


@app.route("/", methods=["GET", "POST"])
def index():
    global current_answer, score

    # Set the difficulty based on session (default to 'easy' if not set)
    difficulty = session.get("difficulty", "easy")

    if request.method == "POST":
        if "difficulty" in request.form:
            # Update the difficulty based on user selection
            session["difficulty"] = request.form["difficulty"]
            return redirect(url_for("index"))  # Reload page to apply new difficulty

        # Get the user's answer from the form input
        try:
            user_answer = float(request.form["answer"])
        except ValueError:
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
            result = "Correct! Well done!"
        else:
            score -= 2
            result = f"Incorrect! The correct answer was {current_answer}"

        # Generate the next problem based on difficulty
        problem, correct_answer = generate_problem(difficulty)
        current_answer = correct_answer

        return render_template(
            "game.html",
            problem=problem,
            score=score,
            result=result,
            difficulty=difficulty,
        )

    # Generate the first problem based on difficulty
    problem, correct_answer = generate_problem(difficulty)
    current_answer = correct_answer

    return render_template(
        "game.html", problem=problem, score=score, result=None, difficulty=difficulty
    )


if __name__ == "__main__":
    app.run(debug=True)
