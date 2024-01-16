import json
import uuid

data = None
with open("packs.json", "r", encoding="utf-8") as packs_file:
    data = json.load(packs_file)

for pack in data["packs"]:
    pack["id"] = str(uuid.uuid4())
    for person in pack["people"]:
        person["id"] = str(uuid.uuid4())

with open("packs2.json", "w", encoding="utf-8") as packs_file:
    json.dump(data, packs_file, indent=4)
