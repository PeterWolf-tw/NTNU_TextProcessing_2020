#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

#讀取 json 的程式
def jsonTextReader(jFP):
    with open(jFP ,"r", encoding='utf-8') as f:
        return json.load(f)

#將字串轉為「句子」列表的程式
def text2Sentence(tet):
    for i in ("...","…"):
        tet=tet.replace(i,"") 
    for i in ("，","。","、",","):
        if '2,718' in tet:
            tet=tet.replace('2,718',"2718")        
        tet=tet.replace(i,"<My_Cutting_Mark>")
    tet=tet.replace('2718',"2,718")
    tet=tet.split("<My_Cutting_Mark>")[:-1]
    return tet
    
if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    NewsJP = "./example/news.json"

    #將 news.json 利用 [讀取 json] 的程式打開
    jtext = jsonTextReader(NewsJP)["text"]

    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST = text2Sentence(jtext)

    #設定要讀取的 test.json 路徑
    TestJP = "./example/test.json"

    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    testLIST = jsonTextReader(TestJP)["sentence"]

    #測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")