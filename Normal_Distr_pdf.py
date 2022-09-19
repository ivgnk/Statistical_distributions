'''
Вычисление и построение кривой плотности нормального распределения.
Пример из https://mipt-stats.gitlab.io/courses/python/07_scipy_stats.html
'''
import scipy.stats as sps
import numpy as np
import matplotlib.pyplot as plt


# loc - среднее, scale - стандартное отклонение
loc_=1; scale_=1
xmin = -3+loc_;  xmax = 3+loc_;   Npoints = 100
x = np.linspace(xmin, xmax, Npoints)
plt.figure(figsize=(12, 5))

y = sps.norm.pdf(x,  loc=loc_, scale=scale_)
# 1.1 чтобы график не касался рамки
ymax = max(y)*1.1

plt.plot(x, y)
plt.grid(ls=':') # сетка из точек
plt.xlabel('Значение', fontsize=18)
plt.ylabel('Плотность', fontsize=18)
plt.title('Плотность N('+str(loc_)+','+str(scale_)+')', fontsize=20)
plt.xlim((xmin, xmax)) # min и max по оси Х
plt.ylim((None, ymax)) # min и max по оси Y
plt.show() # показ всей конструкции
