# Дополните код Монте-Карло последовательности независимых испытаний расчетом соответствующих вероятностей (через биномиальное распределение)
# и сравните результаты.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

k = 0
n = 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
print(k, n, k/n)
P = 6 / 2**4
print(P)

# Повторите расчеты биномиальных коэффициентов и вероятностей k успехов в последовательности из n независимых испытаний, взяв другие значения n и k.

k = 0
n = 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
x = a + b + c + d + e
for i in range(0, n):
    if x[i] == 3:
        k = k + 1
print(k, n, k/n)

C_5_3 = 5*4*3*2 / (3*2*2)
P_5_3 = C_5_3 / 2**5
P_5_3