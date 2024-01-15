from urllib.request import urlretrieve


# Task 1 Query and download from endpoint

id_q = 'Q42'
url = 'https://www.wikidata.org/wiki/Special:EntityData/{}.json'.format(id_q)
filename = '{}.json'.format(id_q)

urlretrieve(url, filename)

# Task 2 - Extract entities.Q??.labels and entities.Q??.claims.P?? .

import json
import os

entities = []
id_q = 'Q42'
json_file = id_q + ".json"
with open(json_file, "r+") as f:
    data = json.load(f)
    # print(data["entities"])
    key_list = list(data.keys())

    # Testing to here

    for key in data.keys():
        if key == "entities":
            entities = next(data["entities"])
            print(entities)
        print(key,data[key])

    # Check its class
    # print(type(data))

    # # Entities
    # entity_item = id_q
    # # Labels
    # labels_and_entities=[]
    # print(data["entities"][entity_item]["labels"],id_q)




    # entities = data.get("entities")
    # json.dump(data,f,indent=2)

#print(data)
print(entities)
print(json.dumps(data,indent=2))

# the json file where the output must be stored
out_file = open("test.json", "w")
json.dump(data, out_file, indent=2)
out_file.close()



## testing gorund
# extract key from dict