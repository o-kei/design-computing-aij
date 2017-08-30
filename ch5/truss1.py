import numpy as np  # モジュールnumpyをnpという名前で読み込み
import csv  # モジュールcsvの読み込み
from scipy import optimize  # scipy内のoptimizeモジュールを読み込み
filename = 'out3'  # 出力ファイル名
writer = csv.writer(open(filename + '.csv', 'w'))  # 出力するcsvファイルの生成
writer.writerow(['step', 'F(A)[mm3]', 'A1[mm2]', 'A2[mm2]',
                 'sigma1[N/mm2]', 'sigma2[N/mm2]', 'U2[mm]'])  # csvファイルへのラベルの書き込み
E = 205000.0  # 各種力学量の設定
L = 2.0 * 1.0e+3
P1 = 400.0 * 1.0e+3
P2 = 200.0 * 1.0e+3
sigma_bar = 235.0
u_bar = 5.0
a1 = L * 1.0
a2 = L * 1.0
A = np.array([3000.0, 3000.0])  # 断面積の初期値


def f(A):  # 目的関数の定義
    return a1 * A[0] + a2 * A[1]


def g(A):  # 制約条件の定義
    sigma1 = sigma_bar - (P1 + P2) / A[0]
    sigma2 = sigma_bar - P2 / A[1]
    u2 = u_bar - (P1 + P2) * L / A[0] / E - P2 * L / A[1] / E
    return np.array([sigma1, sigma2, u2, A[0], A[1]])


def callbackF(A):  # 最適化の各ステップで呼び出される関数
    global step
    step += 1
    cons = g(A)
    writer.writerow([step, f(A), A[0], A[1], sigma_bar - cons[0],
                     sigma_bar - cons[1], u_bar - cons[2]])


step = 0
cons = g(A)
writer.writerow([step, f(A), A[0], A[1], sigma_bar - cons[0], sigma_bar - cons[1],
                 u_bar - cons[2]])
optimize.fmin_slsqp(f, A, f_ieqcons=g, iprint=2,
                    callback=callbackF, iter=10000)  # 逐次2次計画法
