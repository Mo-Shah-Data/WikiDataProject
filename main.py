import argparse
from urllib.request import urlretrieve
import json
from collections import defaultdict
from datetime import datetime
from operator import itemgetter
from itertools import groupby
import os

def download_file(QID):
    id_q = QID
    url = 'https://www.wikidata.org/wiki/Special:EntityData/{}.json'.format(id_q)
    filename = '{}.json'.format(id_q)
    urlretrieve(url, filename)

def preprocess_file(QID):
    filename = '{}.json'.format(QID)
    id_q = QID
    json_file = id_q + ".json"

    with open(json_file, "r+") as f:
        data = json.load(f)

    for k, v in data.items():
        Q = list(v.keys())[0]
        if data[k][Q]["labels"]:
            labels = data[k][Q]["labels"]
        if data[k][Q]["claims"]:
            claims = data[k][Q]["claims"]

        labels_file_to_create = "{}_labels.json".format(QID)
        with open(labels_file_to_create, 'w') as labels_file:
            json.dump(labels, labels_file, indent=4)

        claims_file_to_create = "{}_claims.json".format(QID)
        with open(claims_file_to_create, 'w') as claims_file:
            json.dump(claims, claims_file, indent=4)

    return claims

def sort_claims(claims):

    claims_by_numeric_id = defaultdict(list)
    claims_by_time = defaultdict(list)

    for k, v in claims.items():
        for i in v:
            if i["mainsnak"]["datavalue"][
                "type"] == "wikibase-entityid":  # there are more nested dicts under here with numeric-ids work on this later
                # print(i["mainsnak"]["datavalue"]["value"])
                claims_by_numeric_id[k].append(i["mainsnak"]["datavalue"]["value"]["numeric-id"])
                # need to get values from nested dicts now

            elif i["mainsnak"]["datavalue"]["type"] == "time":
                # print(i["mainsnak"]["datavalue"]["value"]["time"])
                datetime_string = i["mainsnak"]["datavalue"]["value"]["time"]
                adjusted_datetime_string = datetime_string[1:]
                date_format = '%Y-%m-%dT%H:%M:%SZ'
                try:
                    date_datetime = datetime.strptime(adjusted_datetime_string, date_format)
                except ValueError:
                    continue
                claims_by_time[k].append(date_datetime)  # may need to use a different dict
            else:
                continue

    sorted_claims_by_numeric_id_vals = sorted(claims_by_numeric_id.items(), key=lambda item_value: item_value[1])
    sorted_claims_by_datetime_vals = sorted(claims_by_time.items(), key=lambda item_value: item_value[1])

    # list to file

    with open('sorted_claims_by_numeric_id_vals.csv', 'w') as fp:
        fp.write("\n".join(str(item) for item in sorted_claims_by_numeric_id_vals))
    with open('sorted_claims_by_datetime_vals.csv', 'w') as fp:
        fp.write("\n".join(str(item) for item in sorted_claims_by_datetime_vals))

    return sorted_claims_by_numeric_id_vals

def search(search_pattern,QID, claims):
    search_pattern = search_pattern.lower()
    list_of_found_terms = []
    for k, v in claims.items():
        for i in v:
            if search_pattern in str(i["mainsnak"]["datavalue"]["value"]).lower():
                list_of_found_terms.append(i["mainsnak"]["datavalue"]["value"])
            elif search_pattern in str(i["mainsnak"]["datavalue"]["type"]).lower():
                list_of_found_terms.append(i["mainsnak"]["datavalue"]["type"])
            else:
                continue

    with open('{}_list_of_found_terms.csv'.format(QID), 'w') as fp:
        fp.write("\n".join(str(item) for item in list_of_found_terms))

    return list_of_found_terms
def print_min_max(QID, claims):

    sequence_dicts = []

    for k, v in claims.items():
        for i in v:
            if i["mainsnak"]["datavalue"][
                "type"] == "wikibase-entityid":  # there are more nested dicts under here with numeric-ids work on this later
                # print(i["mainsnak"]["datavalue"]["value"])
                row_dict = {
                    "claim_number": k,
                    "numeric_id": i["mainsnak"]["datavalue"]["value"]["numeric-id"]
                }
                sequence_dicts.append(row_dict)
                # need to get values from nested dicts now

            else:
                continue

    sequence_dicts.sort(key=itemgetter("claim_number"))  # sorts only limited characters and may need fixing

    # iterate in groups
    for claim_num, items in groupby(sequence_dicts, key=itemgetter('claim_number')):
        print(QID,claim_num)
        item_values = list(items)
        min_value = min(item_values, key=itemgetter('numeric_id'))
        print(QID,min_value)
        max_value = max(item_values, key=itemgetter('numeric_id'))
        print(max_value)

def check_values(QID1_claims, QID2_claims):
    # Find pvalues in common
    print("Values common")
    print(QID1_claims.keys() & QID2_claims.keys())

    print("Pvalues in QID1 and not in QID2")
    print(QID1_claims.keys() - QID2_claims.keys())

    print("Pvalues in QID2 and not in QID1")
    print(QID2_claims.keys() - QID1_claims.keys())

    print("items common in both QID1 and QID2")
    print(QID1_claims.items() & QID2_claims.items())



def main():
    parser = argparse.ArgumentParser(description='Download JSON Files')
    parser.add_argument('QID1', type=str, help='a QID for download')
    parser.add_argument('--QID2', type=str, default=False, help='another QID for download')
    parser.add_argument('--search_term', type=str, default=False, help='search term to look for in claims')
    args = parser.parse_args()

    # Download File
    download_file(args.QID1)
    if args.QID2:
        download_file(args.QID2)

    # preprocess file or files
    claims_QID1 = preprocess_file(args.QID1)
    list_of_tems_found_QID1 = search(args.search_term,args.QID1,claims_QID1)
    print_min_max(args.QID1,claims_QID1)
    sort_claims(claims_QID1)

    if args.QID2:
        claims_QID2 = preprocess_file(args.QID2)
        list_of_tems_found_QID2 = search(args.search_term, args.QID2,claims_QID2)
        print_min_max(args.QID2, claims_QID2)
        sort_claims(claims_QID2)

        check_values(claims_QID1,claims_QID2)

if __name__ == "__main__":
    main()
