import numpy as np
from collections.abc import Iterable

# BONUS: Add to these methods an optional argument which specifies the datatype
# (dtype) of the array (e.g. to represent its elements as integers, floats, ...)

class NumpyCreator:
    def from_list(self, lst):
        '''
        Takes a list or nested lists
        Returns its corresponding Numpy array
        '''
        if isinstance(lst, list) and all(len(lst[0]) == len(i) for i in lst):
            arr = np.array(lst)
            return arr
        else:
            return None

    def from_tuple(self, tpl): 
        '''
        Takes a tuple or nested tuples
        Returns its corresponding Numpy array
        '''
        if isinstance(tpl, tuple) and all(len(tpl[0]) == len(i) for i in tpl):
            arr = np.asarray(tpl)
            return arr if arr.ndim == 1 else None
        return None
    
    def from_iterable(self, itr):
        '''
        Takes an iterable
        Returns an array which contains all of its elements
        '''
        if isinstance(itr, Iterable):
            arr = np.fromiter(itr, dtype = int)
            return arr
        return None
    
    def from_shape(self, shape, value = 0): 
        '''
        Returns an array filled with the same value.
        The first argument is a tuple which specifies the shape of the array, 
        and the second argument specifies the value of the elements
        This value must be 0 by default
        '''
        if isinstance(shape, tuple):
            arr = np.full(shape, value)
            return arr
        return None

    
    def random(self, shape): 
        '''
        Returns an array filled with random values. 
        It takes as an argument a tuple which specifies the shape of the array
        '''
        if isinstance(shape, tuple):
            arr = np.random.rand(*shape)
            return arr

    def identity(self, n): 
        '''
        Returns an array representing the identity matrix of size n
        '''
        return np.identity(n)