from urllib.request import urlretrieve


# Task 1 Query and download from endpoint

id_q = 'Q42'
url = 'https://www.wikidata.org/wiki/Special:EntityData/{}.json'.format(id_q)
filename = '{}.json'.format(id_q)

urlretrieve(url, filename)

# Task 2 - Extract entities.Q??.labels and entities.Q??.claims.P?? .

import json
import os


id_q = 'Q42'
json_file = id_q + ".json"

entities = []
labels = []
claims_list = []

with open(json_file, "r+") as f:
    data = json.load(f) # creates dict of length 1
    # print(data["entities"])
    # what data structure is data?
    ## Answer = dict
    key_list = list(data.keys())
    if key_list[0] == "entities":
        #print(True) # to remove
        for entity in data:
            #print(entity)
            for sub_item_1 in data["entities"]:
                if sub_item_1.startswith("Q"):
                    # print(sub_item_1)
                    entities.append(sub_item_1)
                    for sub_item_2 in data["entities"][sub_item_1]:
                        # print(sub_item_2) # check nest dict values
                        if sub_item_2 == "labels":
                            for label in data["entities"][sub_item_1][sub_item_2]:
                                labels.append(label)
                            # print(data["entities"][sub_item_1][sub_item_2]) # to uncomment, as it is required
                            # print(sub_item_2)
                        if sub_item_2 == "claims":
                            # print(data["entities"][sub_item_1][sub_item_2])
                            for claims_q in data["entities"][sub_item_1][sub_item_2]:
                                if claims_q.startswith("P"):
                                    claims_list.append(claims_q)
                                    # print(claims_q)

# Task 3 - Sort Claims with mainsnak.datavalue.

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