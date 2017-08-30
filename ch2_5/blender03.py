import bpy

# 立方体の頂点座標と辺・頂点の接続関係
nodes=[[0,0,0], [1,0,0], [1,1,0], [0,1,0],
       [0,0,1], [1,0,1], [1,1,1], [0,1,1]]

faces=[[0,1,2,3], [4,5,6,7], [0,4,5,1],
       [1,2,6,5], [3,2,6,7], [0,3,7,4]]

mesh_data = bpy.data.meshes.new('cube_mesh_data')   #メッシュデータを作成
cube_object = bpy.data.objects.new('cube_object', mesh_data) #立方体オブジェクトを作成

scene = bpy.context.scene                #シーンを作成
scene.objects.link(cube_object)          #オブジェクトを現在のシーンにリンク

mesh_data.from_pydata(nodes, [], faces)  #頂点と面のリストをメッシュデータに追加
mesh_data.update()                       #編集したデータを更新