
import sys
import matplotlib
import matplotlib.pyplot as plt

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, randomly pick n centroids from the dataset.
        Args:
        -----
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
            None.
        Raises:
        -------
            This function should not raise any Exception.
        """
        # ... write code ...

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
            This function should not raise any Exception.
        """
        # ... write code ...

