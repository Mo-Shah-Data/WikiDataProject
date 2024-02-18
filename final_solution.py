import operator
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


for k,v in claims.items():
    print(k, v)

for k,v in labels.items():
    print(k, v)

# Task 3 -0 because not all of the claims had mainsnak.datavalue
### itemgetter did not work, cannot get to nested dict keys
from operator import itemgetter

print(type(claims)) # confirm structure
claims_by_mainsak_datavalue = sorted(claims, key=itemgetter(0))

q= itemgetter(0)
w= itemgetter(1)
e= itemgetter(2)
r= itemgetter(3)

test = itemgetter(claims)

# sorted with lambda function - got no where

claims_by_mainsak_datavalue = sorted(claims, key=itemgetter(0))

print(claims["P1005"][0]["mainsnak"]["datavalue"])
print(claims["P1005"][0]["mainsnak"]["datavalue"]["value"])

# used dictionary to catch all key value pairs
claims_list = {}
for k,v in claims.items():
    #claims_list[k]=0
    #print(k)
    if isinstance(v, list):
        #print("item value is list")
        if isinstance(v[0]["mainsnak"]["datavalue"]["value"],dict):
            #print(v[0]["mainsnak"]["datavalue"]["value"])
            for k1,v1 in v[0]["mainsnak"]["datavalue"]["value"].items():
                if k1 == "numeric-id":
                    claims_list[k] = v1
                    #print("test") # process value here

        if isinstance(v[0]["mainsnak"]["datavalue"]["value"], str):
            #print(v[0]["mainsnak"]["datavalue"]["value"])
            try:
                int_value = int(v[0]["mainsnak"]["datavalue"]["value"])
                claims_list[k] = int_value
            except ValueError:
                # Handle the exception
                continue
        else:
            continue

claims_list_sorted = sorted(zip(claims_list.values(),claims_list.keys()))

# Task 4








