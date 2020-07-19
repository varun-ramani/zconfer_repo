import os, json

def create_module_list():
    modules = os.listdir('.')
    for entry in ['generate.py', '.git', 'repo.json', 'README.md']:
        if entry in modules:
            modules.remove(entry)

    return modules

repo = {}

for module in create_module_list():
    with open(f'{module}/info.json', 'r') as jsonfile:
        repo[module] = json.loads(jsonfile.read())

repo = {key: repo[key] for key in sorted(repo)}


with open('repo.json', 'w+') as repofile:
    repofile.write(json.dumps(repo, indent=4))
