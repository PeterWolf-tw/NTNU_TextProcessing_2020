#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI


def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,"r",encoding="utf-8") as f:
        resultSTR = json.load(f)
    return resultSTR
def jsonFileWriter(jsonList,jsonFileName):
    with open(jsonFileName,"w",encoding="utf-8") as f:
        json.dump(jsonList, f , ensure_ascii=False)
    return None

def getLIST(inputLIST):
    getLIST=[]
    for i in inputLIST:
        if i != [] :
            for k in i:
                if i[0][2] not in getLIST:
                    getLIST.append(k[2])
    return getLIST

def countName(inputLISt):
    countDICT={}
    for i in inputLISt:
        if i != []:
            for k in i:
                if k[2] in countDICT:
                    countDICT[k[2]]+=1
                else:
                    countDICT[k[2]]=1
    return list(countDICT.items())

if __name__== "__main__":
    articut=ArticutAPI.Articut()
   
    tourFilePath = '../example/tourblog.json'
    newsSTR = jsonTextReader(tourFilePath)["content"]
    newsLIST = articut.parse(newsSTR, level = "lv2")
    locLIST = getLIST(articut.getLocationStemLIST(newsLIST))
    newsLIST = articut.parse(newsSTR,openDataPlaceAccessBOOL=True)
    placeLIST = getLIST(articut.getOpenDataPlaceLIST(newsLIST))
    tourblog="tourblog_geoinfo.json"
    jsonFileWriter({"location": locLIST, "place": placeLIST},tourblog)  

    criminalFilePath = '../example/刑事判決_106,交簡,359_2017-02-21.json'
    newsSTR = jsonTextReader(criminalFilePath)["mainText"]
    newsLIST = articut.parse(newsSTR,level="lv2")
    lawLIST = ArticutAPI.LawsToolkit(newsLIST).getCrime()
    justice="jusitice.json"
    jsonFileWriter({"liability": lawLIST},justice)    

    jsonFilePath='../example/news.json'
    newsSTR = jsonTextReader(jsonFilePath)["content"] 
    newsLIST = articut.parse(newsSTR,level="lv2")
    nameLIST = articut.getPersonLIST(newsLIST)
    nameCountLIST=countName(nameLIST)
    locLIST = getLIST(articut.getLocationStemLIST(newsLIST))
    moneyLIST=getLIST(articut.getCurrencyLIST(newsLIST))
    newsInfo="news_info.json"
    newsInfoContent={"people":nameCountLIST,"location":locLIST, "money":moneyLIST}
    jsonFileWriter(newsInfoContent,newsInfo)
    