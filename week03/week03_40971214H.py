#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def txtReadAndPrint(txtFILE):
    """讀取txt文字檔，並印在螢幕上。"""
    with open(txtFILE, encoding="utf-8") as f:
        txtContent = f.read()
    return txtContent

def jsonFileWriter(jsonDICT, jsonFileName):
    """Convert jsonDICT into a jsonFILE and save it by jsonFILEName"""
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)

if __name__ == "__main__":
    txtFilePath = "./example/example.txt"
    txt = txtReadAndPrint(txtFilePath)
    print(txt)

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
jsonDICT["birth"]["year"] = txt.split("\n")[2].split(" ")[5]
jsonDICT["job"] = txt.split("\n")[3].split("\t")[1]
jsonDICT["language"] = txt.split("\n")[4].split(" ")
jsonDICT["education"] = txt.split("\n")[5].split(" ")
jsonDICT["spouse"] = txt.split("\n")[6].split(" ")[1].split("（")[0]

print(jsonDICT)
jsonFileName = "week03_40971214H.json"
jsonFileWriter(jsonDICT, jsonFileName)