#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#讀取 json 的程式
import json
def jsonTextReader(jsonFilePath):
    with open (jsonFilePath, "r", encoding = "utf8") as f:
        jso = json.load(f)
    return jso


#將字串轉為「句子」列表的程式

def text2Sentence(inputSTR):
    for item in("、","，","。"):
        inputSTR=inputSTR.replace(item,'<cut>')
    for item in ("...","…"):
        inputSTR=inputSTR.replace(item,'')
    for i in range(len(inputSTR)):
        if inputSTR[i] == "," and inputSTR[i-1]not in ['0','1','2','3','4','5','6','7','8','9']:
           inputSTR=inputSTR[:i]+"<cut>"+inputSTR[i+1:]
    inputList=inputSTR.split('<cut>')[:-1]
    return(inputList)


if __name__ == "__main__":
    # 設定要讀取的 news.json 路徑
    jsonFilePath = './example/news.json'

    # 將 news.json 利用 [讀取 json] 的程式打開
    newsSTR = jsonTextReader(jsonFilePath)["text"]

    # 將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST = text2Sentence(newsSTR)

    # 設定要讀取的 test.json 路徑
    jsonFilePath = './example/test.json'

    # 將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    testLIST = jsonTextReader(jsonFilePath)["sentence"]

    print(newsLIST)
    print(testLIST)


      #測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")