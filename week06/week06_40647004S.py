#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

numDICT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CUT = '{CUT}'

#讀取 json 的程式

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,'r', encoding="utf-8") as f:
        jsonContent = json.load(f)
    return jsonContent

#將字串轉為「句子」列表的程式

def text2Sentence(inputSTR):
	for i in('...', '…'):
		inputSTR = inputSTR.replace(i, '')
	for i in('，', '、', '。'):
		inputSTR = inputSTR.replace(i, CUT)
	for i in range(len(inputSTR)):
		if inputSTR[i] == ',' and inputSTR[i - 1] not in numDICT:
			inputSTR = inputSTR[: i] + CUT + inputSTR[i + 1 :]
	#print(inputSTR)
	inputLIST = inputSTR.split(CUT)
	#多了句號形成的空字串
	return inputLIST[: -1]



if __name__== "__main__":
	#設定要讀取的 news.json 路徑
	jsonFilePath_1 = "./example/news.json"

	#將 news.json 利用 [讀取 json] 的程式打開
	news_str = jsonTextReader(jsonFilePath_1)["text"]

	#將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
	newsLIST = text2Sentence(news_str)

	#設定要讀取的 test.json 路徑
	jsonFilePath_2 = "./example/test.json"

	#將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
	testLIST = jsonTextReader(jsonFilePath_2)["sentence"]
	#print(newsLIST)
	#print(testLIST)
	#測試是否達到作業需求
	if newsLIST == testLIST:
		print("作業過關！")
	else:
		print("作業不過關，請回到上面修改或是貼文求助！")
