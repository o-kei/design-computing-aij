import simpy
import numpy.random as npr
RANDOM_SEED = 5


class Person:

    def __init__(self, env, name, lam, mu):
        self.env = env  # SimPyのシミュレーション環境
        self.name = name  # 自分の名前
        # 到着するまでの時間の期待値は1/到着率
        self.arrive_time = npr.exponential(1. / lam)
        # 用を足すのにかかる時間をアーラン分布で与える。
        k = 3.0
        lam_2 = k * mu  # 期待値1/mu=k/lamよりlam=k*mu
        self.relieve_time = npr.gamma(k, 1. / lam_2)
        self.status = 'initial'  # 自分の状態を表す。

    def __repr__(self):  # print(self)をした時の出力を決めておく。
        return 'time: %6.2f, name: %s, status: %s' % (self.env.now, self.name, self.status)

    def behave(self):  # 1ステップで行う，一連の行動。
        # SimPyに追加するプロセスとして，generatorとして作成する。
        # 自分の名前をprintする %sのところにself.nameを代入している。
        self.status = 'arrival'
        print(self)
        yield self.env.timeout(self.arrive_time)
        self.status = 'relieving'
        print(self)
        yield self.env.timeout(self.relieve_time)
        self.status = 'leaving'  # 退出中。
        print(self)


def simulation(lam, mu):
    # シミュレーション準備
    # 環境を設定
    env = simpy.Environment()  # SimPyによるシミュレーション環境を作成
    # 人を設定
    person = Person(env, 'Yasuda', lam, mu)
    env.process(person.behave())  # プロセスと登録
    # シミュレーション開始
    env.run(until=100)


if __name__ == '__main__':  # このスクリプト自体が実行されたときにのみ以下を実行
    npr.seed(RANDOM_SEED)
    simulation(1.0 / 30.0, 1 / 5.0)
