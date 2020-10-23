#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

#讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open (jsonFilePath, "r", encoding = "utf8") as f:
        jsonContent = json.load(f)
    return jsonContent

#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
    for item in ("，", "、", "."):
        inputSTR = inputSTR.replace(item, "{}".format("#"))
        #inputSTR = inputSTR.replace(item, "#")

    for i in range(len(inputSTR)):
        if inputSTR[i-1].isdigit() == True and inputSTR[i] == "," and inputSTR[i+1].isdigit() == True:
            pass
        elif inputSTR[i] == ",":
            inputSTR = inputSTR[:i] + "#" +inputSTR[i+1:]
            
        if inputSTR[i] == "。" and i != len(inputSTR)-1:
            inputSTR = inputSTR[:i] +"#" +inputSTR[i+1:]
        elif inputSTR[i] == "。" and i == len(inputSTR)-1:
            inputSTR = inputSTR[:i] 
        
    while "###" in inputSTR:
        inputSTR = inputSTR.replace("###", "")
    while "…" in inputSTR:
        inputSTR = inputSTR.replace("…", "")
        
    inputLIST = inputSTR.split("#")    
        
    return inputLIST
        
if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    jsonFilePath = "./example/news.json"

    #將 news.json 利用 [讀取 json] 的程式打開
    newsSTR = jsonTextReader(jsonFilePath)["text"]

    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST = text2Sentence(newsSTR)
    print("newsLIST: ", newsLIST)

    #設定要讀取的 test.json 路徑
    jsonFilePath2 = "./example/test.json"

    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    testLIST = jsonTextReader(jsonFilePath2)["sentence"]
    print("testLIST: ", testLIST)

    #測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")
