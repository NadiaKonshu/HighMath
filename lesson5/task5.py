# Дополните код расчетом коэффициента корреляции x и y по формуле:
# R = sum((xi - xm)(yi - ym))/sqr(sum((xi - xm) 2) * (sum((yi - ym) 2)))
import numpy as np
import itertools
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

np.warnings.filterwarnings('ignore')
n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
c = np.corrcoef(x, y)

print(a, b)
print(a1, b1)
print(c)
plt.plot([0, 1], [b, a + b])
plt.show()