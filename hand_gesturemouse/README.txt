# Hand Tracking with Mediapipe and OpenCV

This Python script utilizes the Mediapipe library for hand tracking and OpenCV for video processing. The script tracks hand landmarks and performs actions like moving the cursor and clicking based on the hand gestures.

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- PyAutoGUI (`pip install pyautogui`)
- win32api (Windows only, already included in some Python distributions)

## Usage
1. Ensure that you have installed the required dependencies.
2. Run the script: `python your_script_name.py`.
3. A window will appear showing hand tracking in real-time.
4. Move your hand to control the cursor, and perform gestures for clicking.

## Hand Gestures
- **Index Finger Tip:** Moves the cursor on the screen.
- **Thumb Tip:** Used for gestures like clicking.

## Actions
- **Single Click:** The script simulates a mouse click when certain gestures are detected.

## Notes
- Adjust `min_detection_confidence` and `min_tracking_confidence` in the script to fine-tune hand detection parameters.
- Ensure that your camera is properly connected and accessible.
- The script uses the `win32api` library for cursor control on Windows. Modify for compatibility with other operating systems.

## Troubleshooting
- If the script is not working as expected, check if all dependencies are installed and your camera is functional.
- Adjust the hand detection parameters for better performance.

Feel free to customize the script and experiment with additional functionalities!
