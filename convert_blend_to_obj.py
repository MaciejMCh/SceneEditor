import bpy
import sys
 
argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"
 
obj_out = argv[0]

# Export model space .obj
bpy.ops.object.select_pattern(pattern='*_model', extend=False)
bpy.ops.export_scene.obj(filepath=obj_out+'_model.obj', use_selection=True, axis_forward='-Z', axis_up='Y')

# Export scene .dao
bpy.ops.object.select_all(action='INVERT')
bpy.ops.export_scene.obj(filepath=obj_out+'_scene.obj', use_selection=True, axis_forward='-Z', axis_up='Y')