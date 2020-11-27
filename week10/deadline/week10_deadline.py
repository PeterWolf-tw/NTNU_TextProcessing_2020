#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json,nltk

def readJson(filePath):
    with open(filePath,'r',encoding='utf-8') as f:
        resultLIST=json.load(f)
    return resultLIST
def writeJson(jsonLIST,FIlename):
    with open(FIlename,'w',encoding='utf_8') as f:
        json.dump(jsonLIST,f,indent=4,ensure_ascii=False)
    return None


if __name__ == "__main__":
    jsonFIlePath="./foxnews.json"
    foxnews=readJson(jsonFIlePath)
    foxnewsSTR=foxnews["content"]
    foxsentenceLIST=nltk.sent_tokenize(foxnewsSTR)
    foxnews["foxsentenceLIST"]=foxsentenceLIST
    wordLIST=[]
    for i in foxsentenceLIST:
        wordLIST.extend(nltk.word_tokenize(i))
    foxPOS=nltk.pos_tag(wordLIST)
    foxnews["foxPOS"]=foxPOS
    foxNER= nltk.ne_chunk(foxPOS)
    foxnews["foxNER"]=foxNER
    writeJson(foxnews,jsonFIlePath)
    foxNERpath='foxNER.json'

    for i in foxNER:
        for j in i:
            if 'White' in j:
                print('Upper Case:',i)
    
    SfoxnewsSTR=foxnewsSTR.replace('White House','white house')
    SfoxsentenceLIST=nltk.sent_tokenize(SfoxnewsSTR)
    SwordLIST=[]
    for i in SfoxsentenceLIST:
        SwordLIST.extend(nltk.word_tokenize(i))
    SfoxPOS=nltk.pos_tag(SwordLIST)
    SfoxNER= nltk.ne_chunk(SfoxPOS)
    for i in SfoxNER:
        for j in i:
            if 'white' in j:
                print('lower Case:',i,SfoxNER[SfoxNER.index(i)+1])