f1 = open('data1.dat', 'r')  # data1.dat を読込みモードで開く
f1_lines = f1.readlines()  # ファイルを一行ずつ全てをstrタイプで読み込み
f1.close()  # data1.datを閉じる
print('f1:', f1_lines)
f2_lines = []  # データを格納するリスト
for f1_line in f1_lines:
    x1, y1, z1 = f1_line.split(',')  # カンマを区切りとしてリストに分割
    x2 = x1 + ' root'   # x1に文字列を追加
    y2 = '%s^%s' % (float(z1), int(y1))  # 文字列の置換
    z2 = str(float(z1) ** int(y1))  # z1を浮動点少数にしてy1乗
    f2_line = ';'.join([x2, y2, z2]) + '\n'  # リストをセミコロン区切り結合して改行文字を足す
    f2_lines.append(f2_line)
print('f2:', f2_lines)
f2 = open('data2.dat', 'w')  # data2.dat を書込みモードで開く
f2.writelines(f2_lines)  # 2乗値と空白，改行コードを書き込み
f2.close()  # data2.dat を閉じる
