from PIL import Image  # Export image
import numpy as np
import matplotlib.pyplot as plt

# Manipulation of loaded image via numpy arrays, broadcasting.

class ColorFilter:
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.

        ◦ Authorized functions: .copy.
        ◦ Authorized operators: +,-,=.
        """
        # Check if the array is valid
        if array is None or len(array.shape) != 3 or array.shape[2] != 3:
            return None

        # Copy the array
        image = array.copy()

        # Invert the image
        if image.dtype == np.float32:
            image = 1.0 - image
        else:
            image = 255 - image

        return image


    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        
        ◦ Authorized functions: .copy, .zeros,.shape,.dstack.
        ◦ Authorized operators: =.
        """
        # Check if the array is valid
        if array is None or len(array.shape) != 3 or array.shape[2] != 3:
            return None

        # Copy the array
        image = array.copy()

        im_R = np.zeros(array.shape[:2], dtype=np.uint8)
        im_G = np.zeros(array.shape[:2], dtype=np.uint8)
        im_B = array[:, :, 2]

        # Color to blue
        image = np.dstack((im_R, im_G, im_B))

        return image

    def to_green(self, array):
        '''
        Takes a numpy array as an argument and returns an array where the red and blue channels are set to 0.
        '''
        # Check if the array is valid
        if array is None or len(array.shape) != 3 or array.shape[2] != 3:
            return None

        # Copy the array
        image = array.copy()

        im_R = np.zeros(array.shape[:2], dtype=np.uint8)
        im_G = array[:, :, 1]
        im_B = np.zeros(array.shape[:2], dtype=np.uint8)

        # Color to blue
        image = np.dstack((im_R, im_G, im_B))

        return image


    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        
        ◦ Authorized functions: .copy, .to_green,.to_blue.
        ◦ Authorized operators: -,+, =
        """
        # Check if the array is valid
        if array is None or len(array.shape) != 3 or array.shape[2] != 3:
            return None

        # Copy the array
        image = array.copy()

        im_R = array[:, :, 0]
        im_G = np.zeros(array.shape[:2], dtype=np.uint8)
        im_B = np.zeros(array.shape[:2], dtype=np.uint8)

        # Color to blue
        image = np.dstack((im_R, im_G, im_B))

        return image

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.

        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        
        ◦ Authorized functions: .copy, .arange,.linspace, .min, .max.
        ◦ Authorized operators: =, <=, >, & (or and).
        """
        # Check if the array is valid
        if array is None or len(array.shape) != 3 or array.shape[2] != 3:
            return None

        # Copy the array
        image = array.copy()

        # Define the thresholds
        thresholds = np.linspace(np.min(array), np.max(array), num=5)

        # Apply the filter
        for i in range(4):
            image[(array >= thresholds[i]) & (array < thresholds[i + 1])] = thresholds[i]

        return image


    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
            weights: [kwargs] 3 floats where the sum equals to 1,
                    corresponding to the weights of each RBG channels.
                    Expecting keys: ’r_weight’, ’g_weight’ and ’b_weight’.
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        
        ◦ Authorized functions: .sum,.shape,.reshape,.broadcast_to,.as_type.
        ◦ Authorized operators: *,/, =.
        """

        # Check if the array is valid
        if array is None or len(array.shape) != 3 or array.shape[2] != 3:
            return None

        # Copy the array
        image = array.copy()

        # Determine the filter
        if filter in ['m', 'mean']:
            # Sum the RGB values and divide by 3 to get the mean
            grayscale = image.sum(axis=2) / 3
        elif filter in ['w', 'weight']:
            # Ensure the weights are provided and sum to 1
            r_weight = kwargs.get('r_weight', 0)
            g_weight = kwargs.get('g_weight', 0)
            b_weight = kwargs.get('b_weight', 0)

            # print(r_weight, g_weight, b_weight)
            if r_weight + g_weight + b_weight != 1:
                return None
            
            # Calculate the weighted mean
            grayscale = (r_weight * image[:, :, 0] +
                     g_weight * image[:, :, 1] +
                     b_weight * image[:, :, 2])
        else :
            return None
        
        grayscale = grayscale.reshape((grayscale.shape[0], grayscale.shape[1], 1))
        grayscale = np.broadcast_to(grayscale, (grayscale.shape[0], grayscale.shape[1], 3))
        
        image = grayscale.astype(array.dtype)

        return image