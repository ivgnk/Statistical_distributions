'''
Вычисление вероятности по  функции распределения в нормальном распределении.
Пример из 2003_Надежность технических систем и техногенный риск_Ветошкин.pdf

стр.17, пример 3.3
Определить вероятность безотказной работы в течение
t = 20 000 ч подшипника скольжения, если ресурс по износу
подчиняется нормальному закону распределения с параметрами
среднее Mt = 40 000 ч, стандартное отклонение σ = 10 000 ч.
'''
import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as sps
# Часть-1 ------------ Расчет
# loc - среднее, scale - стандартное отклонение, t_current - текущее время
loc_=40_000; scale_=10_000
t_current = 20_000

prob = sps.norm(loc=loc_, scale=scale_).cdf(t_current)
print('Вероятность отказа и безотказной работы = ',prob, 1-prob)
# 0.022750131948179195 0.9772498680518208

# Часть-2 ------------ Визуализация результата
xmin = 0;  xmax = loc_*2;   Npoints = 1000
x = np.linspace(xmin, xmax, Npoints)
plt.figure(figsize=(12, 5))
xadd= np.linspace(xmin, t_current, Npoints)

y = sps.norm(loc=loc_, scale=scale_).cdf(x)
yadd = sps.norm(loc=loc_, scale=scale_).cdf(xadd)
# 1.1 чтобы график не касался рамки
ymax = max(y)*1.1

plt.plot(x, y, color = 'black')
plt.grid(ls=':') # сетка из точек
plt.xlabel('Значение', fontsize=18)
plt.ylabel('Вероятность', fontsize=18)
plt.title('Функция распределения N('+str(loc_)+','+str(scale_)+')', fontsize=20)
plt.xlim((xmin, xmax)) # min и max по оси Х
plt.ylim((None, ymax)) # min и max по оси Y
plt.plot(xadd, yadd, color = 'red')

plt.show() # показ всей конструкции