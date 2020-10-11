#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def textReadAndPrint(txtFile):
    with open(txtFile, encoding="utf-8") as f:
        txtContent = f.read()
    return txtContent

def jsonFileWriter(jsonDICT,jsonFileName):
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

if __name__ == "__main__":
    txtFilePath = "./example/example.txt"
    txt = textReadAndPrint(txtFilePath)
    jsonDICT = { 
    "name": {"zh":"", "en":""},
    "birth": {"year":"", "month":"", "date":""},
    "job": "",
    "language":[],
    "education":[],
    "spouse":""
    }

    jsonDICT["name"]["zh"] = txt.split("\n")[0].split(" ")[1]
    jsonDICT["name"]["en"] = " ".join(txt.split("\n")[1].split(" ")[1:])
    jsonDICT["birth"]["year"] = txt.split("\n")[2].split(" ")[1]
    jsonDICT["birth"]["month"] = txt.split("\n")[2].split(" ")[3]
    jsonDICT["birth"]["date"] = txt.split("\n")[2].split(" ")[5]
    jsonDICT["job"]= txt.split("\n")[3].split("\t")[1]
    jsonDICT["language"] = txt.split("\n")[4].split(" ")
    jsonDICT["education"] = txt.split("\n")[5].split(" ")
    jsonDICT["spouse"] = txt.split("\n")[6].split(" ")[1].split("(")[0]

    print(jsonDICT)
    jsonFileName = "Week03_40775006h.json"
    jsonFileWriter(jsonDICT, jsonFileName)
