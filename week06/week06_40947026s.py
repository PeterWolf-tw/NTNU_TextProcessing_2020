#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json, re

#讀取 json 的程式
def jsonTextReader(jsonFilePath):
  with open(jsonFilePath, encoding='utf-8-sig') as f:
    return json.load(f)


#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
  separatorRegexp = r'(。(?!$)|，|、|(?<![0-9]),(?![0-9])|(?<![0-9]),(?!\D))'
  text = re.sub(r'(…|\...)', '', inputSTR)
  text = re.sub(separatorRegexp, '###', text)
  return text.split('###')


if __name__== "__main__":
  #設定要讀取的 news.json 路徑
  newsJsonPath = "./example/news.json"

  #將 news.json 利用 [讀取 json] 的程式打開
  #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
  newsLIST = text2Sentence(jsonTextReader(newsJsonPath)["text"])
  
  print(newsLIST)

  #設定要讀取的 test.json 路徑
  testJsonPath = "./example/test.json"

  #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
  testLIST = jsonTextReader(testJsonPath)["sentence"]

  print(testLIST)

  #測試是否達到作業需求
  if newsLIST == testLIST:
      print("作業過關！")
  else:
      print("作業不過關，請回到上面修改或是貼文求助！")
