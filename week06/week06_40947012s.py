#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#讀取 json 的程式
import json

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,'r',encoding="utf-8") as f:
        jsonFileContent=json.load(f)
    return jsonFileContent


#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
    for item in("...","…"):
        inputSTR=inputSTR.replace(item,'')
    for item in("、","，","。"):
        inputSTR=inputSTR.replace(item,"<My Cutting Mark>")
    for i in range(len(inputSTR)):
#        if inputSTR[i]==',' and inputSTR[i-1] =="5":
#            inputSTR = inputSTR[:i-1] + "<My Cutting Mark>" + inputSTR[i:]
        if inputSTR[i]==',' and inputSTR[i-1] not in ['0','1','2','3','4','5','6','7','8','9']:
            inputSTR = inputSTR[:i] + "<My Cutting Mark>" + inputSTR[i+1:]
#        if inputSTR[i] == "。" and i != len(inputSTR)-1:
#            inputSTR = inputSTR[:i] +"<My Cutting Mark>" + inputSTR[i+1:]
    inputLIST = inputSTR.split("<My Cutting Mark>")[:-1]
    return inputLIST

if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    jsonFilePath1="./example/news.json"

    #將 news.json 利用 [讀取 json] 的程式打開
    newsSTR=jsonTextReader(jsonFilePath1)["text"]

    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST=text2Sentence(newsSTR)
    
    #設定要讀取的 test.json 路徑
    jsonFilePath2="./example/test.json"

    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    testLIST=jsonTextReader(jsonFilePath2)["sentence"]
    
    #測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")