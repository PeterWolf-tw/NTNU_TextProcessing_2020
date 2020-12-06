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

def main(inputSTR, nlptool):
	resultDICT = articut.parse(inputSTR, level='lv3')

	resultLIST = articut.parse(inputSTR,level="lv2")
	verbLIST = articut.getVerbStemLIST(resultLIST)
	return resultDICT, verbLIST

if __name__=="__main__":
	articut = ArticutAPI.Articut()
	result = {'倉鼠': [], '皇帝企鵝': []}

	#mouse
	mouseSTR = fileTextReader("text.txt")

	mouseLIST, mouseVerb = main(mouseSTR, articut)
	print('倉鼠動詞')
	print(list(filter(None, mouseVerb)))
	print()
	for event in mouseLIST['event']:
		if len(event)>0:
			result["倉鼠"].append(tuple(event))

	#penguin
	penguinSTR = fileTextReader("penguin.txt")

	penguinLIST, penguinVerb = main(penguinSTR, articut)
	print('皇帝企鵝動詞')
	print(list(filter(None, penguinVerb)))
	for event in penguinLIST['event']:
		if len(event)>0:
			result["皇帝企鵝"].append(tuple(event))

	jsonFileName = "week12_potato.json"
	jsonFileWriter(result, jsonFileName) 
	#print(result)
	

	
