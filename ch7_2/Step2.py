import ghpythonlib.components as gh  # 内部モジュールghpythonlib.componentsをghという名前で読み込む
import random  # 内部モジュールrandomを読み込む

b_pos_x = []  # y方向に架かるブリッジが配置されるコアの配置位置を格納
b_pos_y = []  # x方向に架かるブリッジが配置されるコアの配置位置を格納
bridge_x = []  # 生成されたブリッジ（y方向）を格納
bridge_y = []  # 生成されたブリッジ（x方向）を格納

# Step 1にて生成されたコアの配置パターンからブリッジ生成に関する情報の取得
for i in range(0, len(pos)):
    for ii in range(0, len(pos)):
        # Step1で生成されたコア配置間の距離が2スパン以内の組合せに対して実行
        if i != ii and gh.Distance(pos[i], pos[ii]) <= span * 2:
            # y座標が等しいコアの組合せに対して実行（x方向に架かるブリッジの生成情報の取得）
            if pos[i][1] == pos[ii][1]:
                # wにてコア間の距離を取得,cにてコアとコアの中心位置を取得
                w = gh.Distance(pos[i], pos[ii])
                c = gh.DivideCurve(gh.Line(pos[i], pos[ii]), 2).points[1]
                pair = [c, w]
                if pair not in b_pos_x:
                    b_pos_x.append(pair)
# x座標が等しいコアの組合せに対して実行（y方向に架かるのブリッジ生成情報の取得）
            if pos[i][0] == pos[ii][0]:
                #wにてコア間の距離を取得, cにてコアとコアの中心位置を取得
                w = gh.Distance(pos[i], pos[ii])
                c = gh.DivideCurve(gh.Line(pos[i], pos[ii]), 2).points[1]
                pair = [c, w]
                if pair not in b_pos_y:
                    b_pos_y.append(pair)

# x方向に架かるブリッジの生成
for i in range(0, len(b_pos_x)):
    #b_zにて低いブリッジの断面方向配置位置を生成, yz_posにて低いブリッジを生成するための基点生成
    b_z = Lo[random.randrange(0, len(Lo))]
    xz_pos = gh.ConstructPoint(b_pos_x[i][0][0], b_pos_x[i][0][1], b_z)
# 生成された基点にx方向に架かる低いブリッジの生成
    b = gh.CenterBox(gh.XYPlane(xz_pos), b_pos_x[i][
                     1] / 2 + b_width / 2, b_depth / 2, b_hight[0] / 2)
    bridge_x.append(b)
for i in range(0, len(b_pos_x)):
    #b_zにて高いブリッジの断面方向配置位置を生成, yz_posにて低いブリッジを生成するための基点生成
    b_z = Hi[random.randrange(0, len(Hi))]
# 生成された基点にx方向に架かる高いブリッジの生成
    xz_pos = gh.ConstructPoint(b_pos_x[i][0][0], b_pos_x[i][0][1], b_z)
    b = gh.CenterBox(gh.XYPlane(xz_pos), b_pos_x[i][
                     1] / 2 + b_width / 2, b_depth / 2, b_hight[1] / 2)
    bridge_x.append(b)

# y方向に架かるブリッジの生成
for i in range(0, len(b_pos_y)):
    # b_zにて低いブリッジの断面方向配置位置を生成, yz_posにて低いブリッジを生成するための基点生成
    b_z = Lo[random.randrange(0, len(Lo))]
    yz_pos = gh.ConstructPoint(b_pos_y[i][0][0], b_pos_y[i][0][1], b_z)
# 生成された基点にy方向に架かる低いブリッジの生成
    b = gh.CenterBox(gh.XYPlane(yz_pos), b_depth / 2,
                     b_pos_y[i][1] / 2 + b_width / 2, b_hight[0] / 2)
    bridge_y.append(b)
for i in range(0, len(b_pos_y)):
    # b_zにて高いブリッジの断面方向配置位置を生成, yz_posにて低いブリッジを生成するための基点生成
    b_z = Hi[random.randrange(0, len(Hi))]
    yz_pos = gh.ConstructPoint(b_pos_y[i][0][0], b_pos_y[i][0][1], b_z)
# 生成された基点にy方向に架かる高いブリッジの生成
    b = gh.CenterBox(gh.XYPlane(yz_pos), b_depth / 2,
                     b_pos_y[i][1] / 2 + b_width / 2, b_hight[1] / 2)
    bridge_y.append(b)

# 生成されたブリッジが格納されるbridge_x, bridge_yを無作為にシャッフルする
random.shuffle(bridge_x)
random.shuffle(bridge_y)
