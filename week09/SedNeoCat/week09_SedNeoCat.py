#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
from ArticutAPI import ArticutAPI

def readJson(jsonPath, filed):
    with open(jsonPath, 'r', encoding='utf-8') as f:
        js = json.loads(f.read())
    txt = js[filed]
    return txt

def createJson(jsonPath, inputDict):
    with open(jsonPath, 'w', encoding='utf-8') as f:
        json.dump(inputDict, f, indent=4, ensure_ascii=False)

def getData(inputList, n):
    dataList = []
    if n == 1:
        for i in inputList:
            if i != [] and i[0][2] not in dataList:
                dataList.append(i[0][2])
    elif n == 2:
        for i in inputList:
            if i not in ['條']:
                dataList.append(i)
    elif n == 3:
        tempDict = {}
        for i in inputList:
            if i != []:
                for j in i:
                    if j[2] in tempDict:
                        tempDict[j[2]] += 1
                    else:
                        tempDict[j[2]] = 1
        dataList = list(tempDict.items())
    return dataList

def processLawText(inputText):
    dataText = ""
    for i in range(len(inputText)):
        if inputText[i] not in [" ", "　", "\r", "\n"]:
            dataText = dataText + inputText[i]
    return dataText

if __name__ == "__main__":
    articut = ArticutAPI.Articut()

    tourblogContent = readJson("../example/tourblog.json", "content")
    resultDict = articut.parse(tourblogContent, level = "lv2")
    locList = getData(articut.getLocationStemLIST(resultDict), 1)
    resultDict = articut.parse(tourblogContent, openDataPlaceAccessBOOL = True)
    plaList = getData(articut.getOpenDataPlaceLIST(resultDict), 1)
    createJson("./tourblog_geoinfo.json", {"location": locList, "place": plaList})
    
    justiceText = processLawText(readJson('../example/刑事判決_106,交簡,359_2017-02-21.json', "judgement"))
    resultDict = articut.parse(justiceText, level = "lv2")
    lawList = getData(ArticutAPI.LawsToolkit(resultDict).getLawArticle(), 2)
    createJson("./justice.json", {"liability": lawList})

    newsContent = readJson("../example/news.json", "content")
    resultDict = articut.parse(newsContent, level = "lv2")
    nameList = getData(articut.getPersonLIST(resultDict), 3)
    locList = getData(articut.getLocationStemLIST(resultDict), 1)
    createJson("./news_info.json", {"people": nameList, "location": locList, "money": []})