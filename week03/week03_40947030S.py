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

if __name__ == "__main__":
    txtFilePath = "./example/example.txt"
    txt = textReadAndPrint(txtFilePath)
    print(txt)
    jsonDICT = {
    "name": {"zh":"", "en":""},
    "birth": {"year":"", "month":"", "date":""},
    "job": "",
    "language":[],
    "education":[],
    "spouse":""
    }
    name_list = ["zh", "en"]
    proc_list = ["job", "language", "education", "spouse"]
    birth_list = ["year", "month", "date"]
    splitted = txt.split("\n")

    birth_regex = r"出生 ([0-9]{4}) 年 ([0-9]{1,2}) 月 ([0-9]{1,2}) 日"
    birth_match = re.match(birth_regex, splitted[2])

    for idx in range(0, 2):
        jsonDICT["name"][name_list[idx]] = " ".join(splitted[idx].split(" ")[1:])
    for idx in range(1, 4):
        jsonDICT["birth"][birth_list[idx-1]] = birth_match.group(idx)
    for idx in range(3, 7):
        tmp = re.split("\t| ", splitted[idx])[1];
        tmp = tmp.split("（")[0].split("、")
        if(len(tmp) <= 1):
            tmp = tmp[0]
        jsonDICT[proc_list[idx-3]] = tmp


    print(jsonDICT)
    jsonFileName = "week03_40947030S.json"
    jsonFileWriter(jsonDICT, jsonFileName)