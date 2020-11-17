#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json, nltk

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