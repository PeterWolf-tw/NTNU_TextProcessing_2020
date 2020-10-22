#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath, 'r', encoding='utf-8') as f:
        js = json.loads(f.read())
    return js["text"]

def text2Sentence(inputStr):
    for i in ('、', '，'):
        inputStr = inputStr.replace(i, '<Split_Mark>')
    for i in range(len(inputStr)):
        if inputStr[i] == ',' and inputStr[i-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            inputStr = inputStr[:i] + '<Split_Mark>' + inputStr[i+1:]
        if inputStr[i] == '。' and i != len(inputStr)-1:
            inputStr = inputStr[:i] + '<Split_Mark>' + inputStr[i+1:]
    inputList = inputStr.split('<Split_Mark>')
    for i in range(len(inputList)):
        for j in ('...', '…'):
            inputList[i] = inputList[i].replace(j, '')
    return inputList

if __name__== "__main__":
    newsJsonText = jsonTextReader('./example/news.json')
    newsList = text2Sentence(newsJsonText)
    with open('./example/test.json', 'r', encoding='utf-8') as f:
        js = json.loads(f.read())
    testList = js["sentence"]
    if newsList == testList:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")