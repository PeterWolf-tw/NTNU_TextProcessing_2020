#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI
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
  articut = ArticutAPI.Articut()
  tourContent = jsonTextReader("./tourblog.json")["content"]
  parsed = articut.parse(tourContent, level="lv2")

  print(parsed)
  locations = articut.getLocationStemLIST(parsed)
  print(locations)
