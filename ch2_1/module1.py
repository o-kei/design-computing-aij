def read_data(file_name):
    import csv
    reader = csv.reader(open(file_name, 'r'))
    X, Y = [], []
    for row in reader:
        X.append(row[0]), Y.append(row[1])
    return X, Y  # データを返す


def draw_graph(X, Y, xmin, xmax, ymin, ymax, Lc, Ls, Lw, title, xlabel, ylabel):
    import matplotlib.pyplot as plt
    plt.xlim(xmin, xmax)  # Xの範囲の指定
    plt.ylim(ymin, ymax)  # Yの範囲の指定
    plt.title(title)  # グラフタイトル
    plt.xlabel(xlabel)  # X軸タイトル
    plt.ylabel(ylabel)  # Y軸タイトル
    plt.plot(X, Y, color=Lc, linestyle=Ls, linewidth=Lw)  # グラフをメモリ上に作成
    plt.show()  # グラフの描画
