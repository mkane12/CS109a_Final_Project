__author__ = 'nishaswarup'
import json

json_file = 'json_2015.json'
json_data = open(json_file)
data = json.load(json_data)
funny_words = {}
useful_words = {}

for review in data:
    if review['funny'] > 5:
