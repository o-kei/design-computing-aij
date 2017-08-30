class Rectangle:

    def __init__(self, dx, dy):  # 初期化関数
        self.dx = dx
        self.dy = dy

    def cal_area(self):  # 面積を計算する関数
        self.area = self.dx * self.dy
        return self.area