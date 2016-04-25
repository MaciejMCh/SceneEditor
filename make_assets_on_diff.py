import git
import json
import os

with open('config.json') as configurationPayload:    
    configuration = json.load(configurationPayload)
blenderFilePath = configuration['blend_file_path']
blenderFileRepoPath = configuration['blend_file_repo_path']

repo = git.Repo(blenderFileRepoPath)
blenderFilePathRelativeToRepo = blenderFilePath.replace(blenderFileRepoPath, '')
if repo.is_dirty(blenderFilePathRelativeToRepo):
	print os.system('python make_assets.py')