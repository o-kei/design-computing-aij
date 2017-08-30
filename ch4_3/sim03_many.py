import numpy.random as npr
RANDOM_SEED = 5


class Person:

    def __init__(self, name, expected, ahead=None):
        self.name = name  # 自分の名前
        self.ahead = ahead  # 自分の前にいる人
        # 用を足すのにかかる時間をアーラン分布で与える。
        k = 3.0
        lam_2 = k / expected  # 期待値E=k/lamよりlam=k/E
        self.relieve_time = npr.gamma(k, 1. / lam_2)
        self.queueing_time = 0  # 累積の待ち時間
        self.status = 'initial'  # 自分の状態を表す。Noneは存在しないことを表す。

    def __repr__(self):  # print(self)をした時の出力を決めておく。
        return 'name: %s, status: %s' % (self.name, self.status)

    def behave(self):  # 1ステップで行う，一連の行動。
        # 環境から情報を得る
        # 前にいる人の状態を見て得る。ahead_statusを決定する。
        if self.ahead != None:
            ahead_status = self.ahead.status
        else:
            ahead_status = 'leaving'

        # 意思決定をして行動する
        if ahead_status != 'leaving':  # 前に人がいたら行列に並ぶ。
            self.queueing_time += 1
            self.status = 'queueing for %d' % self.queueing_time
            print(self)
        else:  # 前に人がいなければ，用をたす。
            self.relieve_time += -1
            self.status = 'relieving rest:%-2.2f' % self.relieve_time
            print(self)
            if self.relieve_time <= 0:  # もし用を足し終えたら，退出する。
                self.status = 'leaving'  # 退出中。
                print(self)


def person_generator(expected):  # nextで呼び出すたびにpersonを生成
    i = 0
    ahead = None
    while True:
        person = Person('person_%02d' % i, expected, ahead=ahead)
        ahead = person
        i += 1
        yield person  # yeildは，次に呼ばれたときにまたこの位置から処理される。


def simulation(lam, mu, person_Num):
    # シミュレーション準備
    person_list_queueing = []  # システム内にいる人のリスト。
    person_list_worked = []  # シミュレーション終了した人をつめこむリスト
    gen = person_generator(1. / mu)  # 用を足す時間の期待値=1/単位時間あたりに用を足す人数
    time = -1

    # シミュレーション開始
    # 全員が退出するまでシミュレーションをする。
    while len(person_list_worked) < person_Num:  # 指定した人数が終了したらループ終了
        time += 1
        print('time:%d, queue:%d' % (time, len(person_list_queueing)))
        # 出現の処理
        num = npr.poisson(lam)  # 単位時間あたりの到着人数の期待値=到着率(人)。
        if num:
            for i in range(num):
                person_list_queueing.append(next(gen))  # next(gen)でpersonを生成

        # システム内にいる人それぞれの行動の処理
        # pythonの仕様で，person_listのループ中にリストの内容を変更すると
        # 予期しない挙動を示すので，[:]のスライスでコピーする。
        for person in person_list_queueing[:]:  # 一人ずつ行動する
            person.behave()
            if person.status == 'leaving':  # 退出になっているpersonをリストから取り除く
                person_list_queueing.remove(person)
                person_list_worked.append(person)

        if time > 100:
            break

    # シミュレーション終了後まとめ
    print('report')
    for person in person_list_worked:
        print('name: %s, queueing time: %s' %
              (person.name, person.queueing_time))


if __name__ == '__main__':  # このスクリプト自体が実行されたときにのみ以下を実行
    npr.seed(RANDOM_SEED)
    simulation(lam=0.2, mu=0.2, person_Num=5)
