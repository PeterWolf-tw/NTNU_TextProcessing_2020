#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def textReadAndPrint(txtFILE):
    """讀入指定的純文字 txtFILE 檔案路徑，並回傳該檔案的內容。"""
    with open(txtFILE, encoding="utf-8") as f:
        txtContent = f.read()
    return txtContent

def jsonFileWriter(jsonDICT, jsonFileName):
    """轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
    with open(jsonFileName, mode="w", encoding="utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

if __name__ == "__main__":
    txtFilePath = "./example/example.txt"
    txt = textReadAndPrint(txtFilePath)
    print("example.txt: ")
    print(txt)
    print()

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
    jsonDICT["language"]        = txt.split("\n")[4].split(" ")[1].split("、")
    jsonDICT["education"]       = txt.split("\n")[5].split(" ")[1].split("、")
    jsonDICT["spouse"]          = txt.split("\n")[6].split(" ")[1].split("（")[0]

    #上面這個區塊，有個地方讓電腦一直做一樣的事，似乎有讓它更有效率的寫法，不知道有沒有人想到呢？

    jsonFileName = "week03_40647003S.json"
    jsonFileWriter(jsonDICT, jsonFileName)

    JF = textReadAndPrint(jsonFileName)
    print("week03_40647003S.json: ")
    print(JF)
