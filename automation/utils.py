import os
import yaml


def get_config(field):
    path = os.path.join(".", "config.yaml")
    file = open(path, "r", encoding="utf-8")
    file_data = file.read()
    file.close()

    config = yaml.safe_load(file_data)
    return config[field]
