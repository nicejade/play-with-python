import os
import yaml


def get_config(field):
    path = os.path.join(".", "config.yaml")
    print(path)
    file = open(path, "r", encoding="utf-8")
    file_data = file.read()
    file.close()

    config = yaml.load(file_data)
    return config[field]
