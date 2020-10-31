#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json,jieba, os
def text2cws(jsonFilePath):
    with open(jsonFilePath,'r',encoding="utf-8") as f:
        result=json.load(f)
    resultBodySTR = result["BODY"]
    for item in ("、","，","。","(", ")", "「", "」","/", "／", "（", "）"):
        resultBodySTR = resultBodySTR.replace(item,'<Cutting_Mark>') 
    for item in("...","…"):
        resultBodySTR = resultBodySTR.replace(item,"")
    for i in range(len(resultBodySTR)):
        if resultBodySTR[i]=="," and resultBodySTR[i-1] not in['0','1','2','3','4','5','6','7','8','9']:
            resultBodySTR = resultBodySTR[:i] + "<Cutting_Mark>" + resultBodySTR[i+1:]
    resultBodyList = resultBodySTR.spilt('<Cutting_Mark>')[:-1]

    readList=[]

    for j in resultBodyList:
        readList.extend(list(jieba.cut(j)))
        return readList

def termFreq(jList):
    tempDict = {}
    for k in jList:
        if k in tempDict:
            tempDict[k] += 1
        else:
            tempDict[k] =1
    return tempDict


if __name__=='__main__':
    files =("./example/health","./example/finance")
    resultDict = [{}, {}]
    for l in range(len(files)) :
        forTermList = []
        dirs = os.listdir(files[l])
        for m in dirs:
            forTermList.extend(text2cws(files[l] + '/' + m))
        resultDict[l] = termFreq(forTermList)
    for l in resultDict:
        print(l)       
        

   
    
   