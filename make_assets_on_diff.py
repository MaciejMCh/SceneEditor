import git
import json
import os

with open('config.json') as configurationPayload:    
    configuration = json.load(configurationPayload)
blenderFilePath = configuration['blend_file_path']
blenderFileRepoPath = configuration['blend_file_repo_path']

repo = git.Repo(blenderFileRepoPath)
blenderFilePathRelativeToRepo = blenderFilePath.replace(blenderFileRepoPath, '')
git = repo.git
if str(git.status(blenderFilePathRelativeToRepo)).find('clean') == -1:
	os.system('python make_assets.py')