import matplotlib.pyplot as plt
import numpy as np

class GenericRBF(object):
    def __call__(self):
        raise NotImplementedError

    def plot(self, a=0, b=1):
        x=np.linspace(a,b,1024)
        plt.figure()
        plt.plot(x,self(x))
        plt.show()
