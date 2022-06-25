import yaml


def loadyaml(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data

# import yaml
#
# with open("./color.yaml", 'r', encoding='utf-8') as f:
#     data = yaml.load(f)
#
# print(data)

# a = loadyaml('./color.yaml')
# print(a)
# print(type(a))


# a = loal('./aa.py')
# b = loadyaml('./color.yaml')
# print(a)
# print(type(a))
# print(b)
# print(type(b))dyam
