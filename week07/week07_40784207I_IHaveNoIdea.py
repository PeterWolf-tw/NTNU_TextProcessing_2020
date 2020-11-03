#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#設計一 func() 名為 "text2cws(jsonFilePath)"，接受參數為一 .json 格式的檔案，
#並讀取 json 檔案中的"BODY" 欄位的字串，


import jieba
import json

def text2cws(jsonFilePath):
    def jsonTextReader(jsonFilePath):
    with open (jsonFilePath, encoding ="utf-8") as f:
        jsonContent = f.load(f)
    return jsonContent

#加以「斷句」以後

inputSTR = text2cws(jsonFilePath)["BODY"]

    for i in ("， ","，","。","、"):
        inputSTR = inputSTR.replace(i,"{ }{ }",format(i,"_CUT_"))
                                    
    for i in range(len(inputSTR)):
        if inputSTR[i] == "," and inputSTR[i-1]not in ["0","1","2","3","4","5","6","7","8","9"]:
            inputSTR = inputSTR[:i]+ "_CUT_" +inputSTR[i+1:]  
         
    for i in ("…","..."):
        inputSTR = inputSTR.replace(i,"")

    inputLIST = inputSTR.split("_CUT_")[:-1]
    
    return inputLIST

#使用 Jieba 斷詞將每個句子進行斷詞處理，
#回傳 值為一「斷詞處理後的列表」。
segLIST = []

    for s in inputLIST:
        segLIST.extend(list(jieba.cut(s)))
        
    return segLIST

#設計一 func() 名為 "termFreq(inputLIST)"，接受參數為列表，
#並依列表 內容的「字串元素」建立一字典 dict 型別的變數，
#將每個字串元素視為 key，整份文件中的，該字串元素出現的次數視為 value。

def termFreq(segLIST):
    myDICT = { }
    for i in segLIST:
        if i in myDICT:
            myDICT[1] = myDICT[i] +１
        else:
            myDICT[i] = 1
    return myDICT

#設計一程式進入點，透過前述 "text2cws()" 讀取 example/health/ 中所有檔案的 "BODY" 欄位的值，
#再透過 termFreq() 計算每個斷詞處理後的字串出現的次數。
if__name__ == "__main__":
    JsonFiles = ('./example/health', './example/finance')
    for jsonFilePath in jsonFiles:
        print(termFreq(text2cws(jsonFilePath)))
        
    
