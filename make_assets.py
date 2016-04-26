import sys
import os
import json

absolutePath = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '')

# Read config
with open(os.path.join(absolutePath, 'config.json')) as configurationPayload:    
    configuration = json.load(configurationPayload)
blenderFilePath = os.path.join(absolutePath, configuration['blend_file_path'])
resultOutputPath = os.path.join(absolutePath, configuration['assets_output_path'])
blenderAppPath = os.path.join(absolutePath, configuration['blender_app_path'])

os.system('mkdir -p' + resultOutputPath)

os.system('rm -rf ' + resultOutputPath + '/meshes')
os.system('rm -rf ' + resultOutputPath + '/scenes')
os.system('rm -rf ' + resultOutputPath + '/materials')

os.system('mkdir ' + resultOutputPath + '/meshes')
os.system('mkdir ' + resultOutputPath + '/scenes')
os.system('mkdir ' + resultOutputPath + '/materials')

# Export .blend
os.system(blenderAppPath + ' ' + blenderFilePath + ' --background --python ' + os.path.join(absolutePath, 'export_blend.py') + ' -- ' + resultOutputPath)