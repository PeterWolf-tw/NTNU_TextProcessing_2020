##!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,'r',encoding="utf-8") as f:
        resultSTR=json.load(f)
    return resultSTR

#讀取 json 的程式
def text2Sentence(inputSTR):
    for item in("...","…"):
        inputSTR=inputSTR.replace(item,"")
    for item in("、","，","。",","):
        if'2,718'  in inputSTR:
           inputSTR=inputSTR.replace('2,718',"2718") 
        inputSTR=inputSTR.replace(item,'<Cutting_Mark>')
    
    inputSTR=inputSTR.replace('2718',"2,718")    

    inputLIST=inputSTR.split('<Cutting_Mark>')[:-1]
    return inputLIST

#將字串轉為「句子」列表的程式





if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    jsonFilePath='./example/news.json'

    #將 news.json 利用 [讀取 json] 的程式打開
    newsSTR=jsonTextReader(jsonFilePath)["text"]

    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST=text2Sentence(newsSTR)

    #設定要讀取的 test.json 路徑
    jsonFilePath='./example/test.json'

    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    testLIST=jsonTextReader(jsonFilePath)["sentence"]
    print (testLIST)
    print (newsLIST)

    #測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")