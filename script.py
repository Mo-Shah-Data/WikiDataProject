import sys
from urllib.request import urlretrieve


id_q_1 = str(sys.argv[1])
url = 'https://www.wikidata.org/wiki/Special:EntityData/{}.json'.format(id_q_1)
filename_1 = '{}.json'.format(id_q_1)

urlretrieve(url, filename_1)

id_q_2 = str(sys.argv[2])
url = 'https://www.wikidata.org/wiki/Special:EntityData/{}.json'.format(id_q_2)
filename_2 = '{}.json'.format(id_q_2)

urlretrieve(url, filename_2)

# load and join
import json
import os


json_file_1 = id_q_1 + ".json"

with open(json_file_1, "r+") as f:
    data_1 = json.load(f)
    print("1st File")


json_file_2 = id_q_2 + ".json"

with open(json_file_2, "r+") as f:
    data_2 = json.load(f)
    print("2nd File")


#################### Delete following after testing#



json_file_1 = "Q42" + ".json"

with open(json_file_1, "r+") as f:
    data_1 = json.load(f)

terms_for_next_iteration = ["entities"]
terms_for_action = ["claims"]

for k, v in data_1.items():
    if k in terms_for_next_iteration:
        for k1,v1 in data_1[k].items(): # first nested dict
            if k1.startswith("Q"):
                Q = k1 # Q extracted
            for k2,v2 in data_1[k][k1].items():
                #print(k2)
                if k2 in terms_for_action:
                    if k2 == "claims":
                        claims_1 = v2
                    else:
                        continue



json_file_2 = "Q43" + ".json"

with open(json_file_2, "r+") as f:
    data_2 = json.load(f)

for k, v in data_2.items():
    if k in terms_for_next_iteration:
        for k1,v1 in data_2[k].items(): # first nested dict
            if k1.startswith("Q"):
                Q = k1 # Q extracted
            for k2,v2 in data_2[k][k1].items():
                #print(k2)
                if k2 in terms_for_action:
                    if k2 == "claims":
                        claims_2 = v2
                    else:
                        continue

print("Values in both")
print(claims_1.keys() & claims_2.keys())
print("Values in first but not in second")
print(claims_1.keys() - claims_2.keys())
print("values in second but not in first")
print(claims_2.keys() - claims_1.keys())
print("Common values for the same key")
print(claims_1.items() & claims_2.items()) # Is this correct?


