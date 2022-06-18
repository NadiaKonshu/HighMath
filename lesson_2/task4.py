
# 4. Задание (на листочке)
# 1) Пусть задана плоскость:
#
# Напишите уравнение плоскости, параллельной данной и проходящей через начало координат.
# 2)  Пусть задана плоскость: A1x + B1y + C1z + D1 = 0
# и прямая:
#
# Как узнать, принадлежит прямая плоскости или нет?

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import warnings

warnings.filterwarnings('ignore')
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure(figsize = (8, 8))
ax = Axes3D(fig)
x = np.arange(-15, 15, 2)
y = np.arange(-15, 15, 2)
x, y = np.meshgrid(x, y)
z = 2 * x + 3 * y + 204
z2 = 2 * x + 3 * y
ax.plot_wireframe(x, y, z, label='Ax + By + Cz + D = 0', linestyle='--', linewidth=1)
ax.plot_wireframe(x, y, z2, colors='green', label='Ax + By + Cz + D = 0')
ax.scatter(0, 0, 0, 'z', 50, 'red', label='Координата: 0; 0')
plt.legend(frameon=False)
plt.show()