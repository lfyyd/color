from request.data.opne_yaml import read_yaml



print(read_yaml('../data/login.yaml'))

data = read_yaml('../data/login.yaml')
print(data[0]["request"]["url"])
print(data[0]["request"]["datas"])
print(data[0]["request"]["method"])