import csv  # csvファイルのインポート。このファイル自体をcsv.pyにすると競合するので注意。
f1 = open('data1.csv', 'r')  # data1.csvを入力のためにopen
f2 = open('data2.csv', 'w', newline='')  # data2.csvを出力のためにopen
reader = csv.reader(f1)  # data1.csvをcsv形式で認識
writer = csv.writer(f2)  # data2.csvをcsv形式で認識
for row in reader:  # csvファイルの内容を1行ずつリストとして読み込む
    data1, data2 = float(row[0])**2, float(row[1])**2  # 実数に変換し2乗する
    writer.writerow([data1, data2])  # 1行ずつ書き込む
