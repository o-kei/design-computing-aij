import numpy as np
from scipy import integrate as itgr  # scipy内のintegrate関数をインポート


def pi(x):  # 被積分関数の定義
    return 4.0 / (1.0 + x**2)
answer = itgr.quad(pi, 0, 1)  # (被積分関数,積分区間下,積分区間上)
print(answer)
