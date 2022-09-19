"""
Вычисления для логнормального распределения
Пример на основе https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lognorm.html

s - стандартное отклонение
x - набор значениq, для которых расчитывается
loc - среднее, по умолчанию 0
scale - шкалирование, по умолчанию 1
"""
from scipy.stats import lognorm
import numpy as np
import matplotlib.pyplot as plt

################ Часть 1
# Расчет первых  четырех моментов
# mean, vart - среднее; дисперсия;
# skew, kurt - показатель асимметрии (скошенности), скос;  показателя эксцесса (островершинности)
s = 0.954   # стандартное отклонение для расчета моментов
# Расчет аргумента функции плотности  linspace(start, stop, num)
x = np.linspace(0.1, 5, 100)  # x = np.linspace(lognorm.ppf(0.01, s), lognorm.ppf(0.99, s), 100)
print(x)

mean, var, skew, kurt = lognorm.stats(s, moments='mvsk')
print('mean, var, skew, kurt =' , mean, var, skew, kurt)

################ Часть 2
# значения по умолчанию для расчета далее
# loc_ - сдвиг,   scale_ - шкалирование
loc_=0; scale_=1  # по умолчанию в функции pdf
s1 = [0.01, 0.05, 0.1, 0.15, 0.15] # станд. отклонения для расчета графиков

plt.figure(figsize=(6, 5))  # размер окна
plt.grid(ls=':') # сетка из точек
# 'r-' - цвет и тип линии;    lw - толщина;  alpha - прозрачность
color_ = ['c-','m-','y-','k-'] # список цветов для рисования графика
plt.title('Графики плотнотности логнормальных распределений \n с разными стандартнымм отклонениями')
for i in range(len(color_)):
    plt.plot(x, lognorm.pdf(x, s1[i], loc=loc_, scale=scale_), color_[i], lw=2, alpha=1, label=color_[i]+str(s1[i]))
plt.legend(loc='upper right')
plt.show() # показ всей конструкции

#
# xmin = -3+loc_;  xmax = 3+loc_;   Npoints = 100
# x = np.linspace(xmin, xmax, Npoints)
# plt.figure(figsize=(12, 5))
#
# y = sps.norm.pdf(x,  loc=loc_, scale=scale_)
# # 1.1 чтобы график не касался рамки
# ymax = max(y)*1.1
#
# plt.plot(x, y)
# plt.grid(ls=':') # сетка из точек
# plt.xlabel('Значение', fontsize=18)
# plt.ylabel('Плотность', fontsize=18)
# plt.title('Плотность N('+str(loc_)+','+str(scale_)+')', fontsize=20)
# plt.xlim((xmin, xmax)) # min и max по оси Х
# plt.ylim((None, ymax)) # min и max по оси Y

