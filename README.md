# IoT-Project: Math Defender

## Overview

**Project**:  
This is a single-player interactive game designed to help children and teenagers practice math skills in a fun and engaging way. Players solve math problems using physical buttons, and the game responds with real-time feedback. The system integrates IoT functionalities, allowing players or parents to customize the game settings through an online interface.

**Possible Use Case**:  


**Project Objectives**:  
The main goal is to provide a hands-on, gamified approach to math practice. Players can adjust game difficulty, customize problem types, and compete against the clock to improve their skills.

---

## Features

- **Math Problem Generator**: Dynamic generation of addition, subtraction, multiplication, and division problems.
- **Real-Time Input**: Physical buttons allow players to input answers quickly.
- **IoT Customization**: Change game difficulty, and problem types through an online interface.
~~- Progress Tracking: Monitor player performance and improvement over time. Flask is a b*tch~~

---

## Technology Stack

### Hardware
- **Raspberry Pi 4 (or higher)**: Core processing unit.
- **Numpad**: Number keys (1–9), decimal (`.`), and `Enter`.
- **LCD Screen**: Displays math problems and feedback.
- **Servo Motor + Rubberband**: Ejects a toy or activates a reward system.
- **Power Supply**: Reliable power through a battery pack or adapter.

### Software
- **Python**: Core programming language for logic and hardware interaction.
- **GPIO Zero**: To manage button inputs.
- **Flask/Node.js** (optional): To build a web interface for IoT features.
- **LCD Driver**: Included in the file.

---

## Components

1. **Input System**:  
   - numpad
   
2. **Output System**:  
   - An LCD screen displays math problems and player responses.
   - A spring-powered(or rubber band) eject system provides a visual punishment for correct answers.

3. **Processing Unit**:  
   - Raspberry Pi 4B handles game logic, button presses, and displays the game state.

---

## Game Flow

1. **Startup**:  
   - The player powers on the box and initializes the game.
   - However, it still require player to manually start the game through terminal. Due to the need to connect to wifi first then start the game(Flask).
   - The system generates a math problem and displays it on the LCD screen.

2. **Input**:  
   - The player solves the problem and enters the answer using the number buttons.
   - Press the `Enter` button to submit the answer.

3. **Feedback**:  
   - If the answer is correct, the system rewards the player by not ejecting player's model and plus 1.
   - If the answer is incorrect, the system deducts 2 points, when points reachs zero, model ejected.

4. **Rounds**:  
   - The game progresses through a series of problems.
   - Players can compete against a timer or solve as many problems as they can in a fixed time.

---

## Example Use Case

1. **Problem**: The screen shows: `7 x 8 = ?`  
2. **Player Input**:  
   - Press buttons `5`, `6`, and `Enter` (56).  
3. **Feedback**:  
   - **Correct Answer**: The lcd displays next problem and plus score.
   - **Incorrect Answer**: The screen ~~shows "Correct Answer: 56. Try Again!" ONLY IF I HAVE A BIGGER LCD~~ displays "Wrong" and deduct points.  

---

## Proposed Methodologies

1. **Problem Generator**:  
   - Use Python to dynamically generate random math problems based on difficulty.  
   - Example logic:  
     easy: plus and minus
     mid: multiply and division
     hard: log and sqrt

2. **IoT Integration**:  
   - A web interface (using Flask or Node.js) to adjust game settings like difficulty remotely.

3. **Hardware Eject Mechanism**:  
   - Use a rubber band-powered or traditional spring mechanism to eject a toy as a physical reward for correct answers.

---

## Hardware Wiring

### Button Layout
- 0–9: Numeric input.
- `.`: For decimal answers.
- `Enter`: Submit the answer.
- `Delete`: For delete input.

### Connections
- Numpad is connected via USB port.
- Connect LCD to Raspberry pi via wire?
- Connect Servo to Raspberry pi?

## Step by step

### STEP 1! You need a box and some component
![Alt text](images/IMG_2330.jpg)
Bread board is optional, you can add some buttons, leds or other component.
### STEP 2! Boom, box finished!
![Alt text](images/IMG_2341.jpg)
### STEP 3! Put your whole component into it
![Alt text](images/IMG_2342.jpg)
I put the lcd on front and carve a hole to hold it.
![Alt text](images/IMG_2343.jpg)
And I also carve a hole on the back to let the power cable go through.
![Alt text](images/IMG_2344.jpg)
I use 3 chapsticks to hold the rubberband cuz other things are either too short or too fragile.
![Alt text](images/IMG_2345.jpg)
Last carve a hole on the back and seated the Servo so when it connects to the rubberband it doesn't move around.

### STEP 4! Profit???
![Alt text](images/IMG_2347.png)
Enter the name and difficulty.
![Alt text](images/IMG_2348.jpg)
The lcd display the information after enter the variable.


## Optional Enhancements

- **Data Logging**: Store player performance data (e.g., accuracy, speed) for progress tracking.
- **Customization**: Allow users to choose specific math problem types (e.g., fractions, algebra).
- **Multiplayer**: Allow two user to battle with each other with two sets of numpad.

![Alt text](images/IMG_2331.jpg)

---

## Reference

Eject system: https://www.youtube.com/watch?v=oa3bkelYmOw&t=197s
Lcd driver and tutorial: https://youtu.be/3XLjVChVgec?si=pfhjOG6D5fRk9OT9
---

## WIP