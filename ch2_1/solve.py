import numpy as np
a = np.array([[1, 2], [3, 4]])  # 行列の定義
b = np.array([5, 11])  # ベクトルの定義
x = np.linalg.solve(a, b)  # 連立1次方程式の解
print(x)
