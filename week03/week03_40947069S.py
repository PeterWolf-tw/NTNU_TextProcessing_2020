#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import re
def textReadAndPrint(txtFILE):
    """讀入指定的純文字 txtFILE 檔案路徑，並回傳該檔案的內容。"""
    with open(txtFILE, encoding="utf-8") as f:
        txtContent = f.read()
    return txtContent

def jsonFileWriter(jsonDICT, jsonFileName):
    """轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

def jsonFileReader(jsonFileName):
    with open(jsonFileName,"r") as f:
        jsonContent=json.load(f)
    return print(jsonContent)

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

    jsonDICT["name"]["zh"]      = txt.split("\n")[0].split(" ")[1]
    jsonDICT["name"]["en"]      = " ".join(txt.split("\n")[1].split(" ")[1:])
    jsonDICT["birth"]["year"]   = txt.split("\n")[2].split(" ")[1]
    jsonDICT["birth"]["month"]  = txt.split("\n")[2].split(" ")[3]
    jsonDICT["birth"]["date"]   = txt.split("\n")[2].split(" ")[5]
    jsonDICT["job"]             = txt.split("\n")[3].split("\t")[1]
    jsonDICT["language"]        = txt.split("\n")[4].split(" ")[1].split("、")[:]
    jsonDICT["education"]       = txt.split("\n")[5].split(" ")[1].split("、")[:]
    jsonDICT["spouse"]          = txt.split("\n")[6].split(" ")[1].split("（")[0]
    
    print(jsonDICT)
    jsonFileName = "week03_40947069S.json"
    jsonFileWriter(jsonDICT, jsonFileName)
    jsonFileReader(jsonFileName)
