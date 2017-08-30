import ghpythonlib.components as gh  # 内部モジュールghpythonlib.componentsをghという名前で読み込む
import random  # 内部モジュールrandomを読み込む

ArrayPoint = []  # 生成された配置位置を格納
pos = []  # 選択された配置位置を格納
core = []  # 生成されたコアを格納

# 4行5列のコア配置位置の生成
for i in range(0, 5):
    for ii in range(0, 4):
        p = gh.ConstructPoint(i * span, ii * span, 0)
        ArrayPoint.append(p)

# core_num（得たいコアの本数）となるまで配置位置を無作為に選択してコアを生成
while len(pos) < core_num:
    id = random.randrange(0, len(ArrayPoint))
    if id not in pos:
        pos.append(ArrayPoint[id])
        cpos_z = gh.ConstructPoint(ArrayPoint[id][0], ArrayPoint[id][
                                   1], ArrayPoint[id][2] + 268990 / 2)
        core.append(gh.CenterBox(cpos_z, core_width /
                                 2, core_width / 2, core_hight / 2))
