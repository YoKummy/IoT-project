# game.py
import random
import drivers
from time import sleep
from game_state import GameState

lcd = drivers.Lcd()
game_state = GameState()

def generate_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-"])
    problem = f"{num1} {operation} {num2}"
    correct_answer = eval(problem)
    lcd.lcd_clear()
    lcd.lcd_display_string("Math Problem:", 1)
    lcd.lcd_display_string(problem[:16], 2)
    return correct_answer

def play_game():
    global game_state
    try:
        while True:
            correct_answer = generate_problem()
            user_input = ""
            lcd.lcd_clear()
            lcd.lcd_display_string("Enter your answer:", 1)

            # Capture user input
            print("Type your answer:")
            user_input = input().strip()

            game_state.increment_attempts()
            if user_input.isdigit() and int(user_input) == correct_answer:
                game_state.increment_correct()
                game_state.update_score(1)
                lcd.lcd_clear()
                lcd.lcd_display_string("Correct!", 1)
            else:
                game_state.update_score(-2)
                lcd.lcd_clear()
                lcd.lcd_display_string("Wrong!", 1)
                lcd.lcd_display_string(f"Ans: {correct_answer}", 2)

            sleep(2)
    except KeyboardInterrupt:
        print("Exiting...")
        lcd.lcd_clear()

if __name__ == "__main__":
    play_game()
