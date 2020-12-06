#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ArticutAPI import ArticutAPI
import json , sys

sys.path.append("../../week09/Multiply/")

def textReadAndPrint(txtFILE):
    with open(txtFILE, encoding="utf-8") as f:
        txtContent = f.read()
    return txtContent
  
def textReadAndPrint2(txtFILE):
    with open(txtFILE, encoding="utf-8") as f:
        txtContent2 = f.read()
    return txtContent2

def findEvent(inputSTR, nlptool):
    resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT

def findVerb(inputSTR):
    resultLIST = articut.parse(inputSTR,level="lv2")
    verbLIST = articut.getVerbStemLIST(resultLIST)
    return verbLIST


if __name__== "__main__":

    # a.把 "text.txt" 內容用來產生關於「倉鼠」的知識。
    txtFilePath = "text.txt"
    txt = textReadAndPrint(txtFilePath)
    # print(txt)    
    # tourblogSTR = tourblogSTR.replace(" " , "")
    articut = ArticutAPI.Articut()
    resultLIST = findEvent(txt, articut)
    eventLIST = resultLIST["event"]
    LIST3a = list(filter(None, eventLIST))
    # print(LIST3a)

    # b. 把 "text.txt" 的內容取出動詞，比較一下和 a 有何不同
    VerbLIST = findVerb(txt)
    LIST3b =list(filter(None, VerbLIST))
    # print(LIST3b)

    # 請在 wikipedia 中搜尋「皇帝企鵝」，並利用 Articut 的 lv3 event 功能建立關於「皇帝企鵝」的知識
    txtFilePath2 = "penguin_wiki.txt"
    txt2 = textReadAndPrint2(txtFilePath2)
    # print(txt2)
    articut = ArticutAPI.Articut()
    resultLIST2 = findEvent(txt2, articut)
    eventLIST2 = resultLIST2["event"]
    LIST4 = list(filter(None, eventLIST2))
    print("list4:", LIST4)

    # 將步驟 3 和 4 做出的結果儲存為 week12_分組隊名.json ，分別存入 "倉鼠" 和 "皇帝企鵝" 兩個條目中
    resultDICT = []
    resultDICT = {"倉鼠": LIST3a , "皇帝企鵝": LIST4}
                
    with open('week12_Multiply＊.json' , 'w' , encoding = 'utf-8') as f:
       json.dump(resultDICT , f , ensure_ascii = False)