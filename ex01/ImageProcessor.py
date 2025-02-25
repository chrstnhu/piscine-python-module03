from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

import os

# You must handle these errors: if the file passed as argument does not exist 
# or if it can’t be read as an image, with an appropriate message of your choice.

class ImageProcessor:
    def load(self, path):
        '''
        Opens the PNG file specified by the path argument
        Returns an array with the RGB values of the pixels in the image. 
        It must display a message specifying the dimensions of the image (e.g. 340 x 500).
        '''
        # Check if the file exists
        if not os.path.exists(path):
            print(f"Exception: FileNotFoundError -- strerror: No such file or directory")
            return None

        try:
            im = imread(path)
            img = np.array(Image.open(path)).astype(np.float32) / 255.0
            print (f"Loading image of dimensions {img.shape[0]} x {img.shape[1]}")
            return img
        except OSError as e:
            print ("Exception: OSError -- strerror: None")
            return None

    def display(self, array):
        '''
        Takes a numpy array as an argument and displays the corresponding RGB image.
        '''
        plt.imshow(array)
        plt.axis('off')
        plt.show()
