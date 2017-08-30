import numpy.random as npr
RANDOM_SEED = 5


class Person:

    def __init__(self, name):
        self.name = name  # 自分の名前
        # 到着するまでの時間を指数分布で与える。
        expected_1 = 30.0
        lam_1 = 1.0 / expected_1  # 期待値=1/lam
        self.arrive_time = npr.exponential(1. / lam_1)
        # 用を足すのにかかる時間をアーラン分布で与える。
        # アーラン分布はガンマ分布の関数で表現できる。
        k = 3.0
        expected_2 = 5.0
        lam_2 = k / expected_2  # 期待値E=k/lamよりlam=k/E
        self.relieve_time = npr.gamma(k, 1. / lam_2)
        self.status = 'initial'  # 自分の状態を表す。Noneは存在しないことを表す。

    def __repr__(self):  # print(self)をした時の出力を決めておく。
        return 'name: %s, status: %s' % (self.name, self.status)

    def behave(self):  # 1ステップで行う，一連の行動。
        if self.status == 'initial':
            self.arrive_time -= 1  # カウントダウンする
            if self.arrive_time <= 0:
                self.status = 'relieving'
        elif self.status == 'relieving':
            self.relieve_time -= 1  # カウントダウンする
            if self.relieve_time <= 0:  # もし用を足し終えたら，退出する。
                self.status = 'leaving'  # 退出中。
        print(self)


def simulation():
    # シミュレーション準備
    person = Person('Yasuda')  # 人を設定
    time = 0
    # シミュレーション開始
    while time < 1000:
        time += 1
        print('time:%d' % time)
        person.behave()
        if person.status == 'leaving':
            break  # 退出したのでループを終わる

    # シミュレーション終了後まとめ
    print('report\nsimulation time: %d' % (time))


if __name__ == '__main__':  # このスクリプト自体が実行されたときにのみ以下を実行
    npr.seed(RANDOM_SEED)
    simulation()
