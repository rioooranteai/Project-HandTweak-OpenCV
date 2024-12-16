from collections import deque

import cv2
import numpy as np
from sklearn.cluster import KMeans

class ImageProcessing:
    def __init__(self, image):
        self.memory = deque(maxlen=12000)
        self.image = image
        self.panjang = 0

    def setpanjang(self, panjang):
        self.panjang = panjang
        x = self.panjang - 35
        self.memory.append(np.maximum(0, x))

    def blur(self):
        kernel_size = self.get_average_memory_value()

        if kernel_size < 1:
            kernel_size = 1

        blur = cv2.blur(self.image, (kernel_size, kernel_size))
        return blur

    def brightness(self):
        beta_normalized = (self.get_average_memory_value() - 20) * ((100 - (-100)) / (220 - 20)) + 1
        beta = np.clip(beta_normalized, -100, 100)
        adjusted = cv2.convertScaleAbs(self.image, alpha=1.0, beta=beta)
        return adjusted

    def contrast(self):
        alpha_normalized = (self.get_average_memory_value() - 20) * ((3 - 0.1) / (220 - 20)) + 1
        alpha = np.clip(alpha_normalized, 0.1, 3.0)
        adjusted = cv2.convertScaleAbs(self.image, alpha=alpha, beta=0)
        return adjusted

    def imagesegmentation(self):
        new_image = np.array(self.image)
        reshape_image = new_image.reshape(-1, 3)
        kmeans = KMeans(n_clusters=4, n_init=10)
        kmeans.fit(reshape_image)

        segmented_img = kmeans.cluster_centers_[kmeans.labels_]
        segmented_img = segmented_img.reshape(new_image.shape)

        return segmented_img / 255

    def edgedetection(self):
        img_grey = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        G_x = cv2.Sobel(img_grey, cv2.CV_64F, 1, 0, ksize=3)
        G_y = cv2.Sobel(img_grey, cv2.CV_64F, 0, 1, ksize=3)

        G = np.sqrt(np.square(G_x) + np.square(G_y))
        G = np.uint8(np.absolute(G))

        return G

    def get_average_memory_value(self):
        if len(self.memory) > 0:
            return int(np.mean(self.memory))
        return 0
