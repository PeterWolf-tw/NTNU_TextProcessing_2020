#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ArticutAPI import ArticutAPI


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
    with open("館長全文.txt", encoding="utf-8") as f:
        textSTR = f.read()

    charCountLIST = charCounter(textSTR)
    print(charCountLIST)

    articut = ArticutAPI.Articut()
    segTextSTR = ""
    for i in range(0, len(textSTR), 2000):
        resultDICT = articut.parse(textSTR[i:i+2000])
        segTextSTR = segTextSTR + resultDICT["result_segmentation"]
    print(segTextSTR)
    wordCountLIST = wordCounter(segTextSTR)
    print(wordCountLIST)

    posTextLIST = []
    for i in range(0, len(textSTR), 2000):
        resultDICT = articut.parse(textSTR[i:i+2000])
        posTextLIST.extend(resultDICT["result_pos"])
    posTextSTR = "".join([p for p in posTextLIST if len(p) > 1])

    wordCountLIST = wordPlusPosCounter(posTextSTR)
    print(wordCountLIST)


    contentTextLIST = []
    for i in range(0, len(textSTR), 2000):
        resultDICT = articut.parse(textSTR[i:i+2000])
        contentLIST = articut.getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c) > 0:
                for w in c:
                    contentTextLIST.append(w[-1])
    posContentTextSTR = "/".join(contentTextLIST)
    contentWordCountLIST = contentWordPlusPosCounter(posContentTextSTR)
    print(contentWordCountLIST)