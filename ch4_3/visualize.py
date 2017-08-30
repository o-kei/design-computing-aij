import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plotter(data, lambd, mu, capacity):
    x1 = [tup[0] for tup in data]  # 時刻
    y1 = [tup[2] for tup in data]  # 待ち人数
    y2 = [tup[1]/capacity for tup in data]  # 利用率
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.bar(x1, y1, color='gray', label='queue length')
    ax1.set_title(r'Queueing Simulation, $\lambda=%4.2f, \mu=%4.2f, c=%d$' %
                  (lambd, mu, capacity))
    ax1.set_xlabel('steps')
    ax1.set_ylabel('queue length')
    ax2 = ax1.twinx()  # x軸を関連付ける
    ax2.plot(x1, y2, c='k', ls='-', label='simulated UR')
    ax2.axhline(y=np.mean(y2), c='k', ls='--', label='mean of simulated UR')
    ax2.axhline(
        y=lambd/(mu*capacity), c='k', ls=':', lw=2, label='theoretical UR')
    ax2.set_ylabel('utilization ratio (UR)')
    plt.legend(loc='best')
    plt.show()


def animation(data, lambd, mu, capacity, until):
    fig = plt.figure()
    ani = FuncAnimation(fig, update, fargs=(data,), interval=100, frames=until)
    plt.show()


def update(i, data):
    tup = data[i]
    y0 = 0.0
    x1 = np.arange(1, tup[2] + 1)  # 行列人数
    y1 = np.ones(x1.shape) * y0
    x2 = np.arange(-1, -tup[1] - 1, -1)  # 使用人数
    y2 = np.ones(x2.shape) * y0
    plt.cla()
    plt.xlim([-10, 10])
    plt.ylim([-1, 1])
    plt.yticks([])
    plt.title('Users and Queue: time=%03d' % tup[0])
    plt.xlabel('people num')
    plt.scatter(x1, y1, c='white', s=80, label='queueing:%d' % tup[2])
    plt.scatter(x2, y2, c='black', s=80, label='using:%d' % tup[1])
    plt.legend(loc='best')
