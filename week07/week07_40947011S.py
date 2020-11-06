#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json, re, jieba
from pathlib import Path
from collections import Counter

def jsonTextReader(jsonFilePath):
  with open(jsonFilePath, encoding='utf-8-sig') as f:
    return json.load(f)

def termFreq(wordList):
  c = Counter()
  for x in wordList:
    if len(x) > 1 and x != '\r\n':
      c[x] += 1
  return c
  
def text2cws(path):
  text = jsonTextReader(path)["BODY"]
  return jieba.lcut(text)

if __name__ == "__main__":
  healthPathList = Path("./example/health").glob('**/*.json')
  healthDict = Counter()
  for pathObject in healthPathList:
    path = str(pathObject)
    healthDict += termFreq(text2cws(path))
    
  financePathList = Path("./example/finance").glob('**/*.json')
  financeDict = Counter()
  for pathObject in financePathList:
    path = str(pathObject)
    financeDict += termFreq(text2cws(path))

  print(dict(healthDict))
  print(dict(financeDict))
