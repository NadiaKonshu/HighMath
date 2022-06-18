
# 5. Задание (в программе)
# Нарисуйте трехмерный график двух параллельных плоскостей.

# import numpy as np
# import matplotlib.pyplot as plt
# from pylab import *
# from mpl_toolkits.mplot3d import Axes3D
# import warnings
#
# warnings.filterwarnings('ignore')
#
# fig = figure(figsize=(8, 8))
# ax = Axes3D(fig)
# x = np.arange(-15, 15, 2)
# y = np.arange(-15, 15, 2)
# x, y = meshgrid(x, y)
# z = 9 * x + 204
# z2 = 9 * x +10
# ax.plot_wireframe(x, y, z, linestyle='--', linewidth=1)
# ax.plot_wireframe(x, y, z2, colors='green')
# plt.show()

# Нарисуйте трехмерный график двух любых поверхностей второго порядка.
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import warnings

fig = figure(figsize=(18, 18))
ax = Axes3D(fig)
a = 20
b = 90
x, y = np.meshgrid((np.arange(-15, 15, 2)), (np.arange(-15, 15, 2)))
z = b ** 2 + (b ** 2 * (x ** 2 / a ** 2))
z1 = -(b ** 2 + (b ** 2 * (x ** 2 / a ** 2)))
z2 = 2 * a * x ** np.cos(40) * np.sqrt(2 * a * x ** np.cos(40))
ax.plot_surface(x, y, z, linewidth=1, color='g')
ax.plot_surface(x, y, z1, linewidth=1, color='g')
u = np.linspace(0.2 * np.pi, 32)
v = np.linspace(0, np.pi, 16)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 50 * np.outer(np.sin(u), np.sin(v))
z = -100 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, rstride=4, cstride=4, color='r')
plt.show()
