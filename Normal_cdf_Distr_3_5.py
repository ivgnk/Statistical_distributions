'''
Вычисление вероятности по  функции распределения в нормальном распределении.
Пример из 2003_Надежность технических систем и техногенный риск_Ветошкин.pdf

стр.17, пример 3.5
Случайная величина X распределена по нормальному закону и представляет собой ошибку измерения датчика давления.
При измерении датчик имеет систематическую ошибку в сторону завышения на 0,5 МПа,
среднее квадратическое отклонение ошибки измерения составляет 0,2 МПа.
Найти вероятность  того, что отклонение измеряемого значения от истинного
не превзойдет по абсолютной величине 0,7 МПа.
'''

import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as sps
# Часть-1 ------------ Расчет
# loc - среднее, scale - стандартное отклонение, t_current - текущее значение
loc_=0.5; scale_=0.2
t_current1 = -0.7
t_current2 = +0.7

prob1 = sps.norm(loc=loc_, scale=scale_).cdf(t_current1)
prob2 = sps.norm(loc=loc_, scale=scale_).cdf(t_current2)
prob =prob2-prob1
print('prob1 = ',prob1)
print('prob2 = ',prob2)
print('Вероятность не превзойти = ',prob)
# 0.6997171101802624

# Часть-2 ------------ Визуализация результата
# xmin = 0;  xmax = loc_*2;   Npoints = 1000
# x = np.linspace(xmin, xmax, Npoints)
# plt.figure(figsize=(12, 5))
# xadd1= np.linspace(xmin, t_current1, Npoints)
# xadd2= np.linspace(xmin, t_current2, Npoints)
#
# y = sps.norm(loc=loc_, scale=scale_).cdf(x)
# yadd1 = sps.norm(loc=loc_, scale=scale_).cdf(xadd1)
# yadd2 = sps.norm(loc=loc_, scale=scale_).cdf(xadd2)
# # 1.1 чтобы график не касался рамки
# ymax = max(y)*1.1
# plt.plot(x, y, color = 'black')
# plt.grid(ls=':') # сетка из точек
# plt.xlabel('Значение', fontsize=18)
# plt.ylabel('Вероятность', fontsize=18)
# plt.title('Функция распределения N('+str(loc_)+','+str(scale_)+')', fontsize=20)
# plt.xlim((xmin, xmax)) # min и max по оси Х
# plt.ylim((None, ymax)) # min и max по оси Y
# plt.plot(xadd2, yadd2, color = 'blue')
# plt.plot(xadd1, yadd1, color = 'red')
# plt.show() # показ всей конструкции