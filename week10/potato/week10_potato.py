#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import nltk

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,"r",encoding="utf-8") as f:
        resultSTR = json.load(f)
    return resultSTR

def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w", encoding="utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

if __name__== "__main__":
    foxnewsJsonFile  = './foxnews.json'
    foxnews = jsonTextReader(foxnewsJsonFile)
    foxnewsContent = foxnews['content']

    foxsentenceLIST = nltk.sent_tokenize(foxnewsContent)
    foxnews['foxsentenceLIST'] = foxsentenceLIST
    
    foxwordLIST = []
    for s in foxsentenceLIST:
        foxwordLIST.extend(nltk.word_tokenize(s))
    foxnews['foxwordLIST'] = foxwordLIST
    
    foxPOS = nltk.pos_tag(foxwordLIST)
    foxnews['foxPOS'] = foxPOS

    foxNER = nltk.ne_chunk(foxPOS)
    foxnews['foxNER'] = foxNER
    #print(foxNER[:100])
    for NERitem in foxNER:
        for item in NERitem:
            #print(j)
            #print(NERitem[0])
            if 'White' in item:
                print(item,end=" ")
            if 'House' in item:
                print(item,end=" ")
    print()
    jsonFileWriter(foxnews, foxnewsJsonFile)

    foxnewsContent= foxnewsContent.replace("White House","white house")
    foxsentenceLIST = nltk.sent_tokenize(foxnewsContent)
    foxwordLIST = []
    for s in foxsentenceLIST:
        foxwordLIST.extend(nltk.word_tokenize(s))
    foxPOS = nltk.pos_tag(foxwordLIST)
    foxNER = nltk.ne_chunk(foxPOS)
    #print(foxNER[:100])
    for item in foxNER:
        if 'white' in item:
            print(item,end=" ")
        if 'house' in item:
            print(item,end=" ")
    print()
    