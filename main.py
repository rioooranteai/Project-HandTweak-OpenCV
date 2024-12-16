import cv2
import mediapipe as mp
import numpy as np
from Buttons import Button
from ImageProcessing import ImageProcessing as ip

capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

hands = mp.solutions.hands.Hands()
mp_drawing = mp.solutions.drawing_utils

last_x1, last_y1, last_filter = None, None, None

while True:
    success, img = capture.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    filter_img = img
    mode = ip(img)

    buttons = Button(img)
    buttons.activate_all_buttons()

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            x1, x2, y1, y2 = None, None, None, None

            for id, lm in enumerate(hand_landmarks.landmark):
                height, width, _ = img.shape
                x, y = int(lm.x * width), int(lm.y * height)

                if id == 8:  # Jari telunjuk
                    cv2.circle(img=img, center=(x, y), radius=8, color=(255, 255, 255), thickness=3)
                    x1, y1 = x, y

                if id == 4:  # Jari ibu jari
                    cv2.circle(img=img, center=(x, y), radius=8, color=(255, 255, 255), thickness=3)
                    x2, y2 = x, y

            if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 5)
                panjang = int(np.sqrt(((x2 - x1) ** 2 + (y2 - y1) ** 2)))
                mode.setpanjang(panjang)
                print(f"Panjang: {panjang}")

                switcher = None

                if mode.get_average_memory_value() != 0:
                    if (1040 <= x1 <= 1230) and (20 < y1 < 120):
                        filter_img = mode.blur()
                        last_filter = "blur"

                    elif (830 <= x1 <= 1020) and (20 < y1 < 120):
                        filter_img = mode.contrast()
                        last_filter = "contrast"

                    elif (620 <= x1 <= 810) and (20 < y1 < 120):
                        filter_img = mode.brightness()
                        last_filter = "brightness"

                if last_filter:
                    if last_filter == "blur":
                        filter_img = mode.blur()
                    elif last_filter == "contrast":
                        filter_img = mode.contrast()
                    elif last_filter == "brightness":
                        filter_img = mode.brightness()

    cv2.imshow('Img', filter_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
