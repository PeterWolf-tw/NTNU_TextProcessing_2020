#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, json, jieba

def text2cws(jsonFilePath):
    with open(jsonFilePath, 'r', encoding='utf-8') as f:
        js = json.loads(f.read())
    return list(jieba.cut(js["BODY"]))

def termFreq(jiebaList):
    tempDict = {}
    for i in jiebaList:
        if i in tempDict:
            tempDict[i] = tempDict[i] + 1
        else:
            tempDict[i] = 1
    return tempDict

if __name__ == "__main__":
    path = ('./example/health', './example/finance')
    resultDict = [{}, {}]
    for i in range(len(path)) :
        dirs = os.listdir(path[i])
        for j in dirs:
            resultDict[i] = termFreq(text2cws(path[i] + '/' + j))
    for i in resultDict:
        print(i)