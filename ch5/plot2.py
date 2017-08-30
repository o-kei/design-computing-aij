import numpy as np  # モジュールnumpyをnpという名前で読み込み
import csv  # モジュールcsvの読み込み
import matplotlib.pyplot as plt  # モジュールmatplotlibのpyplot関数をplt
# という名前で読み込み

reader = csv.reader(open('out2.csv', 'r'))  # 先ほど出力したoutput.csvの読み込み
f_history = []  # 目的関数の履歴
x1_history, x2_history = [], []  # 設計変数の履歴
for row in reader:  # 1行目はラベル行なので読み飛ばし
    break
for row in reader:
    f_history.append(float(row[1]))  # 目的関数の読み込み
    x1_history.append(float(row[2]))  # 設計変数の読み込み
    x2_history.append(float(row[3]))
plt.figure(figsize=(15, 8))  # グラフ描画キャンバスを横縦比15:8で生成
x1 = np.arange(-0.5, 4.5, 0.1)  # 1.25〜4.75まで0.1刻みのベクトル
x2 = np.arange(-0.5, 4.5, 0.1)  # 0.25〜3.75まで0.1刻みのベクトル
X1, X2 = np.meshgrid(x1, x2)  # x1,x2を組み合わせた行列
f = np.vectorize(lambda x1, x2: ((2.0 - x1)**2 + (4.0 - x2)**2)**0.5 +
                 ((3.0 - x1)**2 + (2.0 - x2)**2)**0.5)  # x1,x2を引数として
# 目的関数を返す関数
plt.subplot(1, 2, 1)  # 1行目の2列の並びの1列目にグラフを生成
plt.xlabel('x1')  # 水平方向のラベル
plt.ylabel('x2')  # 鉛直方向のラベル
C = plt.contour(X1, X2, f(X1, X2), 20, colors='black')  # 等高線データ生成
plt.clabel(C, inline=1, fontsize=10)  # 等高線図生成
plt.plot(x1_history, x2_history)  # 目的関数の探索経路生成
# __
zero1 = [0.0] * len(x1)
zero2 = [0.0] * len(x2)
two1 = [2.0] * len(x1)
two2 = [2.0] * len(x2)
h = (-2.0 * x1 + 7.0) / 3.0
plt.plot(x1, zero1, '-', color='gray', label=r'$x_1=0$')
plt.plot(zero2, x2, '--', color='gray', label=r'$x_2=0$')
plt.plot(x1, two1, '-.', color='gray', label=r'$x_1-2=0$')
plt.plot(two2, x2, ':', color='gray', label=r'$x_2-2=0$')
plt.plot(x1, h, '.', color='gray', label=r'$2x_1+3x_2-7=0$')
plt.fill([0, 2, 2, 0.5, 0], [0, 0, 1, 2, 2], alpha=0.1)
# __
plt.subplot(1, 2, 2)  # 1行目の2列の並びの2列目にグラフを生成
plt.xlabel('step')  # 水平方向のラベル
plt.ylabel('f(x)')  # 鉛直方向のラベル
plt.plot(f_history)  # 目的関数の履歴図の生成
# (x成分を省略すれば自動的に横軸はstep数となる)
plt.show()  # グラフを画面に表示する
