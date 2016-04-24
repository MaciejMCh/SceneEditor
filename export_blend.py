import bpy
import sys
import json
 
argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"
 
storagePath = argv[0]

# Read scenes
scenesJsonArray = []
for scene in bpy.data.scenes:
	sceneJsonObject = {}
	sceneJsonObject['name'] = scene.name
	scenesJsonArray.append(sceneJsonObject)
	objectsJsonArray = []
	sceneJsonObject['renderables'] = objectsJsonArray
	for ob in scene.objects:
		objectJsonObject = {}
		objectJsonObject['name'] = ob.name
		objectJsonObject['mesh'] = ob.data.name
		objectJsonObject['material'] = ob.active_material.name
		objectJsonObject['transformation'] = {}
		objectJsonObject['transformation']['position'] = [ob.location.x, ob.location.y, ob.location.z]
		objectJsonObject['transformation']['rotation'] = [ob.rotation_euler.x, ob.rotation_euler.y, ob.rotation_euler.z]
		objectsJsonArray.append(objectJsonObject)
	with open(storagePath + 'scenes/' + scene.name + '.scene', 'w') as f:
		f.write(json.dumps(sceneJsonObject))
		f.closed

# Copy all meshes to new scene and create objects in model space
bpy.ops.scene.new(type='EMPTY')
modelSpaceScene = bpy.context.scene
modelSpaceScene.name = 'modelSpaceScene'
bpy.data.screens['Default'].scene = bpy.data.scenes['modelSpaceScene']
bpy.context.screen.scene=bpy.data.scenes['modelSpaceScene']
for mesh in bpy.data.meshes:
	modelSpaceObject = bpy.data.objects.new(name=mesh.name, object_data=mesh)
	modelSpaceScene.objects.link(modelSpaceObject)
	print(mesh)

# Export models into separate .objs
for object in bpy.data.meshes:
	bpy.ops.object.select_pattern(pattern=object.name, extend=False)
	bpy.ops.export_scene.obj(filepath=storagePath+'meshes/'+object.name+'.obj', use_selection=True, axis_forward='Y', axis_up='Z', use_triangles=True, use_uvs=True, use_materials=False)
	print(object.name)