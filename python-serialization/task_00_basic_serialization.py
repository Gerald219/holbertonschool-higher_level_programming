#!/usr/bin/env python3

import json



def serialize_and_save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


def load_and_deserialize(filename):
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
