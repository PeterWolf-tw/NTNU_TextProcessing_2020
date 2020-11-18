#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import nltk

#讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open (jsonFilePath, "r", encoding = "utf8") as f:
        jsonContent = json.load(f)
    return jsonContent

def jsonFileWriter(jsonDICT, jsonFileName):
    """convert jsonDICT into a jsonFile and save it as jsonFileName."""
    with open (jsonFileName, mode = "w") as f:
        #json.dump(要寫入的資料, 目標檔案, 是否要讓輸入值為ascii)
        json.dump(jsonDICT, f, ensure_ascii = False)
        
if __name__== "__main__":
    jsonFilePath = "./foxnews.json" 
    jsonContent = jsonTextReader(jsonFilePath)
    foxnewsSTR = jsonTextReader(jsonFilePath)["content"] 
    
    foxsentenceLIST = nltk.sent_tokenize(foxnewsSTR)
    foxwordLIST = []
    for s in foxsentenceLIST:
        foxwordLIST.extend(nltk.word_tokenize(s))
    #print(foxwordLIST)
    
    foxPOS = nltk.pos_tag(foxwordLIST) #LIST
    #print(foxPOS)
    
    foxNER = nltk.ne_chunk(foxPOS)
    #print(foxNER)
    #print(type(foxNER))
    
    jsonContent["foxsentenceLIST"] = foxsentenceLIST
    jsonContent["foxwordLIST"] = foxwordLIST
    jsonContent["foxPOS"] = foxPOS
    jsonContent["foxNER"] = foxNER
    
    jsonFileName = "foxnews.json"
    jsonFileWriter(jsonContent, jsonFileName)       