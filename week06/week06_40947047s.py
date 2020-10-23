#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

#讀取 json 的程式

def jsonTextReader(jsonFile):
    with open(jsonFile,"r",encoding="utf-8") as f:
        text=json.load(f)
    return text

#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
    for i in {"、","，","。","…","..."}:
        if i in {"…","..."}:
            inputSTR=inputSTR.replace(i,"")
        else:
            inputSTR=inputSTR.replace(i,"<CUT_FLAG>")
    for i in range(len(inputSTR)):
        if (str.isdigit(inputSTR[i-1])!=1 or str.isdigit(inputSTR[i+1])!=1) and inputSTR[i]==",":
            inputSTR=inputSTR[:i]+"<CUT_FLAG>"+inputSTR[i+1:]
    return inputSTR.split("<CUT_FLAG>")
    




if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    filePath_news="./example/news.json"

    #將 news.json 利用 [讀取 json] 的程式打開
    inputSTR=jsonTextReader(filePath_news)["text"]

    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST=text2Sentence(inputSTR)[:-1]
    print(newsLIST)
    #設定要讀取的 test.json 路徑
    filePath_test="./example/test.json"

    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    testLIST=jsonTextReader(filePath_test)["sentence"]
    #測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")