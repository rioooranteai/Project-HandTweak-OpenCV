import cv2

class Button:
    def __init__(self, image):
        self.image = image

    def draw_button(self, start_point, end_point, text):
        color = (255, 0, 0)
        thickness = 3

        cv2.rectangle(self.image, start_point, end_point, color, thickness)

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        text_color = (255, 255, 255)

        text_size = cv2.getTextSize(text, font, font_scale, 2)[0]
        text_x = start_point[0] + (end_point[0] - start_point[0] - text_size[0]) // 2
        text_y = start_point[1] + (end_point[1] - start_point[1] + text_size[1]) // 2

        cv2.putText(self.image, text, (text_x, text_y), font, font_scale, text_color, 2)

    def button_blur(self):
        self.draw_button((1040, 20), (1230, 120), "Blur")

    def button_contrast(self):
        self.draw_button((830, 20), (1020, 120), "Contrast")

    def button_brightness(self):
        self.draw_button((620, 20), (810, 120), "Brightness")

    def activate_all_buttons(self):
        self.button_brightness()
        self.button_contrast()
        self.button_blur()
