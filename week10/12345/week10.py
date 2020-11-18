#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json, nltk

def jsonTextReader(jsonFilePath):
  with open(jsonFilePath, encoding='utf-8-sig') as f:
    return json.load(f)

def createJSON(path, data):
  with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

def analyseText(json):
  foxnewSTR = json["content"]
  foxsentenceLIST = nltk.sent_tokenize(foxnewSTR)
  
  foxwordLIST = []
  for s in foxsentenceLIST:
    foxwordLIST.extend(nltk.word_tokenize(s))

  foxPOS = nltk.pos_tag(foxwordLIST)
  foxNER = nltk.ne_chunk(foxPOS)
  
  return {
    'foxsentenceLIST': foxsentenceLIST,
    'foxwordLIST': foxwordLIST,
    'foxPOS': foxPOS,
    'foxNER': foxNER
  }

if __name__ == "__main__":
  # nltk.download('punkt')
  # nltk.download('averaged_perceptron_tagger')
  # nltk.download('maxent_ne_chunker')
  # nltk.download('words')
  
  jsonDict = jsonTextReader("./foxnews.json")
  originalResult = analyseText(jsonDict)
  
  createJSON("./foxnews.json", {**jsonDict, **originalResult})

  jsonDict["content"] = jsonDict["content"].replace("White House", "white house")
  editedResult = analyseText(jsonDict)
  
  print(originalResult['foxNER'])
  print(editedResult['foxNER'])
