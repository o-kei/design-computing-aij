from turtle import *  # 描画環境 turtle をインポート
from rose import *  # plot1.pyと同一フォルダにあるrose.pyをインポート
hideturtle()
rose_window_recursion(
    [[-100, -100], [100, -100], [100, 100], [-100, 100]], 0.1, 40)
done()  # turtleの終了処理