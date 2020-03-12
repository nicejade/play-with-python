import json


def print_list(list):
    print("\n".join("{}: {}".format(*k) for k in enumerate(list)))


def print_json(param):
    print(json.dumps(param, sort_keys=True, indent=4, ensure_ascii=False))
