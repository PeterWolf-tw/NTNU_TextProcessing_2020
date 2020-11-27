#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

from ArticutAPI import ArticutAPI

 
def jsonReader(jsonFilePath):
    with open (jsonFilePath, "r", encoding = "utf-8")as f:
         jsonContent = json.load(f)
    #json.load : read the content; json.loads: dict to str
    return jsonContent

# week 03
# plus ,dump
def jsonWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, "w", encoding = "utf-8") as f:
         json.dump(jsonDICT, f, ensure_ascii = False )


# assignment a : 存成tourblog_geoinfo.json 
    

#a - 行政地名：
def Locations(jsonSTR):
    articut = ArticutAPI.Articut()
    resultDICT = articut.parse(jsonSTR, level = "lv2")
    resultLIST = articut.getLocationStemLIST(resultDICT)

    return resultLIST


    

#a - 景點名稱：
def TouristSpots(jsonSTR):
    articut = ArticutAPI.Articut()
    resultDICT = articut.parse(jsonSTR, level = "lv2")
    resultLIST = articut.getPersonLIST(resultDICT)

    return resultLIST


#assignment b : 存成justice.json

#b - 刑事判決
def verdict(jsonSTR):
    articut = ArticutAPI.Articut()
    resultDICT = articut.parse(jsonSTR, level = "lv2")

    lawTK = ArticutAPI.LawsToolkit(resultDICT)
    
    resultLIST = lawTK.getLawArticle()
    
    return resultLIST

#assignment c :存成ｎｅｗｓ_info
#c - 人物
def suspects(jsonSTR):
    articut = ArticutAPI.Articut()
    resultDICT = articut.parse(jsonSTR, level = "lv2")
    resultLIST = articut.getPersonLIST(resultDICT)

    return resultLIST


#c- 地點 可用上面的
    
#c - 涉案金額
def Fine2Pay(jsonSTR):
    articut = ArticutAPI.Articut()
    resultDICT = articut.parse(jsonSTR, level="lv2")
    resultLIST = articut.getCurrencyLIST(resultDICT)

    return resultLIST


if __name__ == "__main__":
    
#ASSIGNMENT a
    jsonFilePath = "../example/tourblog.json"

    tourblogContent = jsonReader(jsonFilePath)["content"].replace(" ", "")
    
    locationLIST = Locations(tourblogContent)
    spotLIST = TouristSpots(tourblogContent)

    jsonDICTa = {
        "location":[locationLIST],
        "place":[spotLIST]
        }
    jsonFileName = "tourblog_geoinfo.json"
    print("assignment a: ", jsonDICTa)
    jsonWriter (jsonDICTa, jsonFileName)

#ASSIGNMENT (11/17)split the passage; for it is over 2,000 words!

    jsonFilePath4theGuilty = "../example/刑事判決_106,交簡,359_2017-02-21.json"
    suspectsContent = jsonReader(jsonFilePath4theGuilty)["judgement"].replace(" ", "")

    suspiciousNamesLIST =verdict(suspectsContent)

    jsonDICTb = {
        "liability":""
        }
    jsonDICTb["liability"] = ", ".join(suspiciousNamesLIST)

    jsonFileName = "justice.json"
    print("assignment b: ", jsonDICTb)
    jsonWriter (jsonDICTb, jsonFileName)

#ASSIGNMENT c

    jsonFilePath4theNews = "../example/news.json"
    
    newsContent = jsonReader(jsonFilePath4theNews)["content"].replace(" ", "")

    nameLIST = suspects(newsContent)

    countLIST = []
    for p in nameLIST:
        countLIST.append((p, nameLIST.count(p)))
    nameFreqLIST = list(set(countLIST))

    locaLIST = location(newsContent)

    amountLIST = Fine2Pay(newsContent)

    jsonDICTc = {
        "people": [nameFreqLIST],
        "location":[locaLIST],
        "money":[amountLIST]
        }
    print("assignment c ",jsonDICTc)
    jsonFileName = "new_info.json"
    jsonWriter(jsonDICTc, jsonFileName)
    
    

    

    
    

    



    
