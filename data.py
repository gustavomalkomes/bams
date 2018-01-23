''' Classes for handling data'''

import numpy as np
import matplotlib.pyplot as plt
from interfaces import Data


class VectorData(Data):

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def update(self, x, y):
        if self.x is None:
            self.x, self.y = x, y
        else:
            self.x = np.vstack((self.x, x))
            self.y = np.vstack((self.y, y))

    def plot(self):
        plt.scatter(self.x, self.y)
        # (predictions, uncertainty) = self.predict(x)
        # plt.scatter(x, predictions)
        plt.show()

    def __repr__(self):
        if self.x is None:
            return 'x : [] and y : []'
        else:
            return '{}'.format(np.hstack((self.x, self.y)))
