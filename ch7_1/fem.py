import numpy as np
import csv
import math


def input(fname):
    r, ijt, ijc = [], [], []
    reader = csv.reader(open(fname, 'r'))
    for row in reader:  # 節点の読み込み
        break  # 先頭行は読み飛ばし
    for row in reader:
        if row[0] == '':
            break
        r.append([float(row[0]), float(row[1]), float(row[2])])
    nod, r = len(r), np.array(r)  # 節点数,ｒのarray変換
    for row in reader:  # 要素節点関係の読み込み
        break  # 先頭行は読み飛ばし
    for row in reader:
        if row[0] == '':
            break
        if int(row[2]) == 0:
            ijc.append([int(row[0]), int(row[1])])
        else:
            ijt.append([int(row[0]), int(row[1])])
    nelt, nelc = len(ijt), len(ijc)  # 圧縮/引張材の数
    return r, ijt, ijc, nod, nelt, nelc


def output(fname, r, nod, ijt, ijc, nelt, nelc, b, lam):
    writer = csv.writer(open(fname, 'w', newline=''))
    writer.writerow(['X', 'Y', 'Z'])  # タイトル行
    [writer.writerow([r[i, 0], r[i, 1], r[i, 2]])
     for i in range(nod)]  # 節点座標の書き込み
    writer.writerow([])  # 1行あける
    writer.writerow(['I', 'J', 'CorT', 'Axial Force'])  # タイトル行
    [writer.writerow([ijc[e][0], ijc[e][1], 0, lam[e]])
     for e in range(nelc)]  # 圧縮材情報の書き込み
    [writer.writerow([ijt[e][0], ijt[e][1], 1, b[e]])
     for e in range(nelt)]  # 引張材情報の書き込み


def length(r, ijt, ijc, nelt, nelc):
    lght, lghc = [], []  # 圧縮/引張材の長さのリスト
    for e in range(nelt):
        i, j = ijt[e][0], ijt[e][1]
        xl, yl, zl = r[i, 0] - r[j, 0], r[i, 1] - r[j, 1], r[i, 2] - r[j, 2]
        lght.append(math.sqrt(xl**2 + yl**2 + zl**2))  # 引張材の部材長計算
    for e in range(nelc):
        i, j = ijc[e][0], ijc[e][1]
        xl, yl, zl = r[i, 0] - r[j, 0], r[i, 1] - r[j, 1], r[i, 2] - r[j, 2]
        lghc.append(math.sqrt(xl**2 + yl**2 + zl**2))  # 圧縮材の部材長計算
    return np.array(lght), np.array(lghc)  # リスト→arrayに変換して要素長さを返す


def dlengthtc(r, ijt, ijc, nod, lght, lghc, nelt, nelc):
    nablaLt, nablaLc = np.zeros([nod * 3, nelt]), np.zeros([nod * 3, nelc])
    for e in range(nelt):  # 引張材の長さのrに関する偏微分の計算
        i, j = ijt[e][0], ijt[e][1]
        xl, yl, zl = r[i, 0] - r[j, 0], r[i, 1] - r[j, 1], r[i, 2] - r[j, 2]
        nablaLt[i, e], nablaLt[j, e] = xl / lght[e], -xl / lght[e]
        nablaLt[nod + i, e], nablaLt[nod + j, e] = yl / lght[e], -yl / lght[e]
        nablaLt[nod * 2 + i, e], nablaLt[nod *
                                         2 + j, e] = zl / lght[e], -zl / lght[e]
    for e in range(nelc):  # 圧縮材の長さのrに関する偏微分の計算
        i, j = ijc[e][0], ijc[e][1]
        xl, yl, zl = r[i, 0] - r[j, 0], r[i, 1] - r[j, 1], r[i, 2] - r[j, 2]
        nablaLc[i, e], nablaLc[j, e] = xl / lghc[e], -xl / lghc[e]
        nablaLc[nod + i, e], nablaLc[nod + j, e] = yl / lghc[e], -yl / lghc[e]
        nablaLc[nod * 2 + i, e], nablaLc[nod *
                                         2 + j, e] = zl / lghc[e], -zl / lghc[e]
    return nablaLt, nablaLc
