#!/usr/bin/python3
import json
import sys

def save_to_json_file(my_obj, filename):
    with open(filename, "w") as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    with open(filename, "r") as file:
        return json.load(file)
#add items to list
items = load_from_json_file("add_item.json") 
if os.path.isfile("add_item.json") else []
for item in sys.argv[1:]:
    items.append(item)
#save items to file
save_to_json_file(items, "add_item.json")
