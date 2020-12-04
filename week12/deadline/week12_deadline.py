#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys,json
sys.path.append("../../week09/deadline")
from ArticutAPI import ArticutAPI

'''3.(a)text.txt內容用來產生關於倉鼠的知識
   (b)取出text.txt中的動詞和a比較
   4.皇帝企鵝利用articut lv3 event功能建立知識
   5.將3.4存入.json 格式{"倉鼠":[("吃","瓜子"),'''
    
def TextReader(FilePath):
    with open(FilePath,"r",encoding="utf-8") as f:
        resultSTR = f.read()
    return resultSTR

def findEvent(inputSTR,nlptool):
    resultDICT = articut.parse(inputSTR,level="lv3")
    return resultDICT

def findVerb(inputSTR):
    resultLIST = articut.parse(inputSTR,level="lv2")
    verbLIST = articut.getVerbStemLIST(resultLIST)
    return verbLIST

def jsonFileWriter(jsonDICT, jsonFileName):
    """convert jsonDICT into a jsonFile and save it as jsonFileName."""
    with open (jsonFileName, mode = "w") as f:
        json.dump(jsonDICT, f, ensure_ascii = False)

if __name__=="__main__":
    textSTR = TextReader("../example/text.txt")
    
    articut = ArticutAPI.Articut()
    textLIST01 = findEvent(textSTR,articut)
    eventLIST = textLIST01["event"]
    eventLIST01 = list(filter(None, eventLIST))
    print(eventLIST01)
    
    textLIST02 = findVerb(textSTR)
    verbLIST02=list(filter(None, textLIST02))
    print(verbLIST02)
    
    penguinSTR = TextReader("penguin.txt")
    articut = ArticutAPI.Articut()
    textLIST = findEvent(penguinSTR,articut)
    eventLIST = textLIST["event"]
    penguinLIST = list(filter(None, eventLIST))
    print(penguinLIST)
    
    
    jsonDICT={
    "倉鼠":eventLIST01,"皇帝企鵝":penguinLIST
    }
    
    jsonFileName = "week12_deadline.json"
    jsonFileWriter(jsonDICT, jsonFileName)          
    
    
    