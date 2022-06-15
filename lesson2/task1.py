# 1. Задание
# Даны два вектора в трехмерном пространстве: (10,10,10) и (0,0,-10)
# Найдите их сумму. (на листочке)
# Напишите код на Python, реализующий расчет длины вектора, заданного его координатами. (в программе)

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import warnings

warnings.filterwarnings('ignore')

x = 2
y = 4
lenth_vec = np.sqrt(x ** 2 + y **2)
print('Длина вектора равна', lenth_vec)