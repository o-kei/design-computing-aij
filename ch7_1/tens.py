import numpy as np
from scipy import optimize
import fem
import graph
import os


def lagrange(x, w, ijt, ijc, nod, nelt, nelc, lc_bar):  # 停留条件関数
    r[:, 0], r[:, 1], r[:, 2] = x[:nod], x[nod:nod * 2], x[nod * 2:nod * 3]
    lam = x[nod * 3:]
    lght, lghc = fem.length(r, ijt, ijc, nelt, nelc)
    nablaLt, nablaLc = fem.dlengthtc(r, ijt, ijc, nod, lght, lghc, nelt, nelc)
    b = np.array([4.0 * w[e] * lght[e]**3 for e in range(nelt)])
    f1 = nablaLt.dot(b) + nablaLc.dot(lam)
    f2 = lghc - lc_bar
    return np.r_[f1, f2]


filename = '20_face_pieces'
inputfilename = 'datain/' + filename + '.csv'
r, ijt, ijc, nod, nelt, nelc = fem.input(inputfilename)  # 形状と要素節点関係の読み込み
xmin, xmax, ymin, ymax, zmin, zmax =\
    np.min(r), np.max(r), np.min(r), np.max(r), np.min(r), np.max(r)
graph.plot_shape3D(r, ijt, ijc, xmin, xmax, ymin,
                   ymax, zmin, zmax)  # 初期形状の描画(確認用)
lght, lghc = fem.length(r, ijt, ijc, nelt, nelc)  # 部材長の計算
lc_bar = lghc * 1.0  # 圧縮材の長さの指定値(ここでは初期形状の値とする)
lam = np.zeros(nelc)
x = np.r_[r[:, 0], r[:, 1], r[:, 2], lam]
w = [1.0] * len(lght)
x = optimize.root(lagrange, x, args=(w, ijt, ijc, nod, nelt, nelc, lc_bar)).x
r[:, 0], r[:, 1], r[:, 2] = x[:nod], x[
    nod:nod * 2], x[nod * 2:nod * 3]  # 最適解を節点座標へ書込む
b, lam = np.array(
    [4.0 * w[e] * lght[e]**3 for e in range(nelt)]), x[nod * 3:]  # 軸力モード計算
dir = 'dataout/'
outputfilename = dir + filename + '_opt.csv'

try:  # dataoutフォルダの存在有無を調べ，なければ新規作成する
    os.stat(dir)
except:
    os.mkdir(dir)
fem.output(outputfilename, r, nod, ijt, ijc,
           nelt, nelc, b, lam)  # 最適形状と軸力モードの出力
xmin, xmax, ymin, ymax, zmin, zmax =\
    np.min(r), np.max(r), np.min(r), np.max(r), np.min(r), np.max(r)
graph.plot_shape3D(r, ijt, ijc, xmin, xmax, ymin, ymax, zmin, zmax)  # 最適形状の描画
