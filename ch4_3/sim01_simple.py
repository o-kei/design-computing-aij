class Person:

    def __init__(self, name):  # クラスが呼び出されたときに発動（initialize）。
        # __init__はPythonで最初から定義されている。
        self.name = name  # 自分の名前

    def behave(self):  # 1ステップで行う，一連の行動。
        # 自分の名前をprintする %sのところにself.nameを代入している。
        print('My name is %s' % self.name)


def simulation():
    # シミュレーション準備
    person = Person('Yasuda')  # 人を設定
    time = -1
    # シミュレーション開始
    while time < 3:  # 時間が3以上のときにFalseとなってループが終了する。
        time += 1
        print('time:%d' % time)
        person.behave()  # メソッドbehaveを実行する
    else:  # whileループの条件式がFalseを返したとき（whileループ終了時）に発動
        print('time:%d, finished' % time)


if __name__ == '__main__':  # このスクリプト自体が実行されたときにのみ以下を実行
    simulation()
