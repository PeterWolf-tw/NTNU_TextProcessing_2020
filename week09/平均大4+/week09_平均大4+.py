#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
def jsonTextReader(jsonFilePath):
    with open(jsonFilePath, encoding="utf-8") as F:
        return json.load(F)
def jsonWriter(jsonFileName, jsonFileObject, inputDATALIST):
    resultDICT = {}
    with open(jsonFileName, "w", encoding="utf-8") as f:
        for o in jsonFileObject:
            resultDICT.setdefault(o,inputDATALIST[jsonFileObject.index(o)])
        json.dump(resultDICT, f, ensure_ascii=False)
    return None
def getItemLIST(inputLIST):
    resultLIST = []
    try:
        for i in inputLIST:
            if i != []:
                resultLIST.append(i[0][2])
    except TypeError:
        pass
    return resultLIST
def GetWordAfterVerb(inputVerbTargetLIST, ContextSTR):
    resultSTRLIST = []
    for v in inputVerbTargetLIST:
        if v == "處":
            ContextSTR = ContextSTR.replace("/處/", "<CUT>處/")
        else:
            pass
    ContextSTR = ContextSTR.split("<CUT>")[1]
    ContextSTR = ContextSTR.replace("/", "")
    resultSTRLIST.append(ContextSTR)
    return resultSTRLIST
def countPFreq(inputLIST, ContextSTR):
    resultLIST = []
    DoneCountingLIST = []
    for n in inputLIST:
        if n in DoneCountingLIST:
            resultLIST.append((n, ContextSTR.count("/"+n+"/")))
            DoneCountingLIST.append(n)
        else:
            pass
    return resultLIST

if __name__ == "__main__":
    from ArticutAPI import ArticutAPI
    jsonFilePath = ["example/tourblog.json", "example/刑事判決_106,交簡,359_2017-02-21.json", "example/news.json"]
    jsonFileName = ["tourblog_geoinfo.json", "justice.json", "money,news_info.json"]
    jsonFileObject = [["location","place"], ["liability"], ["people", "location", "money"]]
    #tb,content,行政地名location,景點名稱place,tourblog_geoinfo.json
    #刑判,mainText,刑罰liability,justice.json#處
    #nws,content,(人名/次數)people,地點location,涉案金額money,news_info.json

    myArti = ArticutAPI.Articut()
    ##tourblog_geoinfo.json## #因account有限制2000字內，所以無法分析parse
    tbparseDICT = myArti.parse(jsonTextReader(jsonFilePath[0])["content"], level="lv2")
    tbLocationLIST = myArti.getLocationStemLIST(tbparseDICT)
    tbPlaceLIST = myArti.getOpenDataPlaceLIST(tbparseDICT)
    tbDATALIST = [tbLocationLIST, tbPlaceLIST]
    for l in tbDATALIST:
        l = getItemLIST(l)
    jsonWriter(jsonFileName[0], jsonFileObject[0], tbDATALIST)
    ##tourblog_geoinfo.json##

    ##justice.json##
    punDICT = myArti.parse(jsonTextReader(jsonFilePath[1])["mainText"], level="lv2")
    punVerbTargetLIST = getItemLIST(myArti.getVerbStemLIST(punDICT))
    punDATALIST = GetWordAfterVerb(punVerbTargetLIST, punDICT["result_segmentation"])
    jsonWriter(jsonFileName[1], jsonFileObject[1], punDATALIST)
    ##justice.json##

    ##news_info.json## #因account有balance字數問題(?)，所以無法分析parse
    try:
        nwsDICT = myArti.parse(jsonTextReader(jsonFilePath[2])["content"], level="lv2")
    except Exception:
        pass
    nwsPLIST = myArti.getPersonLIST(nwsDICT)
    nwsLLIST = myArti.getLocationStemLIST(nwsDICT)
    nwsMLIST = myArti.getCurrencyLIST(nwsDICT)
    nwsDATALIST = [nwsPLIST, nwsLLIST, nwsMLIST]
    for l in nwsDATALIST:
        l = getItemLIST(l)
    nwsDATALIST[0] = countPFreq(nwsDATALIST[0], nwsDICT["result_segmentation"])
    jsonWriter(jsonFileName[2], jsonFileObject[2], nwsDATALIST)
    ##news_info.json##


