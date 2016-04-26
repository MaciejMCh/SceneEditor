import git
import json
import os

absolutePath = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '')

with open(os.path.join(absolutePath, 'config.json')) as configurationPayload:    
    configuration = json.load(configurationPayload)
blenderFilePath = os.path.join(absolutePath, configuration['blend_file_path'])
blenderFileRepoPath = os.path.join(absolutePath, configuration['blend_file_repo_path'])

repo = git.Repo(blenderFileRepoPath)
blenderFilePathRelativeToRepo = blenderFilePath.replace(blenderFileRepoPath, '')
git = repo.git
if str(git.status(blenderFilePathRelativeToRepo)).find('clean') == -1:
	os.system('python ' + os.path.join(absolutePath, 'make_assets.py'))