#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI


def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,"r",encoding="utf-8") as f:
        resultSTR = json.load(f)
    return resultSTR

if __name__== "__main__":
    articut=ArticutAPI.Articut()
   
    jsonFilePath = '../example/tourblog.json'
    newsSTR = jsonTextReader(jsonFilePath)["content"]
    newsLIST = articut.parse(newsSTR,level="lv2")
    locLIST = articut.getLocationStemLIST(newsLIST)
    placeLIST = articut.parse(locLIST,openDataPlaceAccessBOOL=True)
    resultDICT = articut.getOpenDataPlaceLIST(placeLIST)
    
    jsonFilePath = '../example/刑事判決_106,交簡,359_2017-02-21.json'
    newsSTR = jsonTextReader(jsonFilePath)["mainText"]
    newsLIST = articut.parse(newsSTR,level="lv2")
    lawLIST = ArticutAPI.LawsToolkit(resultDICT)
    
    jsonFilePath='../example/news.json'
    newsSTR = jsonTextReader(jsonFilePath)["content"] 
    newsLIST = articut.parse(newsSTR,level="lv2")
    nameLIST = articut.getPersonLIST(newsLIST)
    locLIST = articut.getLocationStemLIST(nameLIST)