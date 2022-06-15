# 3.
# построение
# графиков:


# окружности
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import warnings

warnings.filterwarnings('ignore')

x = []
x2 = []
y = []
y2 = []
for i in range(1300):
    r = 800
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(r ** 2 - i ** 2))
    y2.append(-np.sqrt(r ** 2 - i ** 2))
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='r')
plt.plot(x, y2, color='r')
plt.plot(x2, y2, color='r')
plt.plot(x2, y, color='r')
plt.axis('scaled')
plt.show()


# эллипса
x = []
x2 = []
y = []
y2 = []
for i in range(1500):
    a = 50
    b = 30
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))
plt.plot(x, y, color='r')
plt.plot(x, y2, color='r')
plt.plot(x2, y2, color='r')
plt.plot(x2, y, color='r')
plt.axis('scaled')
plt.show()

# гиперболы.
x = []
x2 = []
y = []
y2 = []
for i in range(1200):
    a = 500
    b = 300
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))
plt.plot(x, y, color='r')
plt.plot(x, y2, color='r')
plt.plot(x2, y2, color='r')
plt.plot(x2, y, color='r')
plt.axis('scaled')
plt.show()