import sys
import os
import json

# Read config
with open('config.json') as configurationPayload:    
    configuration = json.load(configurationPayload)
blenderFilePath = configuration['blend_file_path']
resultOutputPath = configuration['assets_output_path']
removeCollada = configuration['remove_collada']

os.system('mkdir ' + resultOutputPath)
os.system('mkdir ' + resultOutputPath +'/mesh')

# Export .blend
os.system('/Applications/blender.app/Contents/MacOS/blender ' + blenderFilePath + ' --background --python export_blend.py -- ' + resultOutputPath)
# Process .cae
os.system('python process_dae.py -- ' + resultOutputPath + '/scene/collada.dae')

# Delete .dae
if removeCollada:
	os.system('rm ' + resultOutputPath + '/scene/collada.dae')