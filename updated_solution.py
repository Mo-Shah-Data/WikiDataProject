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

for k,v in data.items():
    Q = list(v.keys())[0]
    if data[k][Q]["labels"]:
        labels = data[k][Q]["labels"]
    if data[k][Q]["claims"]:
        claims = data[k][Q]["claims"]


# Task 3
# Sort Claims with mainsnak.datavalue.
# extract claims and mainsak.datavalue

#This solution was improved further down in task 5
from collections import defaultdict
from datetime import datetime

claims_by_numeric_id = defaultdict(list)
claims_by_time = defaultdict(list)

for k,v in claims.items():
    for i in v:
        if i["mainsnak"]["datavalue"]["type"] == "wikibase-entityid":  # there are more nested dicts under here with numeric-ids work on this later
            # print(i["mainsnak"]["datavalue"]["value"])
            claims_by_numeric_id[k].append(i["mainsnak"]["datavalue"]["value"]["numeric-id"])
            # need to get values from nested dicts now

        elif i["mainsnak"]["datavalue"]["type"] == "time":
            # print(i["mainsnak"]["datavalue"]["value"]["time"])
            datetime_string = i["mainsnak"]["datavalue"]["value"]["time"]
            adjusted_datetime_string = datetime_string[1:]
            date_format = '%Y-%m-%dT%H:%M:%SZ'
            date_datetime = datetime.strptime(adjusted_datetime_string, date_format)
            claims_by_time[k].append(date_datetime)  # may need to use a different dict
        else:
            continue

sort_by_numeric_id_vals = sorted(claims_by_numeric_id.items(), key=lambda item_value: item_value[1])
sorted_by_datetime_vals = sorted(claims_by_time.items(), key=lambda item_value: item_value[1])


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

sequence_dicts = []

#### I did not know you can have duplicate dicts in a  sequence of dictionaries
for k,v in claims.items():
    for i in v:
        if i["mainsnak"]["datavalue"]["type"] == "wikibase-entityid":  # there are more nested dicts under here with numeric-ids work on this later
            #print(i["mainsnak"]["datavalue"]["value"])
            row_dict = {
                "claim_number": k,
                "numeric_id": i["mainsnak"]["datavalue"]["value"]["numeric-id"]
            }
            sequence_dicts.append(row_dict)
            # need to get values from nested dicts now

        else:
            continue

import pprint
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(sequence_dicts)

# claim 106 will help test the grouping

from operator import itemgetter
from itertools import groupby

sequence_dicts.sort(key=itemgetter("claim_number")) #  sorts only limited characters and needs fixing


#iterate in groups
for claim_num, items in groupby(sequence_dicts, key=itemgetter('claim_number')):
    print(claim_num)
    #pp.pprint(list(items))
    # for i in items:
    #     print(i)
    item_values=list(items)
    min_value = min(item_values, key=itemgetter('numeric_id'))
    print(min_value)
    max_value = max(item_values, key=itemgetter('numeric_id'))
    print(max_value)


import pprint
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(sequence_dicts)