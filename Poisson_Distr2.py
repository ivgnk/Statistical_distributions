"""
Вычисления для пуассоновского распределения
Пример на основе https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html

Вычисляем функцию распределения poisson.cdf = Г(k+1, mu)/k!
и сравниваем с графиками из  https://ru.wikipedia.org/wiki/Распределение_Пуассона
"""
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

# Часть 1- расчет вероятностей с разными mu
mu_lst = [1, 4, 10]; x_lst = [i for i in range(0, 21)]; colors = ['r', 'g', 'k']
x = np.array(x_lst)
for i in range(len(mu_lst)):
    prob = poisson.cdf(x, mu_lst[i])
    plt.plot(x, poisson.pmf(x, mu_lst[i]), colors[i], label='mu='+str(mu_lst[i]))
    #print(mu_lst[i])  print(prob)   # просмотр результата в текстовом виде
plt.grid(ls=':') # сетка из точек
plt.title('Графики poisson.cdf(x, mu)')
plt.legend(loc='best', frameon=False)
plt.show()

r = poisson.rvs(mu_lst[0], size=1000)
print(r)
