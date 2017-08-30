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
