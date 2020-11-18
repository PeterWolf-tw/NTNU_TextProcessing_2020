#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json, nltk
nltk.download('words')

def readJson(jsonPath):
    with open(jsonPath, 'r', encoding='utf-8') as f:
        js = json.loads(f.read())
    return js

def updateJson(jsonPath, inputDict):
    with open(jsonPath, 'w', encoding='utf-8') as f:
        json.dump(inputDict, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    foxnewsJsonPath = './foxnews.json'
    foxnewsJson = readJson(foxnewsJsonPath)
    foxnewsSTR = foxnewsJson['content']
    foxsentenceLIST = nltk.sent_tokenize(foxnewsSTR)
    foxnewsJson['foxsentenceLIST'] = foxsentenceLIST
    foxwordLIST = []
    for i in foxsentenceLIST:
        foxwordLIST.extend(nltk.word_tokenize(i))
    foxnewsJson['foxwordLIST'] = foxwordLIST
    foxPOS = nltk.pos_tag(foxwordLIST)
    foxnewsJson['foxPOS'] = foxPOS
    foxNER = nltk.ne_chunk(foxPOS)
    foxnewsJson['foxNER'] = foxNER
    updateJson(foxnewsJsonPath, foxnewsJson)

    foxnewsSTR= foxnewsSTR.replace("White House","white house")
    foxsentenceLIST = nltk.sent_tokenize(foxnewsSTR)
    foxwordLIST = []
    for i in foxsentenceLIST:
        foxwordLIST.extend(nltk.word_tokenize(i))
    foxPOS = nltk.pos_tag(foxwordLIST)
    foxNER = nltk.ne_chunk(foxPOS)
    foxnewsJson=readJson('./foxnews.json')
    foxnewsJson_NER=foxnewsJson['foxNER']


    print("In foxNER:")
    for i in foxNER:
        if 'white' in i:
            print(i,end=" ")
        elif 'house' in i:
            print(i,end=" ")
    print("\n","In foxnewsJson:",sep="")
    for i in foxnewsJson_NER:
        for  j in i:
            if 'White' in j:
                print(j,end=" ")
            if 'House' in j:
                print(j,end=" ")
                exit()
