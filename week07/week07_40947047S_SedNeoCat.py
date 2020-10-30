#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, json, jieba

def text2cws(jsonFilePath):
    with open(jsonFilePath, 'r', encoding='utf-8') as f:
        js = json.loads(f.read())
    jsBodyStr = js["BODY"]
    for item in ("、", "，", "。", "「", "」", "/", "／", "(", ")", "（", "）"):
        jsBodyStr = jsBodyStr.replace(item, '<cutting mark>')
    for item in ("...", "…"):
        jsBodyStr = jsBodyStr.replace(item, '')
    for i in range(len(jsBodyStr)):
        if jsBodyStr[i] == "," and jsBodyStr[i-1]not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            jsBodyStr = jsBodyStr[:i]+"<cutting mark>"+jsBodyStr[i+1:]
    jsBodyList = jsBodyStr.split('<cutting mark>')[:-1]
    rList= []
    for i in jsBodyList:
        rList.extend(list(jieba.cut(i)))
    return rList

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
        forTermList = []
        dirs = os.listdir(path[i])
        for j in dirs:
            forTermList.extend(text2cws(path[i] + '/' + j))
        resultDict[i] = termFreq(forTermList)
    for i in resultDict:
        print(i)