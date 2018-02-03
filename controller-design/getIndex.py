import numpy as np
from numpy import *

def getIndex(omega,val):
    return argmin(np.absolute(np.subtract(omega,val)))

