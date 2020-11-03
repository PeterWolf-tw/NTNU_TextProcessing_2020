#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, jieba, sys
sys.path.insert(0,'.\GitHub\NTNU_TextProcessing_2020\week06')
sys.path.append('.\GitHub\NTNU_TextProcessing_2020\week06')
from week06_40706219E.import jsonTextReader


#讀取 json 檔案，並以 jieba 斷詞處理其內容中 "BODY" 欄位的程式
#[註] 上週才寫過「讀取 json 的檔案，其實可以把它複製過來使用哦！
#這麼一來， "讀取 json" 的功能就不用重寫了。只要把檔案丟給上週的
#程式，取得回傳的值，再接著寫就好了。


def text2cws(jsonFilePath):
    FileNames = os.listdir(jsonFilePath)
    List2 = []
    for y in FileNames:
        TSTR = []
        inputSTR = jsonTextReader(jsonFilePath + "/" + str(y))["BODY"]
        BlankMark = ["3、", "2、", "1、", "、", "【", "】", " ", "「", "」"]
        CutMark = [",", "，", "。", "／", "；", "（", "(", "）", ")", "？", "-", "！", "：", ":", "1.", "2.", "3.", "4."]
        LastMark = ["<CUT><CUT><CUT>", "<CUT><CUT>"]
        for j in BlankMark:
            inputSTR = inputSTR.replace(j, "")
        for i in CutMark:
            if inputSTR.find(":00") != -1:
                inputSTR = inputSTR.replace(":00", "<R>")
            inputSTR = inputSTR.replace(i, "<CUT>")
        for k in LastMark:
            inputSTR = inputSTR.replace(k, "<CUT>")
        inputSTR = inputSTR.replace("<R>", ":00")
        inputSTR = inputSTR[:-5]
        TSTR.append(inputSTR.split("<CUT>"))
        for s in TSTR:
            for l in s:
                List2 = List2 + list(jieba.cut(l))
    return List2

def termFreq(List):
    DICT = {}
    for x in List:
        if DICT.get(x) == None:
             DICT[x] = List.count(x)
    return DICT





#設計一個名為 termFreq() 的程式，承接 text2cws() 的回傳值，並
#建立一個 resultDICT{}。內容是 resultDICT = {"某個字/詞", 5,
#"另一個字/詞", 8} 的格式。其中的數字是那個字/詞在 10 篇文章中總
#共出現的次數。

#e.g., 文章01 = "斷詞不要結巴"。文章02 = "斷詞不要結結巴巴"，則
#resultDICT = {"斷詞": 2, "不要": 2, "結巴": 1, "結結巴巴": 1}

if __name__ == "__main__":
    jsonFilePath = ("./example/health/" , "example/finance")
    BodyDict_health = termFreq(text2cws(jsonFilePath[0]))
    BodyDict_finance = termFreq(text2cws(jsonFilePath[1]))    


#設計一程式進入點，讀取 example/health/ 中所有檔案，然後將檔案路徑
#傳給 text2cws()，取得內容後，再傳給 termFreq()。
#完成後，對 example/finance/ 中的所有檔案做一樣的操作。
