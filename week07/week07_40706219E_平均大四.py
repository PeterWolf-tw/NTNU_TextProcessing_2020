#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, jieba, sys
sys.path.insert(0,'GitHub/NTNU_TextProcessing_2020/week06') #加位置：依jsonTextReader在哪修位置
sys.path.append('GitHub/NTNU_TextProcessing_2020/week06')
from week06_40706219E import jsonTextReader

def text2cws(jsonFilePath):
    FileNames = os.listdir(jsonFilePath) #讀取：讀資料夾裡檔案目錄
    BodyCutList = []
    for n in FileNames:
        TempSTR = []
        inputSTR = jsonTextReader(jsonFilePath + "/" + str(n))["BODY"]
        BlankMark = ["3、", "2、", "1、", "、", "【", "】", " ", "「", "」"]
        CuttingMark = [",", "，", "。", "／", "；", "（", "(", "）", ")", "？", "-", "！", "：", ":", "1.", "2.", "3.", "4."]
        LastAvoidMark = ["<CUT><CUT><CUT>", "<CUT><CUT>"]
        #以上：列需要用的 #以下：開始放斷句結點斷句
        for j in BlankMark:
            inputSTR = inputSTR.replace(j, "")
        for i in CuttingMark:
            if inputSTR.find(":00") != -1:
                inputSTR = inputSTR.replace(":00", "<R>")
            inputSTR = inputSTR.replace(i, "<CUT>")
        for k in LastAvoidMark:
            inputSTR = inputSTR.replace(k, "<CUT>")
        inputSTR = inputSTR.replace("<R>", ":00") #補回：時間我覺得算一個字啦 但還是會被jieba cut掉
        inputSTR = inputSTR[:-5] #去文章尾的結點：不然會多split空字串
        TempSTR.append(inputSTR.split("<CUT>")) #split完：借放到TempSTR 換讀下個檔案會在上面清空一次
        #以上：斷句完 #以下：用+的讓每句jieba cut完不要便二維的list
        for s in TempSTR:
            for a in s:
                BodyCutList = BodyCutList + list(jieba.cut(a))
    return BodyCutList

def termFreq(inputList):
    resultDict = {}
    for i in inputList:
        if resultDict.get(i) == None: #判斷：沒count過的詞彙再count 但好像沒比較省時間
            resultDict[i] = inputList.count(i)
    return resultDict


if __name__== "__main__":
    jsonFilePath = ("example/health", "example/finance")
    BodyDict_health = termFreq(text2cws(jsonFilePath[0]))
    BodyDict_finance = termFreq(text2cws(jsonFilePath[1]))
