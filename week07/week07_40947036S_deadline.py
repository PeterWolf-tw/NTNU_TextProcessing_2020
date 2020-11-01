#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json,jieba,os

def text2cws(jsonFilePath):
    with open(jsonFilePath,'r',encoding="utf-8") as f:
        js=json.load(f)
    jsBodySTR = js["BODY"]

    for item in ("、","，","。","(", ")", "「", "」","【", "】","/", "／", "（", "）"):
        jsBodySTR=jsBodySTR.replace(item,'<CuttingMark>')
    for item in ("...","…"):
        jsBodySTR=jsBodySTR.replace(item,"")

    for i in range( len(jsBodySTR) ):
        IsDigit=jsBodySTR[i-1].isdigit()
        if jsBodySTR[i]=="," and IsDigit==False:
            jsBodySTR=jsBodySTR[:i]+"<CuttingMark>"+jsBodySTR[i+1:]
    jsBodyList = jsBodySTR.split('<CuttingMark>')[:-1]

    readList=[]
    for i in jsBodyList:
       readList.extend( list(jieba.cut(i)) )

    return readList

def termFreq(jsList):
    tempDict = {}
    for i in jsList:
        if i in tempDict:
            tempDict[i] +=1
        else:
            tempDict[i]=1
    return tempDict





if __name__=='__main__':
    files=("./example/health","./example/finance")
    strDict = [{}, {}]
    for i in range( len(files) ):
        forTermList=[]
        dirs=os.listdir(files[i])
        for j in dirs:
            forTermList.extend( text2cws(files[i] + '/' + j) )
        strDict[i] = termFreq(forTermList)
    for i in strDict:
        print(i)


