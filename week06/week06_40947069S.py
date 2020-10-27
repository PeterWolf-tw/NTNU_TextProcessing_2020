#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json


#讀取 json 的程式

def jsonTextReader(jsonFilePatch):
    with open(jsonFilePatch, encoding="utf-8") as f:
        txtContent = json.load(f)
    return txtContent 

#將字串轉為「句子」列表的程式

def texttoSentence(inputSTR):
    for item in ("..."), ("…"), ("．．．"):
        inputSTR = inputSTR.replace(item, "")

    for item in ("「", "，", "、", "…", "」", "。", "."):
        inputSTR = inputSTR.replace(item, "<My_Cutting_Mark>")

    for item in (","):
        inputSTR = inputSTR.replace(item, "<My_Cutting_Mark>")

    for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]: 
        while i+"<My_Cutting_Mark>" in inputSTR: 
            inputSTR = inputSTR.replace(i+"<My_Cutting_Mark>", i+",")

    resultLIST = inputSTR.split("<My_Cutting_Mark>")
    return resultLIST


if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    jsonFilePath = "./example/news.json"

    #將 news.json 利用 [讀取 json] 的程式打開
    txt = jsonTextReader(jsonFilePath)

    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST = texttoSentence(txt["text"])
    newsLIST.pop()    

    #設定要讀取的 test.json 路徑
    jsonFilePath2 = "./example/test.json"


    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIS
    txt2 = jsonTextReader(jsonFilePath2)
    testLIST = txt2["sentence"]    

    #測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！") 
