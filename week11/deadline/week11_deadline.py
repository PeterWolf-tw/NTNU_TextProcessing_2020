#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
from ArticutAPI import ArticutAPI
def TextReader(FilePath):
    with open(FilePath,"r",encoding="utf-8") as f:
        resultSTR = f.read()
    return resultSTR

def jsonFileWriter(jsonList,jsonFileName):
    with open(jsonFileName,"w",encoding="utf-8") as f:
        json.dump(jsonList, f , ensure_ascii=False)
    return None

def charCounter(inputSTR):
    charDICT = {}
    for i in inputSTR:
        if i in charDICT:
            pass
        else:
            charDICT[i] = inputSTR.count(i)

    charCountLIST = []
    for i in charDICT.items():
        charCountLIST.append(i)

    charCountLIST.sort(key=lambda c: c[1], reverse=True)
    return charCountLIST

def wordCount(inputSTR):
	'''計算「字詞」出現次數'''
	inputLIST = inputSTR.split("/")

	wordCountLIST = []
	for w in inputLIST:
		wordCount = (w, inputLIST.count(w))
		if wordCount not in wordCountLIST:
			wordCountLIST.append(wordCount)

	wordCountLIST.sort(key=lambda c: c[1], reverse=True)
	return wordCountLIST

def wordCounter(inputSTR):
	inputLIST = inputSTR.split("/")
	wordCountLIST = []
	for w in inputLIST:
		wordCounter = (w, inputLIST.count(w))
		if wordCounter not in wordCountLIST:
			wordCountLIST.append(wordCounter)

	wordCountLIST.sort(key=lambda c: c[1], reverse=True)
	return wordCountLIST

def wordPlusPosCounter(inputSTR):
    inputSTR = inputSTR.replace("><", ">MY_SPLITTER<")
    inputLIST = inputSTR.split("MY_SPLITTER")
    wordDICT = {}
    for w in inputLIST:
        if w in wordDICT:
            pass
        else:
            wordDICT[w] = inputLIST.count(w)
    wordCountLIST = []
    for i in wordDICT.items():
        wordCountLIST.append(i)
    wordCountLIST.sort(key=lambda c: c[1], reverse=True)
    return wordCountLIST

def contentWordPlusPosCounter(inputSTR):
    inputLIST = inputSTR.split("/")
    wordDICT = {}
    for w in inputLIST:
        if w in wordDICT:
            pass
        else:
            wordDICT[w] = inputLIST.count(w)
    wordCountLIST = []
    for i in wordDICT.items():
        wordCountLIST.append(i)
    wordCountLIST.sort(key=lambda c: c[1], reverse=True)
    return wordCountLIST

def seg(segSTR,STR):
    articut=ArticutAPI.Articut()
    for i in range(0, len(STR), 2000):
        resultDICT=articut.parse(STR[i:i+2000])
        segSTR=segSTR + resultDICT["result_segmentation"]
    return segSTR

def pos(LIST,STR):
    articut = ArticutAPI.Articut()
    for i in range(0, len(dbpSTR), 2000):
        resultDICT=articut.parse(STR[i:i+2000])
        LIST.extend(resultDICT["result_pos"])
    pos_STR="".join([p for p in LIST if len(p) > 1])
    return pos_STR

if __name__=="__main__":
    dbpSTR=TextReader("../example/dbp.txt")
    pdbSTR=TextReader("../example/pbd.txt")

    charCount_dbp=charCounter(dbpSTR)
    charCount_pbd=charCounter(pdbSTR)

    seg_dSTR=""
    wordCount_dbp=wordCounter(seg(seg_dSTR,dbpSTR))
    seg_pSTR=""
    wordCount_pbd=wordCounter(seg(seg_pSTR,pdbSTR))
    
    pos_dLIST=[]
    posWordCount_dbp=wordPlusPosCounter(pos(pos_dLIST,dbpSTR))
    pos_pLIST=[]
    posWordCount_pbd=wordPlusPosCounter(pos(pos_pLIST,pdbSTR))

    articut = ArticutAPI.Articut()
    content_dLIST=[]
    for i in range(0, len(pdbSTR), 2000):
        resultDICT = articut.parse(pdbSTR[i:i+2000])
        contentLIST = articut.getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c) > 0:
                for w in c:
                    content_dLIST.append(w[-1])
    posContent_dSTR = "/".join(content_dLIST)
    contentWord_dbp = contentWordPlusPosCounter(posContent_dSTR)

    content_pLIST=[]
    for i in range(0,len(pdbSTR),2000):
        resultDICT=articut.parse(pdbSTR[i:i+2000])
        contentLIST=articut.getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c) > 0:
                for w in c:
                    content_pLIST.append(w[-1])
    posContent_pSTR = "/".join(content_pLIST)
    contentWord_pbd = contentWordPlusPosCounter(posContent_pSTR)

    jsonDICT = {
        "charCount_dbp": charCount_dbp,
        "charCount_pbd": charCount_pbd,
        "wordCount_dbp":wordCount_dbp,
        "wordCount_pbd": wordCount_pbd,
        "posWordCount_dbp":posWordCount_dbp,
        "posWordCount_pbd":posWordCount_pbd,
        "contentWord_dbp": contentWord_dbp,
        "contentWord_pbd": contentWord_pbd
    }
    print({"contentWord_dbp":contentWord_dbp,"contentWord_pbd":contentWord_pbd})
    jsonFileWriter(jsonDICT,"count_result.json")