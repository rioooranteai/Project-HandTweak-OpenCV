import cv2
import numpy as np
import mediapipe as mp
from ImageProcessing import ImageProcessing as ip

capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)
pTime = 0

hands = mp.solutions.hands.Hands()
mp_drawing = mp.solutions.drawing_utils

while True:
    success, img = capture.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    filter = img
    mode = ip(img)

    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:
            x1, x2, y1, y2 = None, None, None, None

            for id, lm in enumerate(hand_landmarks.landmark):

                height, width, _ = img.shape
                x, y = int(lm.x * width), int(lm.y * height)

                if id == 8:
                    # cv2.circle(img=img, center=(x,y), radius=8, color=(255,255,255), thickness=3)
                    x1, y1 = x, y

                if id == 4:
                    # cv2.circle(img=img, center=(x, y), radius=8, color=(255, 255, 255), thickness=3)
                    x2, y2 = x, y

                if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
                    # cv2.line(img, (x1,y1), (x2,y2), (0,0,0), 5)
                    panjang = int(np.sqrt(((x2 - x1) ** 2 + (y2 - y1) ** 2)))
                    mode.setpanjang(panjang)

                    switcher = None

                    if mode.__len__() != 0:
                        filter = mode.blur()


    cv2.imshow('Img', filter)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
