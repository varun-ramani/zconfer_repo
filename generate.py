import os, json

repo = {
    'plugins': {},
    'themes': {}
}

for plugin in os.listdir('plugins'):
    with open(f'plugins/{plugin}/info.json', 'r') as jsonfile:
        repo['plugins'][plugin] = json.loads(jsonfile.read())

repo['plugins'] = {key: repo['plugins'][key] for key in sorted(repo['plugins'])}

for theme in os.listdir('themes'):
    with open(f'themes/{theme}/info.json', 'r') as jsonfile:
        repo['themes'][theme] = json.loads(jsonfile.read())

repo['themes'] = {key: repo['themes'][key] for key in sorted(repo['themes'])}

with open('repo.json', 'w+') as repofile:
    repofile.write(json.dumps(repo, indent=4))
