import bezier
import csv  # bezier.pyおよびモジュールcsvの読み込み
import numpy as np  # モジュールnumpyをnpという名前で読み込み
import scipy as sp  # モジュールscipyをspという名前で読み込み
from scipy import optimize  # scipy内のoptimizeモジュールを読み込み
from scipy import integrate  # scipy内のintegrateモジュールを読み込み


filename = 'input1'  # 制御点座標情報を格納した入力ファイル名
reader = csv.reader(open(filename + '.csv', 'r'))  # 入力ファイルの読み込み
next(reader)  # 先頭行は読み飛ばし
row = next(reader)[0:2]
n, m = int(row[0]), int(row[1])  # u,v方向の制御点数
next(reader)  # 1行読み飛ばし
cp = np.zeros([n, m, 3])
for i in range(n):
    for j in range(m):
        cpi = next(reader)[0:3]
        cp[i, j, :] = float(cpi[0]), float(cpi[1]), float(cpi[2])
limit = [np.min(cp), np.max(cp), np.min(cp), np.max(cp),
         np.min(cp), np.max(cp)]  # 描画範囲
bezier.plot_shape(n, m, cp, limit)


def f(x):  # 目的関数の定義
    global cp, n, m
    k = 0
    for i in range(n):
        for j in range(m):
            cp[i, j, 2] = x[k]  # 制御点座標の更新
            k += 1
    return integrate.nquad(lambda u, v: bezier.EGF(n, m, u, v, cp), [[0, 1], [0, 1]],
                           opts={'epsabs': 1.0e-6, 'epsrel': 1.0e-6})[0]  # 数値積分


k = 0
x = []  # 設計変数
b = []  # 設計変数の範囲の設定

for i in range(n):
    for j in range(m):
        x.append(cp[i, j, 2])
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            b.append([cp[i, j, 2], cp[i, j, 2]])  # 境界は動かさない
        else:
            b.append([-1.0e+10, 1.0e+10])
        k += 1

optimize.fmin_slsqp(f, x, fprime=None, bounds=b,
                    iprint=2, full_output=True)  # 逐次二次計画法
bezier.plot_shape(n, m, cp, limit)  # 結果の描画
