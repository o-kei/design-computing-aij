import bpy
import copy              # オブジェクトをコピーするためのモジュールcopyをインポート

def move(box,l,stack,s,t):  # 図形をコピーして移動する操作

    box_2 =copy.deepcopy(box)  # boxをbox_2にコピー
    n=len(box_2)

    for i in range(n):
        for j in range(8):
            box_2[i][j][s]+=l    # s方向に l だけ移動
            box_2[i][j][t]+=l    # t方向に l だけ移動

    stack.extend(box_2)         # スタックにコピー

########################################
# 立方体の頂点座標と辺・頂点の接続関係
verts=[[[0,0,0], [1,0,0], [1,1,0], [0,1,0],
        [0,0,1], [1,0,1], [1,1,1], [0,1,1]]]

faces=[[0, 1, 2, 3], [4, 5, 6, 7], [0, 4, 5, 1],
       [1, 2, 6, 5], [3, 2, 6, 7], [0, 3, 7, 4]]

stack=[]     # 立方体を保存するためのスタックの初期化

l=1         # 立方体を移動する量の初期値
########################################

#フラクタル図形の生成，初期値では3回繰り返し
for i in range(3):
    move(verts,l,stack,1,2)
    move(verts,l,stack,0,1)
    move(verts,l,stack,0,2)
    verts.extend(stack)
    stack=[]
    l=l*2

# 変数の初期化
m_d=[]
c_m_d=[]
c_o=[]
C_O=[]

n=len(verts)

#blnder上に図形を描画するための設定
for i in range(n):
    m_d.append("mesh_data_"+str(i))
    c_m_d.append("cube_mesh_data_"+str(i))
    c_o.append("cube_object"+str(i))
    C_O.append("Cube_Object"+str(i))

    m_d[i] = bpy.data.meshes.new(c_m_d[i])
    m_d[i].from_pydata(verts[i], [], faces)
    m_d[i].update()
    c_o[i] = bpy.data.objects.new(C_O[i], m_d[i])

scene = bpy.context.scene

for i in range(n):
    scene.objects.link(c_o[i])