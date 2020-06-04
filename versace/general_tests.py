import pandas as pd
import json


file = pd.read_csv('versace.csv')


def extract_data(value):
    d = {}
    for i in set(value):
        d[i] = list(value).count(i)
    return d


def extract_size(value):
    d = []
    for j in set(value):
        for i in j.split(','):
            d.append(i)
    return d


all_website_items = file.count().product_category
items_in_region = extract_data(file['product_region'])
items_currency = extract_data(file['product_currency'])
items_size = extract_size(file['product_size'])
size = extract_data(items_size)
items_colour = extract_data(file['product_colour'])
to_json = {'All items on Website': str(all_website_items), 'Correct currency': items_currency,
           'Items region': items_in_region, 'Items size': size, 'Items colour': items_colour}

with open('versace.json', 'w') as f:
    json.dump(to_json, f, sort_keys=True, indent=2)
