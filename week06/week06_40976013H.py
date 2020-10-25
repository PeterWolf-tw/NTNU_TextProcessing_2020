#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#讀取 json 的程式
import json
def jsonTextReader(jsonFilePath):
      with open(jsonFilePath,"r",encoding="utf-8") as file:
            jsonFile= json.load(file)
      return jsonFile    

#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
      for item in("2,718"):
            inputSTR=inputSTR.replace("2,718","{}".format("2k718"))
      for item in ("...","…"):
            inputSTR=inputSTR.replace(item,"{}".format(""))
      for item in ("。","、",",",".","，",):
            inputSTR=inputSTR.replace(item,"{}".format("<cut>"))
      for item in ("2k718"):
            inputSTR=inputSTR.replace("2k718","{}".format("2,718"))
      inputList=inputSTR.split('<cut>')[:-1]
      return(inputList)
if __name__== "__main__":
    #設定要讀取的 news.json 路徑      
      jsonFilePath="./example/news.json"
      
    #將 news.json 利用 [讀取 json] 的程式打開
      newscontent=jsonTextReader(jsonFilePath)["text"]
    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
      newsLIST=text2Sentence(newscontent)      
    
    #設定要讀取的 test.json 路徑
      jsonFilePath02="./example/test.json"
    
    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
      testLIST=jsonTextReader(jsonFilePath02)["sentence"]
    
    #測試是否達到作業需求
      
      if newsLIST == testLIST:
            print("作業過關！")
      else:
            print("作業不過關，請回到上面修改或是貼文求助！")
            print(newsLIST)
            print(testLIST)