#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI

def jsonFileWriter(jsonDICT, jsonFileName):
    with open (jsonFileName, mode = "w") as f:
        json.dump(jsonDICT, f, ensure_ascii = False)

def charCounter(inputSTR):
    '''計算「字符」出現次數'''
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


def wordCounter(inputSTR):
    '''計算「字詞」出現次數'''
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


def wordPlusPosCounter(inputSTR):
    '''計算「字詞 + 詞性」出現次數'''
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
    '''計算「內容字詞」(非功能字/詞)出現次數'''
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

if __name__=="__main__":
    with open ("dbp.txt", encoding="utf-8")as f:
        dbpSTR = f.read()
    with open ("pbd.txt", encoding="utf-8")as f:
        pbdSTR = f.read()
    
    charCount_dbp = charCounter(dbpSTR)
    charCount_pbd = charCounter(pbdSTR)

    articut = ArticutAPI.Articut()

    seg_dbpSTR = ""
    for i in range(0, len(dbpSTR), 2000):
        resultDICT = articut.parse(dbpSTR[i:i+2000])
        seg_dbpSTR = seg_dbpSTR + resultDICT['result_segmentation']
    wordCount_dbp = wordCounter(seg_dbpSTR)
    
    seg_pbdSTR = ""
    for i in range(0, len(pbdSTR), 2000):
        resultDICT = articut.parse(pbdSTR[i:i+2000])
        seg_pbdSTR = seg_pbdSTR + resultDICT["result_segmentation"]
    wordCount_pbd = wordCounter(seg_pbdSTR)

    pos_dbpLIST = []
    for i in range(0, len(dbpSTR), 2000):
        resultDICT = articut.parse(dbpSTR[i:i+2000])
        pos_dbpLIST.extend(resultDICT["result_pos"])
    pos_dbpSTR = "".join([p for p in pos_dbpLIST if len(p) > 1])
    posWordCount_dbp = wordPlusPosCounter(pos_dbpSTR)
    
    pos_pbdLIST = []
    for i in range(0, len(pbdSTR), 2000):
        resultDICT = articut.parse(pbdSTR[i:i+2000])
        pos_pbdLIST.extend(resultDICT["result_pos"])
    pos_pbdSTR = "".join([p for p in pos_pbdLIST if len(p) > 1])
    posWordCount_pbd = wordPlusPosCounter(pos_pbdSTR)    

    content_dbpLIST = []
    for i in range(0, len(dbpSTR), 2000):
        resultDICT = articut.parse(dbpSTR[i:i+2000])
        contentLIST = articut.getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c) > 0:
                for w in c:
                    content_dbpLIST.append(w[-1])
    posContent_dbpSTR = "/".join(content_dbpLIST)
    contentWord_dbp = contentWordPlusPosCounter(posContent_dbpSTR)

    content_pbdLIST = []
    for i in range(0, len(pbdSTR), 2000):
        resultDICT = articut.parse(pbdSTR[i:i+2000])
        contentLIST = articut.getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c) > 0:
                for w in c:
                    content_pbdLIST.append(w[-1])
    posContent_pbdSTR = "/".join(content_pbdLIST)
    contentWord_pbd = contentWordPlusPosCounter(posContent_pbdSTR)
    
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
    print("dbp_contentword_count: ", jsonDICT["contentWord_dbp"])
    print()
    print("pbd_contentword_count: ", jsonDICT["contentWord_pbd"])
    jsonFileName = "count_result.json"
    jsonFileWriter(jsonDICT, jsonFileName) 