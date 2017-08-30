from graphillion import GraphSet         # graphillionのクラスGraphSetをインポート
# graphillionのモジュールtutorialをtlという名前でインポート
import graphillion.tutorial as tl

universe = tl.grid(2, 2)           # 2x2のグリッドを生成
GraphSet.set_universe(universe)
# 必ず存在する辺と必ず存在しない辺を定義
lines = GraphSet({'include': [(8, 9), (5, 8), (4, 5)], 'exclude': [(6, 9)]})
# 全域木を生成
trees = GraphSet.trees(is_spanning=True)
common = trees & lines
# 結果の描画
for path in common:
    tl.draw(path)
