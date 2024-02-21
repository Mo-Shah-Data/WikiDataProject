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
# Make sure file is already loaded
# def sort_dict(dict):
#     return False

# claim numbers for testing

for key in data["entities"]["Q42"]["claims"]:
    print(key)


for key in data["entities"]["Q42"]["claims"]["P11182"][0]["mainsnak"]["datavalue"]["value"]:
    print(key)

# search in mainsnak
for key in data["entities"]["Q42"]["claims"]["P11182"][0]["mainsnak"]["datavalue"]["value"].keys():
    if key == "numeric-id":
        if data["entities"]["Q42"]["claims"]["P11182"][0]["mainsnak"]["datavalue"]["value"]:
            print(data["entities"]["Q42"]["claims"]["P11182"][0]["mainsnak"]["datavalue"]["value"]["numeric-id"])


# search in others - to ask AR

for key in data["entities"]["Q42"]["claims"]["P69"][0]["references"]:
    print(key)




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



## Final Solutions after reading chapter

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
    data = json.load(f)

level1 = {key:value for key, value in data.items() for key in value}

# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#
# # Make a dictionary of all prices over 200
# p1 = {key: value for key, value in prices.items() if value > 200}
#
# # Make a dictionary of tech stocks
# tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# p2 = {key: value for key, value in prices.items() if key in tech_names}

import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(stuff)

pp.pprint(data)