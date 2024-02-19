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

from collections import defaultdict

# used dictionary to catch all key value pairs
claims_list = defaultdict(list) # used this as there may be more than one value for each key

for k,v in claims.items():
    #claims_list[k]=0
    #print(k)
    if isinstance(v, list):
        #print("item value is list")
        if isinstance(v[0]["mainsnak"]["datavalue"]["value"],dict):
            #print(v[0]["mainsnak"]["datavalue"]["value"])
            for k1,v1 in v[0]["mainsnak"]["datavalue"]["value"].items():
                if k1 == "numeric-id":
                    claims_list[k].append(v1)
                    #print("test") # process value here

        if isinstance(v[0]["mainsnak"]["datavalue"]["value"], str):
            #print(v[0]["mainsnak"]["datavalue"]["value"])
            try:
                int_value = int(v[0]["mainsnak"]["datavalue"]["value"])
                claims_list[k].append(int_value)
            except ValueError:
                # Handle the exception
                continue
        else:
            continue

claims_list_sorted = sorted(zip(claims_list.values(),claims_list.keys()))

# Task 4 - Provide a search functionality which X matched value,
# search will look into datavalue.value and datavalue.datatype.
# Search partial text match .

# use of generator yield function

#property value = douglas-adams
search_term = ["douglas","duglas","8","84","str"]
search_list = []

for k,v in claims.items():
    if isinstance(v[0]["mainsnak"]["datavalue"]["value"],dict):
        #print(v[0]["mainsnak"]["datavalue"]["value"])
        for each_val in v[0]["mainsnak"]["datavalue"]["value"].values():
            #print(each_val)
            for term in search_term:
                if term.lower() in str(each_val):
                    search_list.append(each_val)
    else:
        #print(v[0]["mainsnak"]["datavalue"]["value"].lower())
        for term in search_term:
            if term.lower() in v[0]["mainsnak"]["datavalue"]["value"].lower():
                search_list.append(v[0]["mainsnak"]["datavalue"]["value"].lower())

    for term in search_term:
        if term.lower() in v[0]["mainsnak"]["datavalue"]["type"]:
            search_list.append(v[0]["mainsnak"]["datavalue"]["type"])


# Task 5 - if datavalue.value is number,
# print the min and max for that property value.
# if groupby option is provided,
# groupby will work on P???.datatype .

min_value = min(zip(claims_list.values(), claims_list.keys()))
max_value = max(zip(claims_list.values(), claims_list.keys()))





