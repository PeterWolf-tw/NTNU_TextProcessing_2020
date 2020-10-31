#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json, os, jieba

#讀取 json 檔案，並以 jieba 斷詞處理其內容中 "BODY" 欄位的程式
#[註] 上週才寫過讀取 json 的檔案，其實可以把它複製過來使用哦！

def text2cws(folderName):
    def jsonTextReader(jsonFilePath):
        with open (jsonFilePath, "r", encoding = "utf8") as f:
            jsonContent = json.load(f)
            return jsonContent
    
    resultLIST = []
    sentenceLIST = []
    joinLIST = []
    for file in os.listdir(folderName):
        jsonFilePath = folderName + "/" + file
        
        newsSTR = jsonTextReader(jsonFilePath)["BODY"]
        #print (newsSTR)
        
        for item in ("，", "、", "。", "「", "」", "【", "】", "（", "）", "；", "-"):
            newsSTR = newsSTR.replace(item, "{}".format("#"))
        for i in range(len(newsSTR)):
            #千位數
            if newsSTR[i-1].isdigit() == True and newsSTR[i] == "," and newsSTR[i+1].isdigit() == True:
                pass
            elif newsSTR[i] == ",":
                newsSTR = newsSTR[:i] + "#" + newsSTR[i+1:]
            #小數點
            if newsSTR[i-1].isdigit() == True and newsSTR[i] == "." and newsSTR[i+1].isdigit() == True:
                pass
            elif newsSTR[i] == ".":
                newsSTR = newsSTR[:i] + "#" + newsSTR[i+1:]
                
        while "###" in newsSTR:
            newsSTR = newsSTR.replace("###", "")
        while "…" in newsSTR:
            newsSTR = newsSTR.replace("…", "")           
                    
        newsLIST = newsSTR.split("#")
        while "" in newsLIST:
            newsLIST.remove("")
            
        for s in newsLIST:
            sentenceLIST.append(s)
    #print(sentenceLIST)
    
    for s in sentenceLIST:
        resultLIST.append("/".join(jieba.cut(s)))  
    #print(resultLIST)
    
    for i in resultLIST:
        splitLIST = i.split("/")
        joinLIST.extend(splitLIST)
    
    #print(joinLIST)
    return joinLIST

#設計一個名為 termFreq() 的程式，承接 text2cws() 的回傳值，並
#建立一個 resultDICT{}。內容是 resultDICT = {"某個字/詞", 5,
#"另一個字/詞", 8} 的格式。其中的數字是那個字/詞在 10 篇文章中總
#共出現的次數。
#e.g., 文章01 = "斷詞不要結巴"。文章02 = "斷詞不要結結巴巴"，則
#resultDICT = {"斷詞": 2, "不要": 2, "結巴": 1, "結結巴巴": 1}
def termFreq(joinList):
    tempDict = {}
    for i in joinList:
        if i in tempDict:
            tempDict[i] = tempDict[i] + 1
        else:
            tempDict[i] = 1
    return tempDict



#設計一程式進入點，讀取 example/health/ 中所有檔案，然後將檔案路徑
#傳給 text2cws()，取得內容後，再傳給 termFreq()。
#完成後，對 example/finance/ 中的所有檔案做一樣的操作。
if __name__== "__main__":
    folderLIST = ["./example/health", "./example/finance"]
    for folderName in folderLIST:
        print(termFreq(text2cws(folderName)))