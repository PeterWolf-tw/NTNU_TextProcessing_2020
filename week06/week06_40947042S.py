#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

#讀取 json 的程式

def jsonFileReader(jsonFilePath):
    with open(jsonFilePath, mode='r', encoding="utf-8") as f:
        txtContent = json.load(f)
    return txtContent

#將字串轉為「句子」列表的程式

def toSentence(inputSTR):
    for item in ("，","、","。"):
        inputSTR = inputSTR.replace(item, "<Cut>")
    for item in ("…","．．．","..."):
        inputSTR = inputSTR.replace(item, "")
    for i in range(len(inputSTR)):
        if(inputSTR[i] == "," and inputSTR[i-1] not in ['1','2','3','4','5','6','7','8','9','0']):
            
            inputSTR = inputSTR[:i] + "<Cut>" +inputSTR[i+1:]  
    
    resultLIST = inputSTR.split("<Cut>")[:-1]
    return resultLIST
    
    
    
    
if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    newsjsonFilePath = "./example/news.json"
    
    #將 news.json 利用 [讀取 json] 的程式打開
    newstxt = jsonFileReader(newsjsonFilePath)["text"]

    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST = toSentence(newstxt)

    #設定要讀取的 test.json 路徑
    testjsonFilePath = "./example/test.json"

    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    testLIST = jsonFileReader(testjsonFilePath)["sentence"]


    #測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")