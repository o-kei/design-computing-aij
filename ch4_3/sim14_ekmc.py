import simpy
import numpy.random as npr
import sim13_many as mysim  # 自分で作成したモジュールを読み込み。
from visualize import plotter, animation
RANDOM_SEED = 5


def monitor(env, toilet, data, interval=1.0):  # 記録用紙
    while True:
        tup = (
            env.now,  # 現在時刻
            toilet.count,  # 使用人数
            len(toilet.queue),  # 行列人数
        )
        data.append(tup)
        yield env.timeout(interval)


def simulation(lambd=0.3, mu=0.2, capacity=1, until=100):
    # シミュレーション準備
    # 環境を設定
    env = simpy.Environment()  # SimPyによるシミュレーション環境を作成
    toilet = simpy.Resource(env, capacity=capacity)
    # 人を出現させるプロセスと登録 # 無限母集団
    env.process(mysim.person_generator(env, toilet,
                                       lambd, mu))
    # 記録用紙を設定
    data = []  # 記録用
    env.process(monitor(env, toilet, data))
    # データを設定
    # シミュレーション
    env.run(until=until)
    # 可視化
    animation(data, lambd, mu, capacity, until)
    plotter(data, lambd, mu, capacity)


if __name__ == '__main__':  # このスクリプト自体が実行されたときにのみ以下を実行
    npr.seed(RANDOM_SEED)
    simulation(lambd=1.0, mu=0.2, capacity=6, until=100)
