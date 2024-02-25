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
        elif data[k][Q]["claims"]:
            claims = data[k][Q]["claims"]
        else:
            continue


# Task 3
# Sort Claims with mainsnak.datavalue.
# extract claims and mainsak.datavalue

from operator import itemgetter

from collections import defaultdict


claims_by_numeric_id = defaultdict(list)

for k,v in claims.items():
    for i in v:
        #print(i)
        if not i["mainsnak"]["datavalue"]["type"] == "time": # there are more nested dicts under here with numeric-ids work on this later
            #print(i["mainsnak"]["datavalue"]["value"])
            claims_by_numeric_id[k].append(i["mainsnak"]["datavalue"]["value"])

        elif i["mainsnak"]["datavalue"]["type"] == "time":
            #print(i["mainsnak"]["datavalue"]["value"]["time"])
            claims_by_numeric_id[k].append(i["mainsnak"]["datavalue"]["value"]["time"]) # may need to use a different dict

        # need to get valeus from nested dicts now












            claims_by_numeric_id[k].append(i["mainsnak"]["datavalue"]["value"]["numeric-id"])

# sort the default dict
            for each_value in claims_by_numeric_id.items():
                print(each_value)

                    each_value[1].sort()

claims_by_numberic_id_sorted = sorted(claims_by_numeric_id)


import array as arr
# Create an array of integer type
my_array = arr.array('u', ['1', '2', '3', '4', '5'])



# 4- Provide a search funcationlity which X matched value, search will look into datavalue.value and datavalue.datatype.
# Search partial text match .

def search(search_pattern):
    search_pattern = search_pattern.lower()
    for k,v in claims.items():
        for i in v:
            if search_pattern in str(i["mainsnak"]["datavalue"]["value"]).lower():
                list_of_found_terms.append(i["mainsnak"]["datavalue"]["value"])
            elif search_pattern in str(i["mainsnak"]["datavalue"]["type"]).lower():
                list_of_found_terms.append(i["mainsnak"]["datavalue"]["type"])
            else:
                continue

list_of_found_terms = []
search("wiki")

# 5- if datavalue.value is number, print the min and max for that property value.
# if groupby option is provided, groupby will work on P???.datatype .