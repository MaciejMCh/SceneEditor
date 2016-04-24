import sys
import os
import json

# Read config
with open('config.json') as configurationPayload:    
    configuration = json.load(configurationPayload)
blenderFilePath = configuration['blend_file_path']
resultOutputPath = configuration['assets_output_path']

os.system('mkdir ' + resultOutputPath)
os.system('mkdir ' + resultOutputPath + '/meshes')
os.system('mkdir ' + resultOutputPath + '/scenes')

# Export .blend
os.system('/Applications/blender.app/Contents/MacOS/blender ' + blenderFilePath + ' --background --python export_blend.py -- ' + resultOutputPath)