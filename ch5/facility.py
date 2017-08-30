import numpy as np  # モジュールnumpyをnpという名前で読み込み
import csv  # モジュールcsvの読み込み
from scipy import optimize  # scipy内のoptimizeモジュールを読み込み
filename = 'out2'  # 出力ファイル名
writer = csv.writer(open(filename + '.csv', 'w', newline=''))  # 出力するcsvファイルの生成
writer.writerow(['step', 'f(x)', 'x1', 'x2'])  # csvファイルへのラベルの書き込み


def f(x):  # 目的関数の定義
    return ((2 - x[0])**2 + (4 - x[1])**2)**0.5 + ((3 - x[0])**2 + (2 - x[1])**2)**0.5


def g(x):  # 制約条件の定義(>0)
    return np.array([-2 * x[0] - 3 * x[1] + 7, x[0], -x[0] + 2, x[1], -x[1] + 2])


def callbackF(x):  # 最適化の各ステップで計算結果を記録する関数
    global step
    step += 1
    writer.writerow([step, f(x), x[0], x[1]])


x = np.array([0.0, 0.0])
step = 0
writer.writerow([step, f(x), x[0], x[1]])
optimize.fmin_slsqp(f, x, f_ieqcons=g, iprint=2, callback=callbackF)  # 逐次二次計画法
