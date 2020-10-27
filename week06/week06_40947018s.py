#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

#讀取 json 的程式

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,'r', encoding="utf-8") as f:
        txtContent = json.load(f)
    return txtContent

#將字串轉為「句子」列表的程式

def text2Sentence(inputSTR):
    for item in ("，","、","。",):
        inputSTR = inputSTR.replace(item, "<Cut>")
    for item in ("…","．．．","..."):
        inputSTR = inputSTR.replace(item, "")
    for i in range(len(inputSTR)):
        if(inputSTR[i] == "," and inputSTR[i-1] not in ['1','2','3','4','5','6','7','8','9','0']):
            #inputSTR = inputSTR.replace(inputSTR[i], "<Cut>")
            inputSTR = inputSTR[:i] + "<Cut>" +inputSTR[i+1:]
    #print(inputSTR)
    resultList = inputSTR.split("<Cut>")[:-1]
    return resultList




if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    jsonFilePath = "./example/news.json"

    #將 news.json 利用 [讀取 json] 的程式打開
    newstxt = jsonTextReader(jsonFilePath)["text"]
    
    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST = text2Sentence(newstxt)
    #print(newsLIST)

    #設定要讀取的 test.json 路徑
    testPath = "./example/test.json"

    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    testLIST = jsonTextReader(testPath)["sentence"]
    #print(testLIST)

    #測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")