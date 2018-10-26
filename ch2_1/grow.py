def grow(s, r):  # 文字列sと繰り返し回数rを入力
    n = len(s)  # 入力した文字列の長さ
    ss = ' '  # 出力する文字列を初期化
    for i in range(n):
        if s[i] == 'f':  # ' f'  を ' fg'  に書き換え
            ss = ss + 'fg'
        else:
            if s[i] == 'g':  # ' g'  を ' gh'  に書き換え
                ss = ss + 'gh'
            else:
                ss = ss + 'h'  # その他の文字（h）のときそのまま
    print(ss)
    r -= 1  # 残りの繰返し回数を1減らす
    if r > 0:  # 繰返し回数が0でない時，自分自身を呼び出す
        ss = grow(ss, r)
    return ss

grow('fgh', 2)  # growを2回実行