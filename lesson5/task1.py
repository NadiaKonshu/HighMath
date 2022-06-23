# Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро).

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

np.random.randint(0, 36)

for i in range(0, 5):
    a = int(input())
    num = np.random.uniform(0, 36)
    if num == 0:
      print("green")
    elif num < 50:
        print("red")
    else:
        print("black")


