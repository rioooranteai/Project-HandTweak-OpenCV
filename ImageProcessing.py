import cv2
import numpy as np
from collections import deque
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
        kernel = self.__len__()
        blur = cv2.blur(self.image, (kernel, kernel))

        return blur

    def imagesegmentation(self):
        # self.__len__()
        # self.setpanjang(10)
        # self.setpanjang(10)
        # self.setpanjang(10)

        # min = np.min(self.memory)
        # max = np.max(self.memory)

        # normalized_data = int((self.__len__() - min) / (max - min) * (10 - 2) + 2)

        new_image = np.array(self.image)
        reshape_image = new_image.reshape(-1, 3)
        kmeans = KMeans(n_clusters=4, n_init=10)
        kmeans.fit(reshape_image)

        segmented_img = kmeans.cluster_centers_[kmeans.labels_]
        segmented_img = segmented_img.reshape(new_image.shape)

        return segmented_img / 255

    def edgedetectiion(self):
        img_grey = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        G_x = np.array([[1,0,-1], [2,0,-2], [1,0,-1]]) * image.reshape(3, -1)
        G_y = np.array([[1,0,-1], [0,0,0], [-1,-2,-1]]) * image.reshape(3, -1)

        G = np.sqrt(np.square(G_x) + np.square(G_y))

        return G

    def __len__(self):
        return int(np.mean(self.memory))
