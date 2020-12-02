#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ArticutAPI import ArticutAPI
import json

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
    # print(inputLIST)
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
    # a. 把 "dbp.txt" 和 "pbd.txt" 的內容取出
    with open("../example/dbp.txt", encoding="utf-8") as f1:
        dbp_textSTR = f1.read()
    with open("../example/pbd.txt", encoding="utf-8") as f2:
        pbd_textSTR = f2.read()
        

# file_list = [dbp_textSTR, pbd_textSTR]
# for i in file_list: 
#     ...

    # b. 計算兩文本的「字符」出現次數，並存成 charCount_dbp 和charCount_pbd
    charCount_dbp = charCounter(dbp_textSTR)
    charCount_pbd = charCounter(pbd_textSTR)
    print("charCount_dbp: ", charCount_dbp)
    print("charCount_pbd: ", charCount_pbd)

    # c. 計算兩文本的「字詞」出現次數，並存成 wordCount_dbp 和 wordChount_pbd
    articut = ArticutAPI.Articut()
    # dbp
    segTextSTR = ""
    for i in range(0, len(dbp_textSTR), 2000):
        print(i)
        resultDICT = articut.parse(dbp_textSTR[i:i+2000])
        segTextSTR = segTextSTR + resultDICT["result_segmentation"]
    print("segTextSTR:", segTextSTR)
    wordCount_dbp = wordCounter(segTextSTR)
    print("wordCount_dbp:", wordCount_dbp)

    # pbd
    segTextSTR2 = ""
    for j in range(0, len(pbd_textSTR), 2000):
        resultDICT2 = articut.parse(pbd_textSTR[i:i+2000])
        segTextSTR2 = segTextSTR2 + resultDICT2['result_segmentation']
    print("segTextSTR2:", segTextSTR2)
    wordChount_pbd = wordCounter(segTextSTR2)
    print("wordChount_pbd:", wordChount_pbd)

    # d. 計算兩文本含有詞性標記的字詞出現次數，並存成 posWordCount_dbp 和 posWordCount_pbd
    # dbp
    posTextLIST = []
    for i in range(0, len(dbp_textSTR), 2000):
        resultDICT = articut.parse(dbp_textSTR[i:i+2000])
        posTextLIST.extend(resultDICT["result_pos"])
    posTextSTR = "".join([p for p in posTextLIST if len(p) > 1])

    posWordCount_dbp = wordPlusPosCounter(posTextSTR)
    print("posWordCount_dbp:", posWordCount_dbp)

    # pbd
    posTextLIST2 = []
    for i in range(0, len(pbd_textSTR), 2000):
        resultDICT2 = articut.parse(pbd_textSTR[i:i+2000])
        posTextLIST2.extend(resultDICT2["result_pos"])
    posTextSTR2 = "".join([p for p in posTextLIST2 if len(p) > 1])

    posWordCount_pbd = wordPlusPosCounter(posTextSTR2)
    print("posWordCount_pbd:", posWordCount_pbd)

    # e. 計算兩文本「去除功能詞」，並存成 contentWord_dbp 和 contentWord_pbd 
    # dbp
    contentTextLIST = []
    for i in range(0, len(dbp_textSTR), 2000):
        resultDICT = articut.parse(dbp_textSTR[i:i+2000])
        contentLIST = articut.getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c) > 0:
                for w in c:
                    contentTextLIST.append(w[-1])
    posContentTextSTR = "/".join(contentTextLIST)
    contentWord_dbp = contentWordPlusPosCounter(posContentTextSTR)
    print("contentWord_dbp:", contentWord_dbp)

    # pbd
    contentTextLIST2 = []
    for i in range(0, len(pbd_textSTR), 2000):
        resultDICT2 = articut.parse(pbd_textSTR[i:i+2000])
        contentLIST2 = articut.getContentWordLIST(resultDICT2)
        for d in contentLIST2:
            if len(d) > 0:
                for w in d:
                    contentTextLIST2.append(w[-1])
    posContentTextSTR2 = "/".join(contentTextLIST2)
    contentWord_pbd = contentWordPlusPosCounter(posContentTextSTR2)
    print("contentWord_pbd:", contentWord_pbd)

    # f. 將以上所有的 _dbp 都存入 count_result.json 裡
    dbp_resultDICT = [charCount_dbp, wordCount_dbp, posWordCount_pbd, contentWord_dbp]
    with open('count_result.json' , 'w' , encoding = 'utf-8') as f:
        json.dump(dbp_resultDICT , f , ensure_ascii = False)