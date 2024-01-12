from urllib.request import urlretrieve

id_q = 'Q42'
url = 'https://www.wikidata.org/wiki/Special:EntityData/{}.json'.format(id_q)
filename = '{}.json'.format(id_q)

urlretrieve(url, filename)

import json
import os

id_q = 'Q42'
json_file = id_q + ".json"
with open(json_file, "r+") as f:
    data = json.load(f)
    # Entities
    entity_item = id_q
    # Labels
    labels_and_entities=[]
    print(data["entities"][entity_item]["labels"],id_q)




    # entities = data.get("entities")
    # json.dump(data,f,indent=2)

#print(data)
print(entities)
print(json.dumps(data,indent=2))

# the json file where the output must be stored
out_file = open("test.json", "w")
json.dump(data, out_file, indent=2)
out_file.close()

