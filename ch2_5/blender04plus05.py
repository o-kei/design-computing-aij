import bpy
import copy              # オブジェクトをコピーするためのモジュールcopyをインポート
import math


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
    
    
#camera_setting
########################################

bpy.ops.object.camera_add(location=(0, 0, 15.5),rotation=(math.pi/4, 0, math.pi/2))
camera=bpy.data.objects['Camera']
world=bpy.data.worlds['World']
d_camera=bpy.data.cameras['Camera']

world.light_settings.use_environment_light=True#環境光を使用
world.light_settings.use_indirect_light=True#間接光を使用

d_camera.shift_x=0.12#レンダリング範囲の調整
d_camera.shift_y=0.064

scene.render.resolution_x=1200#解像度の指定
scene.frame_end=260#レンダリングを行う最後のフレームの設定

T_START=0
current_frame = T_START
for i in range(n):#図形が出現するタイミング,カメラの設定
    cube=bpy.data.objects[C_O[i]]
    cube.hide_render = True
    cube.hide = True
    cube.keyframe_insert(data_path="hide_render",frame=current_frame)
    cube.keyframe_insert(data_path="hide",frame=current_frame)

    current_frame = T_START+i
    cube.hide_render = False
    cube.hide = False
    cube.keyframe_insert(data_path="hide_render",frame=current_frame)
    cube.keyframe_insert(data_path="hide",frame=current_frame)

    camera.location=(30*math.cos(2*math.pi/n*i)+10,30*math.sin(2*math.pi/n*i)+10,30)
    camera.rotation_euler = (10*math.pi/36, 0, math.pi/2+2*math.pi/n*i)
    camera.keyframe_insert(data_path="location",frame=current_frame)
    camera.keyframe_insert(data_path="rotation_euler",frame=current_frame)
