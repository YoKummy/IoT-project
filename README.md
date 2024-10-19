# IoT-project

## Smart locker with laser ir sensor

## Overview
This IoT project integrates a IR sensor onto a box with a lock that detect a IR laser movement to unlock it.

## Features
- **Gesture Recognition**: Detects specific hand or body gestures using the camera.
- **Smart Lock System**: Unlocks the box when a valid gesture is recognized.
- **Real-Time Detection**: Provides quick gesture response for user convenience.
- **Security**: Supports only pre-configured gestures, providing an extra layer of security.

## Technology Stack
- **Hardware**: 
  - Raspberry Pi 4 or higher(for IoT functionality)
  - USB/PI Camera
  - Servo motor or solenoid lock for the box
- **Software**:
  - Python (OpenCV for gesture recognition)
  - Machine Learning model for gesture detection (TensorFlow/Keras)
  - MQTT (optional) for cloud communication
  - Flask/Node.js (optional) for web-based monitoring and control interface

## Components
1. **Camera**: Captures real-time video of the user.
2. **Processing Unit**: Raspberry Pi processes the video feed and runs the gesture recognition model.
3. **Locking Mechanism**: Servo motor or solenoid to physically unlock the box upon valid gesture detection.
4. **Power Supply**: Ensure reliable power for the system (e.g., a power bank or battery pack).

## Flowchart
<img src="https://drive.google.com/file/d/12E4vvuNnkRL0h4R0kRCv1kFjeHY3aCgR/view?usp=sharing" alt="A photo show flowchart of this project">