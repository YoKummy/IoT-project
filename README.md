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
- **IoT Customization**: Change game difficulty, timer settings, and problem types through an online interface.
- **Progress Tracking**: Monitor player performance and improvement over time.

---

## Technology Stack

### Hardware
- **Raspberry Pi 4 (or higher)**: Core processing unit.
- **Numpad**: Number keys (1–9), decimal (`.`), and `Enter`.
- **LCD Screen**: Displays math problems and feedback.
- **Servo Motor + Spring Mechanism**: Ejects a toy or activates a reward system.
- **Power Supply**: Reliable power through a battery pack or adapter.

### Software
- **Python**: Core programming language for logic and hardware interaction.
  - **GPIO Zero**: To manage button inputs.
  - **NumPy**: For random problem generation.
- **Flask/Node.js** (optional): To build a web interface for IoT features.

---

## Components

1. **Input System**:  
   - numpad
   
2. **Output System**:  
   - An LCD screen displays math problems and player responses.
   - A spring-powered(or rubber band) eject system provides a visual reward for correct answers.

3. **Processing Unit**:  
   - Raspberry Pi handles game logic, button presses, and displays the game state.

---

## Game Flow

1. **Startup**:  
   - The player powers on the box and initializes the game.
   - The system generates a math problem and displays it on the LCD screen.

2. **Input**:  
   - The player solves the problem and enters the answer using the number buttons.
   - Press the `Enter` button to submit the answer.

3. **Feedback**:  
   - If the answer is correct, the system rewards the player by not ejecting player's model.
   - If the answer is incorrect, the system displays the correct answer and deducts points, when points reachs zero, model ejected.

4. **Rounds**:  
   - The game progresses through a series of problems.
   - Players can compete against a timer or solve as many problems as they can in a fixed time.

---

## Example Use Case

1. **Problem**: The screen shows: `7 x 8 = ?`  
2. **Player Input**:  
   - Press buttons `5`, `6`, and `Enter` (56).  
3. **Feedback**:  
   - **Correct Answer**: The spring ejects a toy, and the next problem appears.  
   - **Incorrect Answer**: The screen shows "Correct Answer: 56. Try Again!"  

---

## Proposed Methodologies

1. **Problem Generator**:  
   - Use Python to dynamically generate random math problems based on difficulty.  
   - Example logic:  
     easy: plus and minus
     mid: multiply and division
     hard: log and sqrt

2. **IoT Integration**:  
   - A web interface (using Flask or Node.js) to adjust game settings like difficulty and timers remotely.

3. **Hardware Eject Mechanism**:  
   - Use a rubber band-powered or traditional spring mechanism to eject a toy as a physical reward for correct answers.

---

## Hardware Wiring

### Button Layout
- 1–9: Numeric input.
- `.`: For decimal answers.
- `Enter`: Submit the answer.

### Connections
- Each button is connected to a GPIO pin on the Raspberry Pi with pull-down resistors.

---

## Optional Enhancements

- **Data Logging**: Store player performance data (e.g., accuracy, speed) for progress tracking.
- **Customization**: Allow users to choose specific math problem types (e.g., fractions, algebra).
- **Multiplayer**: Allow two user to battle with each other with two sets of numpad.

---

## Reference

Eject system: https://www.youtube.com/watch?v=oa3bkelYmOw&t=197s

---

## WIP