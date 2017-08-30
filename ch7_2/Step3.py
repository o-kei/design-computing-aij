import ghpythonlib.components as gh  # 内部モジュールghpythonlib.componentsをghという名前で読み込む
import random  # 内部モジュールrandomを読み込み

xkeepList = []  # xキープリスト：残すと判断されたブリッジ（x方向）を格納
xdelList = []  # x削除リスト：削除すると判断されたブリッジ（x方向）
ykeepList = []  # yキープリスト：残すと判断されたブリッジ（y方向）を格納
ydelList = []  # y削除リスト：削除すると判断されたブリッジ（y方向）を格納

# x方向に架かるブリッジの選択
for i in range(0, len(bridge_x)):
    for ii in range(0, len(bridge_x)):
        if i != ii:
            # ブリッジiがx削除リストにない場合実行
            if bridge_x[i] not in xdelList:
                # ブリッジiiがxキープリスト,x削除リストにない場合,ブリッジiとブリッジiiに重なりがあるかないか判定
                if bridge_x[ii] not in xkeepList and bridge_x[ii] not in xdelList:
                    check = gh.BrepXBrep(bridge_x[i], bridge_x[ii]).curves
# 重なりがある場合ブリッジiはxキープリストへ格納,ブリッジiiは削除リストへ格納
                if check != None:
                    xkeepList.append(bridge_x[i])
                    xdelList.append(bridge_x[ii])

# y方向にå架かるブリッジの選択
for i in range(0, len(bridge_y)):
    for ii in range(0, len(bridge_y)):
        if i != ii:
            # ブリッジiがy削除リストにない場合実行
            if bridge_y[i] not in ydelList:
                # ブリッジiiがyキープリスト,y削除リストにない場合,ブリッジiとブリッジiiに重なりがあるかないか判定
                if bridge_y[ii] not in ykeepList and bridge_y[ii] not in ydelList:
                    check = gh.BrepXBrep(bridge_y[i], bridge_y[ii]).curves
# 重なりがある場合ブリッジiはyキープリストへ格納,ブリッジiiは削除リストへ格納
                if check != None:
                    ykeepList.append(bridge_y[i])
                    ydelList.append(bridge_y[ii])

xdelList = []
ydelList = []
B = []

#----------------------------------------------------------------
# 以下xキープリスト,yキープリスト内のブリッジ形態（端部を傾斜）に変更
for i in xkeepList:
    P = []
    P.append(gh.BoxCorners(i)._0)
    P.append(gh.BoxCorners(i)._1)
    P.append(gh.BoxCorners(i)._2)
    P.append(gh.BoxCorners(i)._3)
    P.append(gh.BoxCorners(i)._4)
    P.append(gh.BoxCorners(i)._5)
    P.append(gh.BoxCorners(i)._6)
    P.append(gh.BoxCorners(i)._7)
    t = gh.Distance(P[0], P[4])
    P[0] = gh.ConstructPoint(P[0][0] + t / 4, P[0][1], P[0][2])
    P[1] = gh.ConstructPoint(P[1][0] - t / 4, P[1][1], P[1][2])
    P[2] = gh.ConstructPoint(P[2][0] - t / 4, P[2][1], P[0][2])
    P[3] = gh.ConstructPoint(P[3][0] + t / 4, P[3][1], P[1][2])
    B.append(gh.ConstructMesh((P[0], P[1], P[2], P[3])))
    B.append(gh.ConstructMesh((P[4], P[5], P[6], P[7])))
    B.append(gh.ConstructMesh((P[0], P[3], P[7], P[4])))
    B.append(gh.ConstructMesh((P[1], P[2], P[6], P[5])))
    B.append(gh.ConstructMesh((P[0], P[1], P[5], P[4])))
    B.append(gh.ConstructMesh((P[2], P[3], P[7], P[6])))

for i in ykeepList:
    P = []
    P.append(gh.BoxCorners(i)._0)
    P.append(gh.BoxCorners(i)._1)
    P.append(gh.BoxCorners(i)._2)
    P.append(gh.BoxCorners(i)._3)
    P.append(gh.BoxCorners(i)._4)
    P.append(gh.BoxCorners(i)._5)
    P.append(gh.BoxCorners(i)._6)
    P.append(gh.BoxCorners(i)._7)
    t = gh.Distance(P[0], P[4])
    P[0] = gh.ConstructPoint(P[0][0], P[0][1] + t / 4, P[0][2])
    P[1] = gh.ConstructPoint(P[1][0], P[1][1] + t / 4, P[1][2])
    P[2] = gh.ConstructPoint(P[2][0], P[2][1] - t / 4, P[0][2])
    P[3] = gh.ConstructPoint(P[3][0], P[3][1] - t / 4, P[1][2])
    B.append(gh.ConstructMesh((P[0], P[1], P[2], P[3])))
    B.append(gh.ConstructMesh((P[4], P[5], P[6], P[7])))
    B.append(gh.ConstructMesh((P[0], P[3], P[7], P[4])))
    B.append(gh.ConstructMesh((P[1], P[2], P[6], P[5])))
    B.append(gh.ConstructMesh((P[0], P[1], P[5], P[4])))
    B.append(gh.ConstructMesh((P[2], P[3], P[7], P[6])))
