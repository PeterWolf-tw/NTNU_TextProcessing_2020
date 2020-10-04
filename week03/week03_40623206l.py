# -*- coding:utf-8 -*-
'''
在 week03_你的學號.py 中，設計你的程式完成以下功能：
a. 讀取 example.txt 中的文字，並印出在畫面上
b. 仿照 week03_example.json 的格式，另外新增一個名為 week03_你的學號.json 的檔案，
   並將 example.txt 中的內容，利用 json 模組的dump() 寫入 week03_你的學號.json 中
c. 讀取 week03_你的學號.json 的內容，並印出在畫面上
'''
import json

def textReadAndPrint(txtFILE):
    # 讀入指定的純文字 txtFILE 檔案路徑，並回傳該檔案的內容
    with open(txtFILE, encoding="utf-8") as f:
        txtContent = f.read()
    return txtContent

def jsonFileWriter(jsonDICT, jsonFileName):
    # 輸入並轉換 jsonDICT 為 json (也就是文字資料)，檔名 = jsonFileName 
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False) #json檔用big-5開才不會亂碼
        # 亂碼問題: 如果只打 json.dump(jsonDICT, f) ，中文就會變成 \u67ef\u4f73\u5b3f
        
    return None

if __name__ == "__main__":
    txtFilePath = "./example.txt"
    txt = textReadAndPrint(txtFilePath) 
    # 執行 textReadAndPrint : txt 就等於剛剛傳入的檔案內的文字

    jsonDICT = {
    "name": {"zh":"", "en":""},
    "birth": {"year":"", "month":"", "date":""},
    "job": "",
    "language":[],
    "education":[],
    "spouse":""
    }

# \n 表示空格
    jsonDICT["name"]["zh"]      = txt.split("\n")[0].split(" ")[1]
    jsonDICT["name"]["en"]      = " ".join(txt.split("\n")[1].split(" ")[1:])
    jsonDICT["birth"]["year"]   = txt.split("\n")[2].split(" ")[1]
    jsonDICT["birth"]["month"]  = txt.split("\n")[2].split(" ")[3]
    jsonDICT["birth"]["date"]   = txt.split("\n")[2].split(" ")[5]
    jsonDICT["job"]             = txt.split("\n")[3].split("\t")[1]
    jsonDICT["language"]        = txt.split("\n")[4].split(" ")
    jsonDICT["education"]       = txt.split("\n")[5].split(" ")
    jsonDICT["spouse"]          = txt.split("\n")[6].split(" ")[1].split("（")[0]

    #似乎可以把 txt.split("\n") 跟 .split("") 變成一種指令，直接套用到每個參數...

    print(jsonDICT)
    jsonFileName = "week03_40623206l.json"
    jsonFileWriter(jsonDICT, jsonFileName)