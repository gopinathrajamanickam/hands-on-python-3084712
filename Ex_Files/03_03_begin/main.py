import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN)  # dict to json
back_to_dict = json.loads(einstein_json)  # json to dict
print(f" einstein_json file is {einstein_json}")
pprint(einstein_json)
print("Back to dict ")
pprint(back_to_dict)


with open("laureates.csv", "r") as f:  # f is the file object
    reader = csv.DictReader(f)
    laureates = list(reader)

print(f"Type of reader : {type(reader)}")
print(f"Type of laureates : {type(laureates)}")

with open("laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)
