#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
#讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open(jsonFilePath, encoding="utf-8") as F:
        return json.load(F)
#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
    inputSTR = inputSTR[:-1]
    for j in ("...","…"):
        inputSTR = inputSTR.replace(j, "")
    for i in (",", "，", "。", "、"):
        if i == "," and inputSTR[inputSTR.index(i)+1:inputSTR.index(i)+4].isdigit():
            inputSTR = inputSTR.replace(inputSTR[inputSTR.index(i):inputSTR.index(i)+4],"<R>"+inputSTR[inputSTR.index(i)+1:inputSTR.index(i)+4])
        inputSTR = inputSTR.replace(i, "<CUT>")
    inputSTR = inputSTR.replace("<R>", ",")
    return inputSTR.split("<CUT>")

if __name__== "__main__":
    jsonFilePath = "example/news.json"
    newsLIST = text2Sentence(jsonTextReader(jsonFilePath)["text"])
    jsonFilePath2 = "example/test.json"
    testLIST = jsonTextReader(jsonFilePath2)["sentence"]
    print(newsLIST)
    print(testLIST)
    #測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")