#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI

def jsonFileWriter(jsonDICT, jsonFileName):
    """convert jsonDICT into a jsonFile and save it as jsonFileName."""
    with open (jsonFileName, mode = "w") as f:
        #json.dump(要寫入的資料, 目標檔案, 是否要讓輸入值為ascii)
        json.dump(jsonDICT, f, ensure_ascii = False)

#讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open (jsonFilePath, "r", encoding = "utf8") as f:
        jsonContent = json.load(f)
    return jsonContent

#取得地名列表的程式
def location(inputSTR):
    articut = ArticutAPI.Articut()
    resultDICT = articut.parse(inputSTR, level = "lv2")
    resultLIST = articut.getLocationStemLIST(resultDICT)
    newLIST = []
    for i in resultLIST:
        if i not in newLIST:
            newLIST.append(i)
    newLIST.remove([])
    newNewLIST = []
    for f in newLIST:
        if f not in newNewLIST:
            for g in f:
                newNewLIST.append(g[2])

    return newNewLIST

#取得景點列表的程式
def place(inputSTR):
    articut = ArticutAPI.Articut()
    resultDICT = articut.parse(inputSTR, openDataPlaceAccessBOOL = True)
    resultLIST = articut.getOpenDataPlaceLIST(resultDICT)
    newLIST = []
    for i in resultLIST:
        if i not in newLIST:
            newLIST.append(i)
    newLIST.remove([])
    newNewLIST = []
    for f in newLIST:
        if f not in newNewLIST:
            for g in f:
                newNewLIST.append(g[2])

    return newNewLIST    

#取得刑罰列表的程式
def sentence(inputSTR):
    articut = ArticutAPI.Articut()
    resultDICT = articut.parse(inputSTR, level="lv2")
    lawTK = ArticutAPI.LawsToolkit(resultDICT)

    resultLIST = lawTK.getLawArticle()
    return resultLIST   

#取得姓名列表的程式
def name(inputSTR):
    articut = ArticutAPI.Articut()
    resultDICT = articut.parse(inputSTR, level="lv2")
    resultLIST = articut.getPersonLIST(resultDICT)
    newLIST = []
    for i in resultLIST:
        if i not in newLIST:
            newLIST.append(i)
    newLIST.remove([])
    newNewLIST = []
    for f in newLIST:
        if f not in newNewLIST:
            for g in f:
                newNewLIST.append(g[2])

    return newNewLIST    


#取得金額列表的程式
def currency(inputSTR):
    articut = ArticutAPI.Articut()
    resultDICT = articut.parse(inputSTR, level="lv2")
    resultLIST = articut.getCurrencyLIST(resultDICT)
    newLIST = []
    for i in resultLIST:
        if i not in newLIST:
            newLIST.append(i)
    newLIST.remove([])
    newNewLIST = []
    for f in newLIST:
        if f not in newNewLIST:
            for g in f:
                newNewLIST.append(g[2])

    return newNewLIST    


if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    jsonFilePath = "./tourblog.json"
    
    #將 tourblog.json 利用 [讀取 json] 的程式打開
    tourblogSTR = jsonTextReader(jsonFilePath)["content"].replace(" ", "")
    
    #將讀出來的內容字串傳給 [將字串轉為地名列表的程式]，存為 locLIST
    #將讀出來的內容字串傳給 [將字串轉為景點列表的程式]，存為 placeLIST
    
    locLIST = location(tourblogSTR)
    placeLIST = place(tourblogSTR)
    #print(locLIST)  
    
    jsonDICT = {
        "location":[t for t in locLIST], #list
        "place":[t for t in placeLIST]
        }    
    print(jsonDICT)
    jsonFileName = "tourblog_geoinfo.json"
    jsonFileWriter(jsonDICT, jsonFileName)    
    
    #設定要讀取的 刑事判決_106,交簡,359_2017-02-21.json 路徑
    jsonFilePath2 = "./刑事判決_106,交簡,359_2017-02-21.json"
    
    #將 刑事判決_106,交簡,359_2017-02-21.json 利用 [讀取 json] 的程式打開
    sentenceSTR = jsonTextReader(jsonFilePath2)["judgement"].replace(" ", "")
    
    #將讀出來的內容字串傳給 [將字串轉為刑罰列表的程式]，存為 sentenceLIST
    sentenceLIST = sentence(sentenceSTR)
    
    jsonDICT2 = {
        "liability":"" #string
        }  
    
    jsonDICT2["liability"] = ", ".join(sentenceLIST)
    
    print(jsonDICT2)
    jsonFileName = "justice.json"
    jsonFileWriter(jsonDICT2, jsonFileName) 
    
    #設定要讀取的 news.json 路徑
    jsonFilePath3 = "./news.json"
    
    #將 news.json 利用 [讀取 json] 的程式打開
    newsSTR = jsonTextReader(jsonFilePath3)["content"].replace(" ", "")
    
    #將讀出來的內容字串傳給 [將字串轉為姓名列表的程式]，存為nameLIST
    nameLIST = name(newsSTR)
    #print(nameLIST)
    countLIST = []
    for i in nameLIST:
        countLIST.append((i, nameLIST.count(i)))
    nameCountLIST = list(set(countLIST))
    
    #將讀出來的內容字串傳給 [將字串轉為地名列表的程式]，存為 locLIST
    locLIST = location(newsSTR)
    #print(locLIST)
    
    #將讀出來的內容字串傳給 [將字串轉為金額列表的程式]，存為 moneyLIST
    moneyLIST = currency(newsSTR)
    #print(moneyLIST)
    
    jsonDICT3 = {
        "people":[t for t in nameCountLIST], #list
        "location":[t for t in locLIST], 
        "money":[t for t in moneyLIST]
        }  
    
    print(jsonDICT3)
    jsonFileName = "news_info.json"
    jsonFileWriter(jsonDICT, jsonFileName)      
    
