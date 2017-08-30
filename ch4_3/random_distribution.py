# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as npr
import matplotlib.pylab as plt

RANDOM_SEED = 1  # random seed
SIZE = 10000  # 試行回数
EXPECTED_V = 5  # 期待値


def x_uniform():
    # 一様分布
    # aからbまで一様の確率のときその間のxを返す。
    a = 0
    b = EXPECTED_V * 2 - a
    return npr.uniform(a, b, SIZE)


def x_poisson():
    # ポアソン分布
    # 単位時間あたりλ回起こる事象がちょうどk回発生するときのkを返す
    lambd = EXPECTED_V  # 期待値=λとなる
    return npr.poisson(lambd, size=SIZE)


def x_exponential():
    # 指数分布
    # 単位時間当たり平均λ回起こる事象＝平均1/λ時間で1回発生する事象の発生間隔がt時間であるときのtを返す
    # 平均余命など。
    lambd = 1.0 / EXPECTED_V  # 1分あたりlambd回発生する。= 平均1/lambd時間の間隔で1回発生
    return npr.exponential(1. / lambd, size=SIZE)  # 発生間隔をランダムに返す


def x_erlang():
    # アーラン分布
    # アーラン分布はガンマ分布の形状母数kを正整数に限定したもの
    k = 3
    lambd = k / EXPECTED_V  # 期待値 = k/λとなる。
    return npr.gamma(k, 1. / lambd, size=SIZE)


def histogram(x_distribution, ax, title="histogram"):
    mean = np.mean(x_distribution)
    print("%s: mean:%f" % (title, mean))
    bins = np.arange(np.floor(np.amin(x_distribution)),
                     np.ceil(np.amax(x_distribution)) + 1.0, 1.)
    n, bins, patches = ax.hist(
        x_distribution, bins=bins, align='left', normed=1, color="gray")

    ax.set_title(title, fontsize=14)
    ax.set_xlabel('value')
    ax.set_ylabel('frequency / N')


if __name__ == '__main__':
    npr.seed(RANDOM_SEED)
    fig = plt.figure()
    fig.suptitle('Histogram: N=%d, E=%-4.2f' % (SIZE, EXPECTED_V), fontsize=16)
    fig.subplots_adjust(left=None, bottom=None, right=None,
                        top=None, wspace=0.3, hspace=0.4)

    ax1 = fig.add_subplot(221)
    histogram(x_uniform(), ax1, title="uniform")

    ax2 = fig.add_subplot(222)
    histogram(x_poisson(), ax2, title="poisson")

    ax3 = fig.add_subplot(223)
    histogram(x_exponential(), ax3, title="exponential")

    ax4 = fig.add_subplot(224)
    histogram(x_erlang(), ax4, title="erlang(k=3)")

    plt.show()
