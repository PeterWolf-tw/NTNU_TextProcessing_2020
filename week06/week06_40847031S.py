#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json


# 讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open(jsonFilePath, 'r', encoding='utf-8') as f:
        jsonFile = json.load(f)
        return jsonFile['text']


# 將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
    # replace '...' and '…' with ''
    unused = ['...', '…']
    for sep in unused:
        inputSTR = inputSTR.replace(sep, '')

    # replace '，', '、', '。', '「', '」' with separator '\n'
    separators = ['，', '、', '。', '「', '」']
    for sep in separators:
        inputSTR = inputSTR.replace(sep, '\n')

    # if ',' is not located in number, replace it with '\n'
    currentIndex = 0
    while True:
        # find next ','
        currentIndex = inputSTR.find(',', currentIndex)

        # ',' not find
        if currentIndex == -1:
            break

        # ',' is located in numbers
        if str.isdigit(inputSTR[currentIndex - 1]) and str.isdigit(inputSTR[currentIndex + 1]):
            currentIndex += 1
            continue

        inputSTR = inputSTR[:currentIndex] + '\n' + inputSTR[currentIndex + 1:]
        currentIndex += 1

    return inputSTR.strip('\n').split('\n')


if __name__ == "__main__":
    # 設定要讀取的 news.json 路徑
    newsJsonPath = './example/news.json'

    # 將 news.json 利用 [讀取 json] 的程式打開
    text = jsonTextReader(newsJsonPath)

    # 將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST = text2Sentence(text)

    # 設定要讀取的 test.json 路徑
    testJsonPath = './example/test.json'

    # 將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    with open(testJsonPath, 'r', encoding='utf-8') as f:
        jsonFile = json.load(f)
        testLIST = jsonFile['sentence']

    print(newsLIST)
    print(testLIST)
    # 測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")
