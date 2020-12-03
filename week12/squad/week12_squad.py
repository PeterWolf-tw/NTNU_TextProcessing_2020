#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI


def main(inputSTR, nlptool):
    resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT

def jsonFileWriter(jsonDICT, jsonFileName):
    """convert jsonDICT into a jsonFile and save it as jsonFileName."""
    with open (jsonFileName, mode = "w") as f:
        #json.dump(要寫入的資料, 目標檔案, 是否要讓輸入值為ascii)
        json.dump(jsonDICT, f, ensure_ascii = False)


if __name__== "__main__":
    with open("text.txt", encoding="utf-8") as f:
        inputSTR = f.read()    
    articut = ArticutAPI.Articut()
    resultLIST = main(inputSTR, articut)
    eventLIST = resultLIST["event"]
    a = list(filter(None, eventLIST))
    print(a)
    
    with open("text01.txt", encoding="utf-8") as f:
        inputSTR = f.read()  
    articut = ArticutAPI.Articut()
    resultLIST = main(inputSTR, articut)
    eventLIST = resultLIST["event"]
    b = list(filter(None, eventLIST))
    print(b)
    
    jsonDICT = {
    "倉鼠":a,
    "皇帝企鵝":b
    }
    
    jsonFileName = "week12_squad.json"
    jsonFileWriter(jsonDICT, jsonFileName)      