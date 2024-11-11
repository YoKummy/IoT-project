# IoT-project

## Wizard defender

## Overview
-**Project**: This is a mini game with interactive box where two players can compete with each other to see who is the better wizard. With internet you can even set the attributes of the game such as: Health, round, attack, and time...

-**Possible use case**: Are you tired of scrolling through social media when you are bored in class? Are you tired of listening to teacher yapping about how important it is to remember that one single noun that you have to remember it and use it in test? Are you simply bored when sitting at your desk not knowing how to write that homework? 

Well you are in luck my friend! Today we will sell the brand new WIZARD DEFENDER for the price of low low $99.99!!! 
  
What did you say? "That's cheap!", Well hell yeah it is cheap! Come on down to your local gaming store and get your Super wizard defeender toy!!!!!! Yee haaa~ Howdy!

-**Project objectives**: This project main goal is to provide a cool way to play with games. You can change the game attributes through internet connecting the box. And added a physical player model to give a better immersion.

## Features
- **Gesture Recognition**: Detects specific hand or body gestures using the camera.
- **Real-Time Detection**: Provides quick gesture response for user convenience.

## Current survey
Maybe the game logic will be more complicated than the hardware side. The hardware side basically only needs a camera with some computation hardware to accelerate the calculation and some mechanic that enable the compress of spring and let go of the string. 

The problem might be how to load the spring and make sure it doesn't go off automatically and only go off when one side died. Also, the hardware might be a little be old so the reaction time might be slow leading the game not being fun to play. The casting spell is also a big problem because what if i want to add a bit complex character into it but the gesture recognition model doesn't know what is it. :/


## Technology Stack
- **Hardware**: 
  - Raspberry Pi 4 or higher(for IoT functionality)
  - USB/PI Camera
  - Servo motor * 4?
  - Some spring
- **Software**:
  - Python (OpenCV for gesture recognition)
  - Machine Learning model for gesture detection (TensorFlow/Keras)
  - Flask/Node.js (optional) for web-based monitoring and control interface

## Components
1. **Camera**: Captures real-time video of the user.
2. **Processing Unit**: Raspberry Pi processes the video feed and runs the gesture recognition model.
3. **Eject Mechanism**: With the help of servo motor blocking the spring and releasing the spring to make the character eject when the game ends.
4. **Power Supply**: Ensure reliable power for the system (e.g., a power bank or battery pack).

## Proposed methodologies
User can start by connecting to the box to initialize the game, before starting, user can choose to play single player or multiplayer(2 people only). When the player is ready. 

They can start the game by pressing a pyhsical button on the box. The box will do a count down and start the round. There will be a attacker and a defender, defender needs to replicate attackers move, if defender cannot replicate attackers move, defender will lose health points, however, if defender successfully replicate attackers move, the role will change and move to the next round. 

Once health points go down to 0 or the timer count to 0 the game end. The spell should cast in a specific charachters. Once the battle end, the loser sides box will use spring to eject character meaning that they died.

## Reference
**https://maker.pro/raspberry-pi/projects/wand-controlled-horcrux-box**

## WIP