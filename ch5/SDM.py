import numpy as np  # モジュールnumpyをnpという名前で読み込み
import csv  # モジュールcsvの読み込み
filename = 'out'  # 出力ファイル名
writer = csv.writer(open(filename + '.csv', 'w', newline=''))  # 出力するcsvファイルの生成
writer.writerow(['step', 'f(x)', 'x1', 'x2'])  # csvファイルへのラベルの書き込み


def f(x):  # 目的関数の定義
    return 0.50 * (x[0] - 3.0)**2 + (x[1] - 2.0)**2


def df(x):  # 勾配ベクトルの定義
    return np.array([x[0] - 3.0, 2.0 * (x[1] - 2.0)])


def line_search(xk):  # 2分法によりラインサーチを行う関数
    tau = 2.0
    xj1 = xk
    xj2 = xj1 - tau * df(xk)
    while abs(f(xj2) - f(xj1)) > eps:
        if f(xj2) < f(xj1):
            tau = tau
        else:
            tau = -tau / 2.0
        xj1 = xj2
        xj2 = xj1 - tau * df(xk)
    return xj1


x = [4.0, 3.0]  # 設計変数の初期値
t = 0.10  # τの初期値
itera = 1000  # 最適化の最大反復回数
eps = 1.0e-10  # 終了条件のための指定値
for k in range(itera):  # ここから最急降下法
    fx = f(x)
    writer.writerow([k, fx, x[0], x[1]])
    x_prev = x
    x = line_search(x)
    if abs(np.linalg.norm(x_prev - x)) < eps:
        break
