import numpy as np
import matplotlib.pyplot as plt
import numpy.random
import pandas as pd
x = np.linspace(0, 10, 200)

y = np.sin(5*x) / (1+x**2)

m1 = [1, 2, 3]

m2 = m1.copy()

print(x.shape)

print(y.shape)

plt.plot(x, y)

plt.show()

plt.plot(m1, m2, "go-", label="line1", linewidth=2)

plt.show()

plt.plot(x, y, linewidth=2, color='red')

plt.show()

plt.plot(x, y, linewidth=2, color='0.6')

plt.show()

plt.plot(x, y, linewidth=2, color='0')

plt.show()

x1 = range(20)
y1 = numpy.random.randn(20)

plt.plot(x1, y1, linewidth=2, marker='D')

plt.show()

plt.bar(list(range(1, 6)), numpy.random.randint(1, 30, 5))

plt.show()

plt.bar(numpy.arange(0.6, 5), numpy.random.randint(1, 30, 5))
plt.show()

plt.bar(numpy.arange(0.8, 5), numpy.random.randint(1, 30, 5))
plt.show()

arange = numpy.arange(1, 6)
plt.bar(arange - 0.4, numpy.random.randint(1, 15, 5), width=0.4, edgecolor='none', facecolor='blue')
plt.bar(arange, numpy.random.randint(1, 15, 5), width=0.4, edgecolor='none', facecolor='red')
plt.show()

A = numpy.random.randint(2, 15, 5)
B = numpy.random.randint(2, 15, 5)
C = numpy.random.randint(2, 15, 5)

plt.bar(arange, A, facecolor='green')
plt.bar(arange, B, facecolor='blue', bottom=A)
plt.bar(arange, C, facecolor='yellow', bottom=A + B)
plt.show()

plt.barh(arange, numpy.random.randint(1, 20, 5))
plt.show()

arange2 = numpy.arange(0.6, 6)
C = numpy.random.randint(2, 15, 6)
D = numpy.random.randint(2, 15, 6)
plt.barh(arange2, C, facecolor='red')
plt.barh(arange2, -D, facecolor='blue')
plt.show()

x = np.linspace(0, 10, 100)
plt.subplot(221)
plt.plot(x, np.sin(x), c='#e63946', lw=3)

plt.subplot(222)
plt.plot(x, np.sin(3*x), c='#7fb069', lw=3)

plt.subplot(223)
plt.scatter(x, np.random.randn(100), c='#daa73e', s=50, alpha=0.5)

plt.subplot(224)
plt.bar(range(10), np.random.randint(1, 30, 10), fc='#e55934')
plt.show()

x = np.linspace(0, 10, 100)

plt.subplot(231)
plt.plot(x, np.sin(x), c='#e63946', lw=3)

plt.subplot(232)
plt.plot(x, np.sin(3*x), c='#7fb069', lw=3)

plt.subplot(233)
plt.scatter(x, np.random.randn(100), c='#daa73e', s=50, alpha=0.5)

plt.subplot(234)
plt.bar(range(10), np.random.randint(1, 30, 10), fc='#e55934')

plt.subplot(235)
plt.plot(x, np.sin(x), c='#e63946', lw=3)

plt.subplot(236)
plt.plot(x, np.sin(3*x), c='#7fb069', lw=3)
plt.show()

plt.plot()



exit()




