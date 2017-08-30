import numpy as np  # モジュールnumpyをnpという名前で読み込み
from numba.decorators import jit  # just-in timeコンパイラの読み込み#
import matplotlib.pyplot as plt  # モジュールmatplotlibのpyplot関数を
# pltという名前で読み込み
from mpl_toolkits.mplot3d import Axes3D  # matplotlibの3次元モジュール
from mpl_toolkits.mplot3d import proj3d  # matplotlibの3次元モジュール


@jit
def bernstein(t, n, i):  # bernstein既定関数の定義
    cn, ci, cni = 1.0, 1.0, 1.0
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


@jit
def d_bern(t, n, i):  # bernstein既定関数の微分の定義
    cn, ci, cni = 1.0, 1.0, 1.0
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
    j = t**(i - 2) * (1 - t)**(n - i - 1) * cn * \
        ((1 - n) * t + i - 1) / (ci * cni)
    return j


@jit
def bezierplot(n, m, u, v, cp):  # bezier曲面の定義
    xyz = np.zeros([len(u), len(v), 3])
    for k in range(len(u)):
        for l in range(len(v)):
            for i in range(n):
                bu = bernstein(u[k], n, i + 1)
                for j in range(m):
                    bv = bernstein(v[l], m, j + 1)
                    xyz[k, l, :] += cp[i, j, :] * bu * bv
    return xyz


@jit
def EGF(n, m, u, v, cp):  # bezier曲面の面積を求める関数
    z1, z2 = np.zeros(3), np.zeros(3)
    for i in range(n):
        bu, dbu = bernstein(u, n, i + 1), d_bern(u, n, i + 1)
        for j in range(m):
            bv, dbv = bernstein(v, m, j + 1), d_bern(v, m, j + 1)
            z1 += cp[i, j, :] * dbu * bv
            z2 += cp[i, j, :] * bu * dbv
    E, G, F = z1.dot(z1), z2.dot(z2), z1.dot(z2)
    return (abs(E * G - F**2))**0.5


def orthogonal_transformation(zfront, zback):  # 曲面の描画を
    a, b, c = 2 / (zfront - zback), -1 * (zfront + zback) / \
        (zfront - zback), zback
    return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, a, b], [0, 0, 0, c]])


def plot_shape(n, m, cp, limit):  # bezier曲面を描画する関数
    proj3d.persp_transformation = orthogonal_transformation
    u, v = np.arange(0, 1 + 0.1, 0.1), np.arange(0, 1 + 0.1, 0.1)  # パラメータ生成
    s = bezierplot(n, m, u, v, cp)  # bezier曲面生成
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_axis_off()
    ax.set_aspect('equal')
    ax.set_xlim(limit[0], limit[1])
    ax.set_ylim(limit[2], limit[3])
    ax.set_zlim(limit[4], limit[5])
    ax.plot_surface(s[:, :, 0], s[:, :, 1], s[:, :, 2],
                    rstride=1, cstride=1, color='yellow')  # bezier曲面の描画
    ax.plot_wireframe(cp[:, :, 0], cp[:, :, 1], cp[:, :, 2],
                      color='red', linestyle='dashed')  # 制御多面体描画
    ax.scatter3D(cp[:, :, 0], cp[:, :, 1], cp[
                 :, :, 2], c='green', s=25)  # 制御点の描画
    plt.show()
