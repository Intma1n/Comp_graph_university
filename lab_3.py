import numpy as np
import matplotlib.pyplot as plt

def my_3d_function(x, y):
    f = np.cos(x * y) * np.cos(np.sqrt(x ** 2 * y ** 2))
    return f