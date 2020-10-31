#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json,jieba,os
def text2cws(jsonFilePath):
    with open(jsonFilePath,'r',encoding="utf-8") as f:
<<<<<<< HEAD
        js=json.load(f.read())
    inputSTR = js["BODY"]
     for item in("…","..."):
     inputSTR=inputSTR.replace(item,"")
=======
        js=json.load(f)
    inputSTR = js["BODY"]

    for item in("…","..."):
        inputSTR=inputSTR.replace(item,"")
    for item in("、","，","。",",", "「", "」", "/", "／", "(", ")", "（", "）"):
        for i in range(len(inputSTR)):
            if inputSTR[i]==',' and inputSTR[i-1] not in ['0','1','2','3','4','5','6','7','8','9']:
                inputSTR = inputSTR[:i] + "<My Cutting Mark>" + inputSTR[i+1:]
            inputSTR=inputSTR.replace(item,"<My Cutting Mark>")
    inputLIST = inputSTR.split("<My Cutting Mark>")[:-1]   

    jsonLIST=[]

    for j in inputLIST:   
        jsonLIST.extend(list(jieba.cut(j)))
    return jsonLIST 

def termFreq(inputLIST):
    strDICT={}
    for j in inputLIST:
        if j in strDICT:
            strDICT[j] += 1
        else:
            strDICT[j]=1
    return strDICT

if __name__=="__main__":
    jsonPATH =("./example/health","./example/finance")
    strDICT = [{}, {}]
    for i in range(len(jsonPATH)) :
        forTermList = []
        dirs = os.listdir(jsonPATH[i])
        for j in dirs:
            forTermList.extend(text2cws(jsonPATH[i] + '/' + j))
        strDICT[i] = termFreq(forTermList)
    for i in strDICT:
        print(i)
>>>>>>> d62fe236f722aa5ecf7c5ee7427360d22db3d4fd
