import bpy
import sys
 
argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"
 
storagePath = argv[0]

# # Export scene .dao
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_same_group(group='WorldSpace')
bpy.ops.wm.collada_export(filepath=storagePath+'scene/collada', selected=True, export_transformation_type_selection='transrotloc')

# Export models into separate .objs
for object in bpy.data.groups['ModelSpace'].objects:
	bpy.ops.object.select_pattern(pattern=object.name, extend=False)
	bpy.ops.export_scene.obj(filepath=storagePath+'mesh/'+object.name+'.obj', use_selection=True, axis_forward='Y', axis_up='Z', use_triangles=True, use_uvs=True, use_materials=False)
	print(object.name)