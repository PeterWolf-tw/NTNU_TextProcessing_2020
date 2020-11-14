#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
from ArticutAPI import ArticutAPI

def readJson(jsonFilePath):
    with open(jsonFilePath, 'r', encoding='utf-8') as f:
        js = json.loads(f.read())
    txt = js["content"]
    return txt

def writeJson():
    pass

if __name__ == "__main__":
    tourblogContent = readJson("./example/tourblog.json")
    articut = ArticutAPI.Articut()
    resultDict = articut.parse(tourblogContent, level = "lv2")
    locList = articut.getLocationStemLIST(resultDict)
    resultDict = articut.parse(tourblogContent, openDataPlaceAccessBOOL = True)
    plaList = articut.getOpenDataPlaceLIST(resultDict)