#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,"r",encoding="utf-8") as f:
        resultSTR = json.load(f)
    return resultSTR

def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w", encoding="utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

def ResultDataProcessing(resultList):
    dataList = []
    for item in resultList:
        if item != [] and item[0][2] not in dataList:
            dataList.append(item[0][2])
    return dataList

def PeopleCountData(inputList):
    dataList = []
    tempDict = {}
    for item in inputList:
        if item != []:
            for p in item:
                if p[2] in tempDict:
                    tempDict[p[2]] += 1
                else:
                    tempDict[p[2]] = 1
    dataList = tuple(tempDict.items())
    return dataList

if __name__== "__main__":
    articut=ArticutAPI.Articut()

    #tourblog.json
    tourblogJsonFile = '../example/tourblog.json'
    tourblogText = jsonTextReader(tourblogJsonFile)['content']
    resultDict = articut.parse(tourblogText, level = "lv2")
    locList = articut.getLocationStemLIST(resultDict)
    resultDict = articut.parse(tourblogText, openDataPlaceAccessBOOL = True)
    plaList = articut.getOpenDataPlaceLIST(resultDict)
    
    locationList = ResultDataProcessing(locList)
    placeList = ResultDataProcessing(plaList)
    tourblog_geoinfoFile = 'tourblog_geoinfo.json'
    jsonFileWriter({"location":locationList, "place":placeList}, tourblog_geoinfoFile)
    
    #criminal.json
    criminalJsonFile = '../example/刑事判決_106,交簡,359_2017-02-21.json'
    judgementText = jsonTextReader(criminalJsonFile)["judgement"]
    judgementText = judgementText.replace('\r', '')
    judgementText = judgementText.replace('\n', '')
    judgementText = judgementText.replace('　', '')
    judgementText = judgementText.replace(' ', '')
    mainTextDICT = articut.parse(judgementText, level="lv2")
    lawTK = ArticutAPI.LawsToolkit(mainTextDICT)
    
    justiceFile = 'justice.json'
    jsonFileWriter({'liability':lawTK.getLawArticle()}, justiceFile)

    #news.json
    newsJsonFile = '../example/news.json'
    newsText = jsonTextReader(newsJsonFile)['content']
    resultDict = articut.parse(newsText, level = "lv2")
    nameList = articut.getPersonLIST(resultDict)
    locList = articut.getLocationStemLIST(resultDict)

    nameList = PeopleCountData(nameList)
    locList = ResultDataProcessing(locList)
    news_infoFile = 'news_info.json'
    jsonFileWriter({"people": nameList, "location": locList, "money": []}, news_infoFile)
