#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
from ArticutAPI import ArticutAPI

def fileTextReader(FilePath):
    with open(FilePath,"r",encoding="utf-8") as f:
        resultSTR = f.read()
    return resultSTR

def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w", encoding="utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

def charCount(inputSTR):
    '''計算「字符」出現次數'''
    charCountLIST = []
    for i in inputSTR:
    	charCount = (i, inputSTR.count(i))
    	if charCount not in charCountLIST:
            charCountLIST.append(charCount)
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

def posWordCount(inputSTR):
    '''計算「字詞 + 詞性」出現次數'''
    posWordCountLIST = []
    inputSTR = inputSTR.replace("><", ">MY_SPLITTER<")
    inputLIST = inputSTR.split("MY_SPLITTER")
    	
    for wp in inputLIST:
    	posWordCount = (wp, inputLIST.count(wp))
    	if posWordCount not in posWordCountLIST:
    		posWordCountLIST.append(posWordCount)
    posWordCountLIST.sort(key=lambda c: c[1], reverse=True)
    return posWordCountLIST

def contentWordCount(inputLIST):
	'''計算「內容字詞」(非功能字/詞)出現次數'''

	contentWordLIST = []
	for wc in inputLIST:
		contentWordCount = (wc, inputLIST.count(wc))
		if contentWordCount not in contentWordLIST:
			contentWordLIST.append(contentWordCount)

	contentWordLIST.sort(key=lambda c: c[1], reverse=True)
	return contentWordLIST


if __name__=="__main__":
	dbpSTR = fileTextReader('../example/dbp.txt')
	pbdSTR = fileTextReader('../example/pbd.txt')

	charCount_dbp = charCount(dbpSTR)
	charCount_pbd = charCount(pbdSTR)

	articut = ArticutAPI.Articut()

	resultdbpDICT = articut.parse(dbpSTR,  level = "lv2")
	seg_dbpSTR = resultdbpDICT['result_segmentation']
	wordCount_dbp = wordCount(seg_dbpSTR)

	pos_dbpLIST = resultdbpDICT['result_pos']
	pos_dbpSTR = "".join([p for p in pos_dbpLIST if len(p) > 1])
	posWordCount_dbp = posWordCount(pos_dbpSTR)
	
	contentLIST = articut.getContentWordLIST(resultdbpDICT)
	content_dbpLIST = []
	for c in contentLIST:
		if len(c) > 0:
			for w in c:
				content_dbpLIST.append(w[-1])
	contentWord_dbp = contentWordCount(content_dbpLIST)
	
	resultpbdDICT = articut.parse(pbdSTR,  level = "lv2")

	seg_pbdSTR = resultpbdDICT['result_segmentation']
	wordCount_pbd = wordCount(seg_pbdSTR)

	pos_pbdLIST = resultpbdDICT['result_pos']
	pos_pbdSTR = "".join([p for p in pos_pbdLIST if len(p) > 1])
	posWordCount_pbd = posWordCount(pos_pbdSTR)

	contentLIST = articut.getContentWordLIST(resultpbdDICT)
	content_pbdLIST = []
	for c in contentLIST:
		if len(c) > 0:
			for w in c:
				content_pbdLIST.append(w[-1])
	contentWord_pbd = contentWordCount(content_pbdLIST)


	jsonDICT = {
	"charCount_dbp": charCount_dbp,
	"charCount_pbd": charCount_pbd,
	"wordCount_dbp":wordCount_dbp,
	"wordCount_pbd": wordCount_pbd,
	"posWordCount_dbp":posWordCount_dbp,
	"posWordCount_pbd":posWordCount_pbd,
	"contentWord_dbp": contentWord_dbp,
	"contentWord_pbd": contentWord_pbd,
    }

	print("dbp_contentword_count: ", jsonDICT["contentWord_dbp"])
	print()
	print("pbd_contentword_count: ", jsonDICT["contentWord_pbd"])
	jsonFileName = "count_result.json"
	jsonFileWriter(jsonDICT, jsonFileName) 
    