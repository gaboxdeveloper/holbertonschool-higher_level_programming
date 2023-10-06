#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python
list, and then save them to a file:
"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []
arguments = sys.argv[1:]
existing_list.extend(arguments)
save_to_json_file(existing_list, "add_item.json")
