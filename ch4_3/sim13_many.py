import simpy
import numpy.random as npr
RANDOM_SEED = 5


class Person:

    def __init__(self, env, name, mu):
        self.env = env  # SimPyのシミュレーション環境
        self.name = name  # 自分の名前
        # 用を足すのにかかる時間をアーラン分布で与える。
        k = 3.0
        lam_2 = k * mu  # 期待値1/mu=k/lamよりlam=k*mu
        self.relieve_time = npr.gamma(k, 1. / lam_2)
        self.status = 'initial'  # 自分の状態を表す。

    def __repr__(self):  # print(self)をした時の出力を決めておく。
        return 'time: %6.2f, name: %s, status: %s' % (self.env.now, self.name, self.status)

    def behave(self, toilet):  # 1ステップで行う，一連の行動。
        print(self)
        # SimPyに追加するプロセスとして，generatorとして作成する。
        with toilet.request() as req:
            self.status = 'queueing'
            print(self)
            yield req  # requestが通るまで待ち，通ったら次のプロセスへ。
            self.status = 'relieving'
            print(self)
            yield self.env.timeout(self.relieve_time)
            self.status = 'leaving'  # 退出中。
            print(self)


def person_generator(env, toilet, lam, mu, person_Num=None):
    print('time: %6.2f, start' % env.now)
    i = 0
    if person_Num is None:
        def flag(i):
            return True  # Noneのときは無限母集団として扱う。
    else:
        def flag(i):
            return i < person_Num  # 有限母集団。

    while flag(i):
        # 登場する時間間隔は指数分布
        yield env.timeout(npr.exponential(1.0 / lam, size=1))
        person = Person(env, 'person_%00d' % i, mu)
        i += 1
        env.process(person.behave(toilet))  # シミュレーション環境に実行するプロセスを追加


def simulation(lam=0.2, mu=0.2, capacity=1, until=100):
    # シミュレーション準備
    # 環境を設定
    env = simpy.Environment()  # SimPyによるシミュレーション環境を作成
    toilet = simpy.Resource(env, capacity=capacity)  # capacityの数だけトイレがある。
    # 人を設定
    person_Num = 5  # 有限母集団
    env.process(person_generator(env, toilet,
                                 lam, mu, person_Num))  # 人を出現させるプロセスと登録
    # シミュレーション開始
    env.run(until=until)


if __name__ == '__main__':  # このスクリプト自体が実行されたときにのみ以下を実行
    npr.seed(RANDOM_SEED)
    simulation(lam=0.2, mu=0.2, capacity=1, until=100)
