import copy

class Rectangle:

    def __init__(self, dx, dy):  # 初期化関数
        self.dx = dx
        self.dy = dy

    def cal_area(self):  # 面積を計算する関数
        self.area = self.dx * self.dy
        return self.area

a=Rectangle(10,10)
area=a.cal_area()
print(area)

b=a
area2=b.cal_area()
print(area2)

c=copy.copy(a)
d=copy.deepcopy(a)

a.dx=20

area2=b.cal_area()
print(area2)

area2=c.cal_area()
print(area2)

area2=d.cal_area()
print(area2)


x=[1,2,3,4]

y=x[:]

x[2]=100

print(x)
print(y)
