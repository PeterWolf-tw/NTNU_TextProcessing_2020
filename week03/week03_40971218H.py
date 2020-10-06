#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
def ReadandPrint(txtFile):
    with open(txtFile, encoding='UTF-8') as F:
        txtContext= F.read()
        return txtContext
def WriteJSON(jsonDICT, jsonFileName):
    with open(jsonFileName, "w") as F:
        json.dump(jsonDICT, F, ensure_ascii=False)
    return None

if __name__== "__main__":
    txtFile='example.txt'
    txt=ReadandPrint(txtFile)

    jsonDICT = {
        "name": {"ch": "", "en": ""},
        "birth": {"year": "", "month": "", "date": ""},
        "job": "",
        "language": "",
        "education": "",
        "spouse": ""
    }

    jsonDICT["name"]["ch"] = txt.split("\n")[0].split(" ")[1]
    jsonDICT["name"]["en"] = " ".join(txt.split("\n")[1].split(" ")[1:])
    jsonDICT["birth"]["year"] = txt.split("\n")[2].split(" ")[1]
    jsonDICT["birth"]["month"] = txt.split("\n")[2].split(" ")[3]
    jsonDICT["birth"]["date"] = txt.split("\n")[2].split(" ")[5]
    jsonDICT["job"] = txt.split("\n")[3].split("\t")[1]
    jsonDICT["language"] = txt.split("\n")[4].split(" ")[1:]
    jsonDICT["education"] = txt.split("\n")[5].split(" ")[1:]
    jsonDICT["spouse"] = txt.split("\n")[6].split(" ")[1].split("（")[0]

    jsonFileName = "week03_40971218H.json"
    WriteJSON(jsonDICT, jsonFileName)
    print(jsonDICT)

