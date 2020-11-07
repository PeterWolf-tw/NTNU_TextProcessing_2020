<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import jieba
import os

def isNumber(Character):
    for i in ("0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"):
        if Character == i:
            return 1
    return 0

#讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open(jsonFilePath , encoding="utf-8") as f:
        jsonFile = json.loads(f.read())
    return jsonFile

#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
    for i in ("，" , "。" , "、" , "「" , "」" , "【" , "】" , "（" , "）" , "?" , "/" , ";" , ":" , "(" , ")"):
        inputSTR = inputSTR.replace( i , "MyCurringMark")
    for i in ("…" , "..."):
        inputSTR = inputSTR.replace( i, "")    
    #print("2: " + inputSTR)
    for i in range(len(inputSTR)):
        if inputSTR[i] == ",":
            if isNumber(inputSTR[i-1]) == 0 or isNumber(inputSTR[i+1]) == 0 :
                #print(inputSTR[i-1] , isNumber(inputSTR[i-1]) , inputSTR[i+1] , isNumber(inputSTR[i+1]) , inputSTR )
                inputSTR = inputSTR[0:i] + "MyCurringMark" + inputSTR[i+1:]
    #print("5: " + inputSTR)
    inputList = inputSTR.split("MyCurringMark")
    while "" in inputList:
        inputList.remove("")
    return inputList

#將資料夾內的所有文件jieba斷句
def text2cws(DocuPath , STR):
    allFileList = os.listdir(DocuPath)
    jsonFileList = []
    jiebaList = []
    #依標點符號斷句
    
    for j in allFileList:
        jsonFileText = jsonTextReader(DocuPath + j)[STR]
        text2SentenceList = text2Sentence(jsonFileText)
        for k in text2SentenceList:
            jsonFileList.append(k)
    #print("jsonFileList:")
    #print(type(jsonFileList))
    #print(jsonFileList)
    
    #jieba斷句
    #print("jiebaList:")
    for i in jsonFileList:
        #print(type(i))
        #print(i)        
        jiebaList.append(jieba.cut(i))
    
    return jiebaList

#計算字/詞頻率
def termFreq(jiebaList):
    resultDICT = {}
    for i in jiebaList:
        for j in i:
            if resultDICT.get(j) == None :
                resultDICT[j] = 1
            else :
                resultDICT[j] = resultDICT[j] + 1
            
    return resultDICT


if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    docuTuple = ("health/" , "finance/")
    FilePath = "./example/"
    for i in docuTuple:
=======
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import jieba
import os

def isNumber(Character):
    for i in ("0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"):
        if Character == i:
            return 1
    return 0

#讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open(jsonFilePath , encoding="utf-8") as f:
        jsonFile = json.loads(f.read())
    return jsonFile

#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
    for i in ("，" , "。" , "、" , "「" , "」" , "【" , "】" , "（" , "）" , "?" , "/" , ";" , ":" , "(" , ")"):
        inputSTR = inputSTR.replace( i , "MyCurringMark")
    for i in ("…" , "..."):
        inputSTR = inputSTR.replace( i, "")    
    #print("2: " + inputSTR)
    for i in range(len(inputSTR)):
        if inputSTR[i] == ",":
            if isNumber(inputSTR[i-1]) == 0 or isNumber(inputSTR[i+1]) == 0 :
                #print(inputSTR[i-1] , isNumber(inputSTR[i-1]) , inputSTR[i+1] , isNumber(inputSTR[i+1]) , inputSTR )
                inputSTR = inputSTR[0:i] + "MyCurringMark" + inputSTR[i+1:]
    #print("5: " + inputSTR)
    inputList = inputSTR.split("MyCurringMark")
    while "" in inputList:
        inputList.remove("")
    return inputList

#將資料夾內的所有文件jieba斷句
def text2cws(DocuPath , STR):
    allFileList = os.listdir(DocuPath)
    jsonFileList = []
    jiebaList = []
    #依標點符號斷句
    
    for j in allFileList:
        jsonFileText = jsonTextReader(DocuPath + j)[STR]
        text2SentenceList = text2Sentence(jsonFileText)
        for k in text2SentenceList:
            jsonFileList.append(k)
    #print("jsonFileList:")
    #print(type(jsonFileList))
    #print(jsonFileList)
    
    #jieba斷句
    #print("jiebaList:")
    for i in jsonFileList:
        #print(type(i))
        #print(i)        
        jiebaList.append(jieba.cut(i))
    
    return jiebaList

#計算字/詞頻率
def termFreq(jiebaList):
    resultDICT = {}
    for i in jiebaList:
        for j in i:
            if resultDICT.get(j) == None :
                resultDICT[j] = 1
            else :
                resultDICT[j] = resultDICT[j] + 1
            
    return resultDICT


if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    docuTuple = ("health/" , "finance/")
    FilePath = "./example/"
    for i in docuTuple:
>>>>>>> d62fe236f722aa5ecf7c5ee7427360d22db3d4fd
        print(termFreq(text2cws(FilePath + i, "BODY")))