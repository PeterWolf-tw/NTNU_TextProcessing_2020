#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json, nltk

#讀取 json 的程式
def jsonTextReader(jsonFilePath):
    try:
        with open (jsonFilePath, "r", encoding = "utf-8") as f:
            jsonContent = json.load(f)
    except UnicodeDecodeError:
        try:
            #用 Big-5 (encoding="cp950") 來開檔案
            with open (jsonFilePath, "r", encoding="cp950") as f:
                jsonContent = json.load(f)            
        except:
            #用 GB (encoding="gb") 來開檔案
            with open (jsonFilePath, "r", encoding="gb") as f:
                jsonContent = json.load(f)            
    return jsonContent

#寫入json的程式
def jsonFileWriter(jsonDICT, jsonFileName):
    """convert jsonDICT into a jsonFile and save it as jsonFileName."""
    with open (jsonFileName, mode = "w") as f:
        #json.dump(要寫入的資料, 目標檔案, 是否要讓輸入值為ascii)
        json.dump(jsonDICT, f, indent = 4, ensure_ascii = False)
        
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
    #print(jsonTextReader(jsonFilePath))
    
    compareDICT = {}
    compareDICT['content'] = nltkDICT["content"].replace("White House", "white house")
    #print(compareDICT)
    nltkDICT2 = nltkTool(compareDICT)
    
    print("In original foxNER:")
    print(nltkDICT['foxNER'])
    print()
    
    print("In replaced foxNER:")
    print(nltkDICT2['foxNER'])