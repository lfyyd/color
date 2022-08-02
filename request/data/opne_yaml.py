import yaml


def read_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
    return value
