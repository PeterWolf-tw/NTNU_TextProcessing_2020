#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
week06:
a. 設計一 func() 名為 "jsonTextReader(jsonFilePath)"，
接受參數為 .json 格式的一個檔案，而 return 回傳值為 json 檔案中的 "text" 欄位的字串。

b. 設計一 func() 名為 "text2Sentence(inputSTR)"，
接受參數為字串，而 return 回傳值為一「斷句處理後」的 list。

c. 設計一程式進入點，透過前述 "jsonTextReader() 讀取 example/news.json 檔中
的 "text" 欄位的值，再透過 "text2Sentence()" 斷出完整的句子。

d. 程式進入點的最後輸出要和 example/test.json 中的 "sentenceLIST" 欄位的值
一致。
'''

import json

#a. 讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,'r', encoding="utf-8") as f:
        jsonContent =json.load(f)
    return jsonContent

#b. 將字串轉為「句子」列表的程式
#標點符號 會轉為 item
def text2Sentence(inputSTR):
    #刪節號會忽略，當成空白(就跟中文字後的英數字有空格一樣)
    for item in("...","…"):  
        inputSTR=inputSTR.replace(item,'')
    #一般中斷符號會當成要斷句的地方
    for item in("，","、","。"):
        inputSTR=inputSTR.replace(item,'<Cutting_Mark>')
    # print(inputSTR)
    # 處理另一種逗號 " , "
    for i in range(len(inputSTR)):
        # 後面的字是, 前面的是是數字 3,xxxx 就不行 => 前面一定是文字 ex: 我,xxxx => 這樣就要把, 當成中斷符號cut掉
        if inputSTR[i] == "," and inputSTR[i-1] not in ['0','1','2','3','4','5','6','7','8','9']:
            inputSTR = inputSTR[:i] + "<Cutting_Mark>" +inputSTR[i+1:]
    # print(inputSTR)
    
    #把斷開的句子都彙整成一個清單 inputLIST
    inputLIST=inputSTR.split('<Cutting_Mark>')[:-1]
    return inputLIST


if __name__== "__main__":
    #c.設定要讀取的 news.json 路徑
    jsonFilePath = './example/news.json'

    #c.將 news.json 利用 [讀取 json] 的程式打開，並打開text欄位的檔案 
    newsSTR=jsonTextReader(jsonFilePath)["text"] 

    #c.將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    # newsSTR 會跑到上面的 func() 成為 inputSTR
    # func()做出來的 inputLIST 會是 newsLIST
    newsLIST=text2Sentence(newsSTR)

    #d.設定要讀取的 test.json 路徑
    jsonFilePath2 = './example/test.json'

    #d.將 test.json 的 sentence(欄位) LIST 內容讀出，存為 testLIST
    testLIST=jsonTextReader(jsonFilePath2)["sentence"]
    # print(testLIST)
    # print(newsLIST)

    #d.測試是否達到作業需求
    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")
