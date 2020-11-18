#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json, nltk

#讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open (jsonFilePath, "r") as f:
        jsonContent = json.load(f)
    return jsonContent

#寫入json的程式
def jsonFileWriter(jsonDICT, jsonFileName):
    """convert jsonDICT into a jsonFile and save it as jsonFileName."""
    with open (jsonFileName, mode = "w") as f:
        #json.dump(要寫入的資料, 目標檔案, 是否要讓輸入值為ascii)
        json.dump(jsonDICT, f, ensure_ascii = False)
        
def nltkTool(jsonDICT):
    
    foxnewsSTR = jsonDICT["content"] 
    foxsentenceLIST = nltk.sent_tokenize(foxnewsSTR)
    
    foxwordLIST = []
    for s in foxsentenceLIST:
        foxwordLIST.extend(nltk.word_tokenize(s))
    
    foxPOS = nltk.pos_tag(foxwordLIST) #LIST
    
    foxNER = nltk.ne_chunk(foxPOS)

    
    jsonDICT["foxsentenceLIST"] = foxsentenceLIST
    jsonDICT["foxwordLIST"] = foxwordLIST
    jsonDICT["foxPOS"] = foxPOS
    jsonDICT["foxNER"] = foxNER
    
    return jsonDICT
       
        
if __name__== "__main__":
    
    jsonFilePath = "./foxnews.json" 
    jsonDICT = jsonTextReader(jsonFilePath)
    nltkDICT = nltkTool(jsonDICT)
    
    jsonFileWriter(nltkDICT, jsonFilePath) 
    print(jsonTextReader(jsonFilePath)["foxNER"])
    
    compareDICT = nltkDICT
    compareDICT["content"] = compareDICT["content"].replace("White House", "white house")
    nltkDICT2 = nltkTool(compareDICT)
    print(nltkDICT2["foxNER"])
    
    