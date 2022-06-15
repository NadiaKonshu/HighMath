# 2. Задание (на листочке)
# Почему прямые не кажутся перпендикулярными?


import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import warnings

warnings.filterwarnings('ignore')

x = np.linspace(-5, 5, 21)
y = 3*x+1
y2 = (-1/3)*x+1
plt.plot(x,y)
plt.plot(x, y2)
plt.xlabel('x')
plt.ylabel('y')

plt.figure(figsize = (5, 5))
x = np.linspace(-15, 15)
y = 3*x+1
y2 = (-1/3)*x+1
plt.plot(x,y)
plt.plot(x, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.show()