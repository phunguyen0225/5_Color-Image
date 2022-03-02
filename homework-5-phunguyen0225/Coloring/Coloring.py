import numpy as np
import cv2
import math


class Coloring:

    def intensity_slicing(self, image, n_slices):
        # Steps:

        # 1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        # 2. Randomly assign a color to each interval
        # 3. Create and output color image
        # 4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to

        # returns colored image

        # 1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        interval = np.linspace(0, image.max(), n_slices+1)

        # 2. Randomly assign a color to each interval
        color = np.random.randint(0, 255, (n_slices, 3))

        row = image.shape[0]
        col = image.shape[1]

        # 3. Create and output color image
        colored_image = np.zeros((row, col, 3), dtype=np.uint8)

        # 4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to
        for i in range(row):
            for j in range(col):
                for k in range(n_slices):
                    if interval[k+1] >= image[i, j]:
                        colored_image[i, j] = color[k]
                        break

        # returns colored image
        return colored_image

    def color_transformation(self, image, n_slices, theta):

        # Steps:
        # 1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        # 2. create red values for each slice using 255*sin(slice + theta[0])
        #    similarly create green and blue using 255*sin(slice + theta[1]), 255*sin(slice + theta[2])
        # 3. Create and output color image
        # 4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to

        # returns colored image

        # 1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        interval = np.linspace(0, 255, n_slices + 1)

        # 2. create red values for each slice using 255*sin(slice + theta[0])
        red = np.array([255*np.sin(interval + theta[0])])

        #green, 255*sin(slice + theta[1])
        green = np.array([255*np.sin(interval + theta[1])])

        # blue, 255*sin(slice + theta[2]
        blue = np.array([255*np.sin(interval + theta[2])])

        # 3. Create and output color image
        row, col = image.shape
        colored_image = np.zeros((row, col, 3))

        # 4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to
        for i in range(row):
            for j in range(col):
                for k in range(n_slices):
                    # interval[k] <= image[i][j] < interval[k+1]
                    if interval[k+1] > image[i][j] >= interval[k]:
                        colored_image[i][j][0] = red[0][k]
                        colored_image[i][j][1] = green[0][k]
                        colored_image[i][j][2] = blue[0][k]

        # returns colored image
        return colored_image
