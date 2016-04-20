import sys
import os

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"
blenderFileName = argv[0]
resultPath = blenderFileName.replace('.blend', '') + '/'

# Export .blend
os.system('/Applications/blender.app/Contents/MacOS/blender ' + blenderFileName + ' --background --python export_blend.py -- ' + resultPath)
# Process .cae
os.system('python process_dae.py -- ' + resultPath + 'scene.dae')
# Delete .dae
os.system('rm ' + resultPath + 'scene.dae')