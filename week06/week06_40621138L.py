#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath, 'r', encoding = 'utf8') as f:
        jsonContent = json.load(f)
    return jsonContent

def text2Sentence(inputSTR):
    for i in ("，","、","。"):
        inputSTR = inputSTR.replace(i,'<MyCuttingMark>')
    for i in ("...","…"):
        inputSTR = inputSTR.replace(i,"")
    for i in range(len(inputSTR)):
        if inputSTR[i]==','and inputSTR[i-1] not in ['1','2','3','4','5','6','7','8','9','0']:
            inputSTR = inputSTR[0:i] + "<MyCuttingMark>" + inputSTR[i+1:]

    inputLIST = inputSTR.split('<MyCuttingMark>')
    while "" in inputLIST:
        inputLIST.remove("")
    return inputLIST
    

if __name__ == "__main__":
    jsonFilePath = "./example/news.json"
    newsSTR = jsonTextReader(jsonFilePath)['text']

    newsLIST = {"sentence": text2Sentence(newsSTR)}

    jsonFilePath = "./example/test.json"
    testLIST = jsonTextReader(jsonFilePath)

    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")

    
