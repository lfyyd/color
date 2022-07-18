import yaml


def loadyaml(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)
    return data

loadyaml('./test.yaml')
