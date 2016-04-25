import sys
import os
import json

# Read config
with open('config.json') as configurationPayload:    
    configuration = json.load(configurationPayload)
blenderFilePath = configuration['blend_file_path']
resultOutputPath = configuration['assets_output_path']
blenderAppPath = configuration['blender_app_path']

os.system('mkdir ' + resultOutputPath)

os.system('rm -rf ' + resultOutputPath + '/meshes')
os.system('rm -rf ' + resultOutputPath + '/scenes')
os.system('rm -rf ' + resultOutputPath + '/materials')

os.system('mkdir ' + resultOutputPath + '/meshes')
os.system('mkdir ' + resultOutputPath + '/scenes')
os.system('mkdir ' + resultOutputPath + '/materials')

# Export .blend
os.system(blenderAppPath + ' ' + blenderFilePath + ' --background --python export_blend.py -- ' + resultOutputPath)