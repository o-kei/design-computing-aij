import numpy as np
import matplotlib.pyplot as plt


def bernstein(t, n, i):
    cn = 1.0
    ci = 1.0
    cni = 1.0
    for k in range(2, n, 1):
        cn = cn * k
    for k in range(1, i, 1):
        if i == 1:
            break
        ci = ci * k
    for k in range(1, n - i + 1, 1):
        if n == i:
            break
        cni = cni * k
    j = t**(i - 1) * (1 - t)**(n - i) * cn / (ci * cni)
    return j


def bezierplot(t, cp):
    n = len(cp)
    r = np.zeros([len(t), 2])
    for k in range(len(t)):
        sum1 = 0.0
        sum2 = 0.0
        for i in range(1, n + 1, 1):
            bt = bernstein(t[k], n, i)
            sum1 += cp[i - 1, 0] * bt
            sum2 += cp[i - 1, 1] * bt
        r[k, :] = [sum1, sum2]
    return np.array(r)

cp = np.array([[0, -2], [1, -3], [2, -2], [3, 2], [4, 2], [5, 0]])
t = np.arange(0, 1 + 0.01, 0.01)
p = bezierplot(t, cp)
plt.figure()
plt.plot(p[:, 0], p[:, 1])
plt.plot(cp[:, 0], cp[:, 1], ls=':', marker='o')
plt.show()
