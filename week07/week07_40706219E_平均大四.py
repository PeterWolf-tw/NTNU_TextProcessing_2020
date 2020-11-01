#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, jieba, sys
sys.path.insert(0,'GitHub/NTNU_TextProcessing_2020/week06')
sys.path.append('GitHub/NTNU_TextProcessing_2020/week06')
from week06_40706219E import jsonTextReader

def text2cws(jsonFilePath):
    FileNames = os.listdir(jsonFilePath)
    BodyCutList = []
    for n in FileNames:
        TempSTR = []
        inputSTR = jsonTextReader(jsonFilePath + "/" + str(n))["BODY"]
        BlankMark = ["3、", "2、", "1、", "、", "【", "】", " ", "「", "」"]
        CuttingMark = [",", "，", "。", "／", "；", "（", "(", "）", ")", "？", "-", "！", "：", ":", "1.", "2.", "3.", "4."]
        LastAvoidMark = ["<CUT><CUT><CUT>", "<CUT><CUT>"]
        for j in BlankMark:
            inputSTR = inputSTR.replace(j, "")
        for i in CuttingMark:
            if inputSTR.find(":00") != -1:
                inputSTR = inputSTR.replace(":00", "<R>")
            inputSTR = inputSTR.replace(i, "<CUT>")
        for k in LastAvoidMark:
            inputSTR = inputSTR.replace(k, "<CUT>")
        inputSTR = inputSTR.replace("<R>", ":00")
        inputSTR = inputSTR[:-5]
        TempSTR.append(inputSTR.split("<CUT>"))
        for s in TempSTR:
            for i in s:
                BodyCutList = BodyCutList + list(jieba.cut(i))
    return BodyCutList

def termFreq(inputList):
    Dict = {}
    for i in inputList:
        if Dict.get(i) == None:
            Dict[i] = inputList.count(i)
    return Dict


if __name__== "__main__":
    jsonFilePath = ("example/health", "example/finance")
    BodyDict_health = termFreq(text2cws(jsonFilePath[0]))
    BodyDict_Finance = termFreq(text2cws(jsonFilePath[1]))
