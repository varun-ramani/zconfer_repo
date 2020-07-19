import os, json

repo = {
    'plugins': {},
    'themes': {}
}

for plugin in os.listdir('plugins'):
    with open(f'plugins/{plugin}/info.json', 'r') as jsonfile:
        repo['plugins'][plugin] = json.loads(jsonfile.read())

repo['plugins'] = {key: repo['plugins'][key] for key in sorted(repo['plugins'])}

with open('repo.json', 'w+') as repofile:
    repofile.write(json.dumps(repo, indent=4))
