# 1. Задание (в программе) y= k*cos(x-a)+b
# Нарисуйте график функции:   для некоторых (2-3 различных) значений параметров k, a, b

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import warnings

warnings.filterwarnings('ignore')

x = np.linspace(-2 * np.pi, 3 * np.pi, 101)
k, a, b = np.linspace(4, 12, num=3)
k1, a1, b1 = np.linspace(12, 22, num=3)
k2, a2, b2 = np.linspace(11, 20, num=3)
print(f'k = {k}, a = {a}, b = {b}')
print(f'k1 = {k1}, a1 = {a1}, b1 = {b1}')
print(f'k2 = {k2}, a2 = {a2}, b2 = {b2}')
plt.figure(figsize=(20, 8))
plt.plot(x, k * np.cos(x-a) + b, label='k, a, b')
plt.plot(x, k1 * np.cos(x-a1) + b1, color='g', label='k1, a1, b1')
plt.plot(x, k2 * np.cos(x-a2) + b2, color='r', label='k2, a2, b2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend(frameon=False)
plt.show()
