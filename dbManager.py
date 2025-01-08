import json

factionsSaveFile = "./factions.json"

def loadJson(path):
    file = None
    with open(path, "tr") as f:
        file = json.load(f)

    return file

def appendJson(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def addFaction(name, description, roleId):
    file : dict = loadJson(factionsSaveFile)
    file[name] = {
        "name": name,
        "description": description,
        "role": roleId,
        "members": {

        }
    }
    appendJson(factionsSaveFile, file)