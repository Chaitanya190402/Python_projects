# Eye Controlled Mouse

This Python script uses OpenCV, Mediapipe, and PyAutoGUI to create an eye-controlled mouse. It detects facial landmarks, tracks eye movement, and simulates mouse actions based on predefined gestures.

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- PyAutoGUI (`pip install pyautogui`)

## Usage
1. Run the script: `python your_script_name.py`.
2. A window will appear showing your webcam feed with facial landmark tracking.
3. Adjust your face in the camera frame to start tracking.
4. The script will move the cursor based on your eye movements.
5. Blink both eyes simultaneously to simulate a mouse click.

## Features
- Tracks facial landmarks, specifically eye movement.
- Simulates mouse movements and clicks based on eye gestures.

## Notes
- Ensure your webcam is properly connected and accessible.
- The script uses Mediapipe for facial landmark detection and PyAutoGUI for mouse control.
- Customize the code as needed, such as adjusting the landmark points or gestures for mouse actions.

## Troubleshooting
- If the script is not working as expected, check if all dependencies are installed and your camera is functional.
- Adjust the code to fine-tune the landmark points and gestures for better performance.

Feel free to customize the script and experiment with additional functionalities!