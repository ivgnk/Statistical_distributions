"""
Вычисления для логнормального распределения с разными сдигами
Пример на основе https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lognorm.html

s - стандартное отклонение
x - набор значениq, для которых расчитывается
loc - среднее, по умолчанию 0
scale - шкалирование, по умолчанию 1
"""
from scipy.stats import lognorm
import numpy as np
import matplotlib.pyplot as plt

# Расчет аргумента функции плотности  linspace(start, stop, num)
x = np.linspace(0.1, 5, 100)
print(x)

# loc_ - сдвиг,   scale_ - шкалирование
scale_ = 1
s = 0.2  # станд. отклонение для расчета графиков
loc_n = [0, 1, 2, 3]  # список сдвигов для которых строим график

plt.figure(figsize=(6, 5))  # размер окна
plt.grid(ls=':')  # сетка из точек
# 'r-' - цвет и тип линии;    lw - толщина;  alpha - прозрачность
color_ = ['c-', 'm-', 'y-', 'k-']  # список цветов для рисования графика
plt.title('Графики плотнотности логнормальных распределений \n с разными сдвигами')
for i in range(len(color_)):
    plt.plot(x, lognorm.pdf(x, s, loc=loc_n[i], scale=scale_), color_[i], lw=2, alpha=1, label=color_[i]+str(loc_n[i]))
plt.legend(loc='upper right')
plt.show()  # показ всей конструкции
