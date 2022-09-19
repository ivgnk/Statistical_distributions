"""
Вычисления для пуассоновского распределения
Пример на основе https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html

The probability mass function for poisson is:
f(k) = exp(-m)*m^k/k!
The probability mass function above is defined in the “standardized” form.
To shift distribution use the loc parameter.
Specifically, poisson.pmf(k, mu, loc) is identically equivalent to poisson.pmf(k - loc, mu).
"""
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

################ Часть 1
# Расчет первых  четырех моментов
# mean, vart - среднее; дисперсия;
# skew, kurt - показатель асимметрии (скошенности), скос;  показателя эксцесса (островершинности)

mu = 0.6
mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
print('mean, var, skew, kurt =', mean, var, skew, kurt)

################ Часть 2 - Display the probability mass function (pmf):
# 1 тип задания распределения - массивом
x = np.array([0, 1, 2, 3])
print('x \n'); print(x)

plt.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')  # синяя точка
plt.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)  # синяя вертик.линия

# 2 тип задания распределения - отдельными значениями
# Alternatively, the distribution object can be called (as a function) to fix the shape and location.
# This returns a “frozen” RV object holding the given parameters fixed.
rv = poisson(mu)
plt.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='frozen pmf')
plt.legend(loc='best', frameon=False)
plt.show()
