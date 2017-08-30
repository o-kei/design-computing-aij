# 文字コードエラーを避けるために以下の設定が必要
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import numpy as np  # モジュールnumpyをnpという名前で読み込み
import random
import math  # モジュールrandom,mathを読み込み
from scipy import optimize
E = 205000.0
L = 2.0 * 1.0e+3
P1 = 400.0 * 1.0e+3
P2 = 200.0 * 1.0e+3
sigma_bar = 235.0
u_bar = 5.0
a1 = L * 1.0
a2 = L * 1.0
penalty = 1.0e+10
A0 = np.array([3000.0, 3000.0])


def f(A):
    cons = g(A)
    return a1 * A[0] + a2 * A[1] + penalty * (max(-cons[0], 0) + max(-cons[1], 0) +
                                              max(-cons[2], 0) + max(-cons[3], 0) + max(-cons[4], 0))


def g(A):
    sigma1 = sigma_bar - (P1 + P2) / A[0]
    sigma2 = sigma_bar - P2 / A[1]
    u2 = u_bar - (P1 + P2) * L / A[0] / E - P2 * L / A[1] / E
    return np.array([sigma1, sigma2, u2, A[0], A[1]])
nstep, cool, shrink, scale, temp, delta, nb = 1000, 0.99, 0.99, 0.01, 1.0, 3000.0, 10
# ステップ数,温度を減らす割合,探索範囲を縮小する割合,変数のスケーリングparameter,温度の初期化,探索範囲の初期化,近傍解の数
objopt = f(A0)  # 目的関数の最適値の初期化
random.seed(1000)  # 乱数の初期化
obj0 = f(A0)  # 目的関数の計算
# 設計変数と目的関数の履歴保存用
A0_history = [A0[0]]
A1_history = [A0[1]]
f_history = [obj0]
for k in range(nstep):
    print('-------- ステップ: ', k)
    print('温度', temp, '探索範囲', delta, '変数', A0, '目的関数', obj0, '暫定値', objopt)
    # 近傍解の評価
    obj1 = 1.0e10
    for n in range(nb):
        A = [A0[0] + (random.random() - 0.5) * delta,
             A0[1] + (random.random() - 0.5) * delta]
        obj = f(A)  # 目的関数の計算
        if(obj < obj1):  # 最適な近傍解を選択
            obj1 = obj
            A1 = list(A)
    print('最適近傍解', A, '目的関数', obj1)
    A0_history.append(A[0])
    A1_history.append(A[1])
    f_history.append(obj1)
    diff = obj1 - obj0  # 目的関数の増分
    if(diff < 0):  # 増分が負のとき目的関数と解を更新
        obj0 = obj1
        A0 = A1
    else:  # 増分が0または正のとき
        prob = math.exp(-diff / temp / scale)  # 更新確率の計算
        ran = random.random()
        if(ran < prob):  # 乱数が更新確率より小さいとき目的関数と解を更新
            obj0 = obj1
            A0 = A1
    temp = temp * cool  # 温度の更新
    delta = delta * shrink  # 探索範囲の更新
    if(obj1 < objopt):  # 最適値の更新
        objopt = obj1
        optstep = k
        Aopt = A1
print('==========================')
print('最適目的関数値', objopt, 'ステップ', optstep, '変数', Aopt)
