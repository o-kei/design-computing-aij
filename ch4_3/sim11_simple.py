import simpy


class Person:

    def __init__(self, env, name):
        self.env = env  # SimPyのシミュレーション環境
        self.name = name  # 自分の名前

    def behave(self):  # 1ステップで行う，一連の行動。
        # SimPyに追加するプロセスとして，generatorとして作成する。
        while True:
            print('time[%02d] My name is %s' % (self.env.now, self.name))
            yield self.env.timeout(1)


def simulation():
    # シミュレーション準備
    # 環境を設定
    env = simpy.Environment()  # SimPyによるシミュレーション環境を作成
    # 人を設定
    person = Person(env, 'Yasuda')
    env.process(person.behave())  # プロセスと登録
    # シミュレーション開始
    env.run(until=5)


if __name__ == '__main__':  # このスクリプト自体が実行されたときにのみ以下を実行
    simulation()
