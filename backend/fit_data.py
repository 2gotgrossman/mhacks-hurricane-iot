import numpy as np
import matplotlib.pyplot as plt

s = """1,76,73
2,74,77
3,75,69
4,74,72
5,72,76
6,71,79
7,70,83
8,73,79
9,77,70
10,81,62
11,85,54
12,87,49
13,89,45
14,90,43
15,90,41
16,90,40
17,89,41
18,89,42
19,85,51
20,82,58
21,80,61
22,79,65
23,78,68
24,77,70"""

lines = s.split()
time = []
temp = []
humidity = []

for line in lines:
    vals = line.split(',')
    vals = map(int, vals)
    time.append(vals[0])
    temp.append(vals[1])
    humidity.append(vals[2])


# calculate polynomial

def fit_and_plot(x, y):
    z = np.polyfit(x, y, 4)
    f = np.poly1d(z)
    print z
    print f

    # calculate new x's and y's
    x_new = np.linspace(x[0], x[-1], 50)
    y_new = f(x_new)

    plt.plot(x,y,'o', x_new, y_new)
    plt.xlim([x[0]-1, x[-1] + 1 ])
    plt.show()

fit_and_plot(time, temp)
fit_and_plot(time, humidity)
