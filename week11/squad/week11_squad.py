#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI

def jsonFileWriter(jsonDICT, jsonFileName):
    """convert jsonDICT into a jsonFile and save it as jsonFileName."""
    with open (jsonFileName, mode = "w") as f:
        #json.dump(要寫入的資料, 目標檔案, 是否要讓輸入值為ascii)
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


if __name__== "__main__":
    with open("dbp.txt", encoding="utf-8") as f:
        dSTR = f.read()
    with open("pbd.txt", encoding="utf-8") as f:
        pSTR = f.read()    

    charCount_dbp = charCounter(dSTR)
    charCount_pdb = charCounter(pSTR)

    articut = ArticutAPI.Articut()
    seg_dSTR = ""
    for i in range(0, len(dSTR), 2000):
        resultDICT = articut.parse(dSTR[i:i+2000])
        seg_dSTR = seg_dSTR + resultDICT["result_segmentation"]
    wordCount_dbp = wordCounter(seg_dSTR)
    
    seg_pSTR = ""
    for i in range(0, len(pSTR), 2000):
        resultDICT = articut.parse(pSTR[i:i+2000])
        seg_pSTR = seg_pSTR + resultDICT["result_segmentation"]
    wordCount_pbd = wordCounter(seg_pSTR)

    pos_dLIST = []
    for i in range(0, len(dSTR), 2000):
        resultDICT = articut.parse(dSTR[i:i+2000])
        pos_dLIST.extend(resultDICT["result_pos"])
    pos_dSTR = "".join([p for p in pos_dLIST if len(p) > 1])
    posWordCount_dbp = wordPlusPosCounter(pos_dSTR)
    
    pos_pLIST = []
    for i in range(0, len(pSTR), 2000):
        resultDICT = articut.parse(pSTR[i:i+2000])
        pos_pLIST.extend(resultDICT["result_pos"])
    pos_pSTR = "".join([p for p in pos_pLIST if len(p) > 1])
    posWordCount_pbd = wordPlusPosCounter(pos_pSTR)    

    content_dLIST = []
    for i in range(0, len(dSTR), 2000):
        resultDICT = articut.parse(dSTR[i:i+2000])
        contentLIST = articut.getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c) > 0:
                for w in c:
                    content_dLIST.append(w[-1])
    posContent_dSTR = "/".join(content_dLIST)
    contentWord_dbp = contentWordPlusPosCounter(posContent_dSTR)

    content_pLIST = []
    for i in range(0, len(pSTR), 2000):
        resultDICT = articut.parse(pSTR[i:i+2000])
        contentLIST = articut.getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c) > 0:
                for w in c:
                    content_pLIST.append(w[-1])
    posContent_pSTR = "/".join(content_pLIST)
    contentWord_pbd = contentWordPlusPosCounter(posContent_pSTR)
    
    jsonDICT = {
        "charCount_dbp": charCount_dbp,
        "charCount_pbd": charCount_pdb,
        "wordCount_dbp":wordCount_dbp,
        "wordCount_pbd": wordCount_pbd,
        "posWordCount_dbp":posWordCount_dbp,
        "posWordCount_pbd":posWordCount_pbd,
        "contentWord_dbp": contentWord_dbp,
        "contentWord_pbd": contentWord_pbd
    }
    print("dbp_contentwordcount: ", jsonDICT["contentWord_dbp"])
    print("pbd_contentwordcount: ", jsonDICT["contentWord_pbd"])
    jsonFileName = "count_result.json"
    jsonFileWriter(jsonDICT, jsonFileName)       
    
