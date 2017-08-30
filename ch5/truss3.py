import numpy as np
import csv
import math


def input(fname):  # トラスの読み込み
    reader = csv.reader(open(fname, 'r'))
    # 節点座標,要素節点関係,断面積,ヤング係数,境界条件,荷重ベクトル
    r, ij, A, E, fix, p = [], [], [], [], [], []
    for row in reader:  # 節点の読み込み
        break  # 先頭行は読み飛ばし
    for row in reader:
        if row[0] == '':
            break
        r.append([float(row[0]), float(row[1])])
    nod, r = len(r), np.array(r)  # 節点数,list→array変換
    for row in reader:  # 要素節点関係の読み込み
        break  # 先頭行は読み飛ばし
    for row in reader:
        if row[0] == '':
            break
        ij.append([int(row[0]), int(row[1])])
        A.append(float(row[2]))
        E.append(float(row[3]))
    nel, A, E = len(ij), np.array(A), np.array(
        E)  # 要素数,list→array変換,list→array変換
    for row in reader:  # 境界条件の読み込み
        break  # 先頭行は読み飛ばし
    for row in reader:
        if row[0] == '':
            break
        fix.append([int(row[0]), int(row[1]), int(row[1])])
    p = np.zeros(nod * 2)
    for row in reader:  # 集中荷重の読み込み
        break  # 先頭行は読み飛ばし
    for row in reader:
        if row[0] == '':
            break
        p[int(row[0]) * 2:(int(row[0]) + 1) * 2] =\
            [float(row[1]), float(row[2])]
    return r, nod, ij, nel, A, E, fix, p


def length(r, ij, nel):  # 要素長さを計算
    lgh = [math.sqrt((r[ij[i][0], 0] - r[ij[i][1], 0])**2 +
                     (r[ij[i][0], 1] - r[ij[i][1], 1])**2) for i in range(nel)]
    return np.array(lgh)


def transmatrix(l, r1, r2):  # 座標変換行列を求める
    tr = np.matrix([[0.0] * 4] * 4)
    lx, ly = r2[0] - r1[0], r2[1] - r1[1]
    cos, sin = lx / l, ly / l
    tr[0, 0], tr[1, 1], tr[2, 2], tr[3, 3] = cos, cos, cos, cos
    tr[1, 0], tr[3, 2], tr[0, 1], tr[2, 3] = -sin, -sin, sin, sin
    return tr


def boundary_condition(fix):  # 境界条件の指定
    remove = []
    for i in fix:
        if i[1] == 1:
            remove.append(i[0] * 2)
        if i[2] == 1:
            remove.append(i[0] * 2 + 1)
    return remove


def global_b(r, nod, ij, nel, lgh, remove):  # 全体座標系でのbベクトル作成
    b0, b_g = np.zeros([4]), np.zeros([2 * nod, nel])
    b0[0], b0[2] = 1.0, -1.0
    eln = 0
    for i_j in ij:
        ni, nj = i_j[0], i_j[1]
        trans = transmatrix(lgh[eln], r[ni, :], r[nj, :])
        b = np.dot(trans.T, b0)  # 全体座標系に変換
        b_g[ni * 2:(ni + 1) * 2, eln] += [b[0, 0], b[0, 1]]  # i節点の自由度番号位置に格納
        b_g[nj * 2:(nj + 1) * 2, eln] += [b[0, 2], b[0, 3]]  # j節点の自由度番号位置に格納
        eln += 1
    return np.delete(np.matrix(b_g), remove, 0)  # 拘束節点自由度に対応する行を消去


def make_k(E, a, l, b, nel):  # 全体剛性行列の作成
    K = sum([E[e] * a[e] / l[e] * b[:, e].dot(b[:, e].T) for e in range(nel)])
    return K
