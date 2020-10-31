#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#讀取 json 檔案，並以 jieba 斷詞處理其內容中 "BODY" 欄位的程式
#[註] 上週才寫過「讀取 json 的檔案，其實可以把它複製過來使用哦！
#這麼一來， "讀取 json" 的功能就不用重寫了。只要把檔案丟給上週的
#程式，取得回傳的值，再接著寫就好了。

import json , jieba , os

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
    
    
#設計一個名為 termFreq() 的程式，承接 text2cws() 的回傳值，並
#建立一個 resultDICT{}。內容是 resultDICT = {"某個字/詞", 5,
#"另一個字/詞", 8} 的格式。其中的數字是那個字/詞在 10 篇文章中總
#共出現的次數。
    
#e.g., 文章01 = "斷詞不要結巴"。文章02 = "斷詞不要結結巴巴"，則
#resultDICT = {"斷詞": 2, "不要": 2, "結巴": 1, "結結巴巴": 1}


def termFreq(jList):
    resultDict = {}
    for k in jList:
        if k in resultDict:
            resultDict[k] += 1
        else:
            resultDict[k] =1
    return resultDict





#設計一程式進入點，讀取 example/health/ 中所有檔案，然後將檔案路徑
#傳給 text2cws()，取得內容後，再傳給 termFreq()。
#完成後，對 example/finance/ 中的所有檔案做一樣的操作。


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
        

   
    
   