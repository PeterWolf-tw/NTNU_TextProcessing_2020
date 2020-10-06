import json

with open('example/example.txt', 'r', encoding='utf-8') as f:
    # read txt to data
    lines = f.read()
    print(lines)
    data = {}
    for line in lines.split('\n'):
        element = line.split()
        data[element[0]] = ' '.join(element[1:])

# convert dat to json
jDict = {
    "name": {"zh": "", "en": ""},
    "birth": {"year": "", "month": "", "date": ""},
    "job": "",
    "language": [],
    "education": [],
    "spouse": ""
}

jDict["name"]["zh"] = data['中文名']
jDict["name"]["en"] = data['英文名']
jDict["birth"]["year"] = data['出生'].split()[0]
jDict["birth"]["month"] = data['出生'].split()[2]
jDict["birth"]["date"] = data['出生'].split()[4]
jDict["job"] = data['職業'][1]
jDict["language"] = data['語言'].split('、')
jDict["education"] = data['教育程度'].split("、")[:]
jDict["spouse"] = data['配偶'].split("（")[0]

# write json file
with open('./week03_40847031S.json', 'w', encoding='UTF-8') as f:
    json.dump(jDict, f, indent=4, ensure_ascii=False, separators=(',', ':'))

# print json
with open('./week03_40847031S.json', 'r', encoding='UTF-8') as f:
    print(f.read())
