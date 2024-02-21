from urllib.request import urlretrieve

# Task 1 Query and download from endpoint

id_q = 'Q42'
url = 'https://www.wikidata.org/wiki/Special:EntityData/{}.json'.format(id_q)
filename = '{}.json'.format(id_q)

urlretrieve(url, filename)

# Task 2 - Extract entities.Q??.labels and entities.Q??.claims.P?? .
# used https://jsonformatter.org/json-viewer

import json
import os

id_q = 'Q42'
json_file = id_q + ".json"

with open(json_file, "r+") as f:
    data = json.load(f)

for k,v in data.items():   # Did I even need a for loop?
    Q = list(v.keys())[0]
    if data[k][Q]["labels"]:
        labels = data[k][Q]["labels"]
    if data[k][Q]["claims"]:
        claims = data[k][Q]["claims"]


# Task 3
# Sort Claims with mainsnak.datavalue.

