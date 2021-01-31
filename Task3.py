#Задание 3
#Найдите скалярное произведение столбцов массива a_centered.
# В результате должна получиться величина a_centered_sp.
# Затем поделите a_centered_sp на N-1, где N - число наблюдений.

import numpy as np
a = np.array([
            [1, 6],
            [2, 8],
            [3, 11],
            [3, 10],
            [1, 7]])
res1 = a.mean(axis=0)
mean_a = np.array([res1[0], res1[1]])

a_centered = a - mean_a

x1 = np.squeeze(a_centered[:,:1])
x2 = np.squeeze(a_centered[:,1:])
a_centered_sp = np.dot(x1,x2)
result = a_centered_sp / (a.shape[0] - 1)
print(result)