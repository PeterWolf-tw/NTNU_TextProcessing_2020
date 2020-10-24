#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def isNum(c):
    if c >= '0' and c <= '9':
        return True
    return False

#讀取 json 的程式

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,'r', encoding="utf-8") as f:
        content = json.load(f)
    return content
    

#將字串轉為「句子」列表的程式

def text2Sentence(inputSTR):
    for i in ('...', '…'):
        inputSTR = inputSTR.replace(i, '')
    for i in ('，', '、', '。'):
        inputSTR = inputSTR.replace(i, '{TAR}')
    for i in range(len(inputSTR)):
        if inputSTR[i] == ',' and not isNum(inputSTR[i-1]):
            inputSTR = inputSTR[: i] + '{TAR}' + inputSTR[i + 1 :]

    res = inputSTR.split('{TAR}')
    res.pop(-1)
    #print(res)

    return res

if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    f = "./example/news.json"

    #將 news.json 利用 [讀取 json] 的程式打開
    new_text = jsonTextReader(f)["text"]

    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST = text2Sentence(new_text)

    #設定要讀取的 test.json 路徑
    f = "./example/test.json"

    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    testLIST = jsonTextReader(f)["sentence"]


    #測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")

