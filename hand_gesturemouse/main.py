import mediapipe as mp
import cv2

from math import sqrt
import win32api
import pyautogui

Pic_Drawing = mp.solutions.drawing_utils
Hand = mp.solutions.hands
click = 0

video = cv2.VideoCapture(0)

with Hand.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
    while video.isOpened():
        _, frame = video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = cv2.flip(image, 1)

        image_height, image_Width, _ = image.shape

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                Pic_Drawing.draw_landmarks(image, hand, Hand.HAND_CONNECTIONS,
                                          Pic_Drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                          )

        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                for point in Hand.HandLandmark:

                    normalizedLandmark = handLandmarks.landmark[point]
                    pixelCoordinatesLandmark = Pic_Drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                           normalizedLandmark.y,
                                                                                           image_Width, image_height)

                    point = str(point)

                    if point == 'HandLandmark.INDEX_FINGER_TIP':
                        try:
                            Index_Finger_x = pixelCoordinatesLandmark[0]
                            Index_Finger_y = pixelCoordinatesLandmark[1]
                            win32api.SetCursorPos((Index_Finger_x * 4, Index_Finger_y * 5))

                        except:
                            pass

                    elif point == 'HandLandmark.THUMB_TIP':
                        try:
                            Thumb_Finger_x = pixelCoordinatesLandmark[0]
                            Thumb_Finger_y = pixelCoordinatesLandmark[1]
                            # print("thumb",Thumb_Finger_x)

                        except:
                            pass

                    try:
                        # pyautogui.moveTo(Index_Finger_x,Index_Finger_y)
                        Distance_x = sqrt(
                            (Index_Finger_x - Thumb_Finger_x) ** 2 + (Index_Finger_x - Thumb_Finger_x) ** 2)
                        Distance_y = sqrt(
                            (Index_Finger_y - Thumb_Finger_y) ** 2 + (Index_Finger_y - Thumb_Finger_y) ** 2)
                        if Distance_x < 5 or Distance_x < -5:
                            if Distance_y < 5 or Distance_y < -5:
                                click = click + 1
                                if click % 5 == 0:
                                    print("single click")
                                    pyautogui.click()

                    except:
                        pass

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

video.release()