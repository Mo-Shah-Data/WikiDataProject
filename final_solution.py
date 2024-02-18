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

with open(json_file, "r+") as f:
    data = json.load(f)

terms_for_next_iteration = ["entities"]
terms_for_action = ["labels", "claims"]

for k, v in data.items():
    if k in terms_for_next_iteration:
        for k1,v1 in data[k].items(): # first nested dict
            if k1.startswith("Q"):
                Q = k1 # Q extracted
            for k2,v2 in data[k][k1].items():
                #print(k2)
                if k2 in terms_for_action:
                    if k2 == "labels":
                        labels = v2
                    elif k2 == "claims":
                        claims = v2
                    else:
                        continue











