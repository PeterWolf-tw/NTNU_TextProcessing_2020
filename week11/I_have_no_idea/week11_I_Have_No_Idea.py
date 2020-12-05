#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# read dbp.txt and pdb.txt
# chartCount: count the character WITH 
# wordCount: count the word WITH 
# What is th e differnece between :　word and character?
# posWordCount
# contentWord

import json
from ArticutAPI import ArticutAPI

#week 03
def jsonWriter(jsonDICT, jsonName):
    with open(jsonName, "w") as f:
        json.dump(jsonDICT, f, ensure_ascii = False)
        
# characters
def charCounter(inputSTR):
    # .count(sub, start = , end = len(str))
    # https://www.runoob.com/python/att-string-count.html
    # DICT to LIST = 
    # .items() = 
    # .append(obj) = add the object into the LIST, 
    # versus .extend(seq) = MERGE two LISTS
    
    # dict{} = dictionary
    # dict[] = list; [0] = alphabet, [0:8] = interval
    
    characterDICT = {}
    for c in inputSTR:
        if c in characterDICT:
            pass
        else:
            characterDICT[c] = inputSTR.count(c)
            # meaning: 
    charCountLIST = []
    for c in characterDICT.items():
        charCountLIST.append(c)
        #meaning:
    charCountLIST.sort(key=lambda c: c[1], reverse=True)
    return charCountLIST

# unit 
def wordCounter(inputSTR):
    inputLIST = inputSTR.split("/")
    
    wordCountDICT = {}
    for w in inputLIST:
        pass
    else:
        wordCountDICT[w] = inputSTR.count(w)
        
    wordCountLIST = []
    for i in wordCountDICT.items():
        wordCountLIST.append(i)
        
    wordCountLIST.sort(key=lambda c: c[1], reverse=True)
    return wordCountLIST

# part of speech (with Articut)
def wordPlusPosCounter(inputSTR):
    inputSTR = inputSTR.replace("><","_SPLIT_")
    inputLIST = inputSTR.split("_SPLIT_")
    wordDICT = {}
    for w in inputLIST:
        if w in wordDICT:
            pass
        else:
            wordDICT[w] = inputSTR.count(w)
   
    wordCountLIST = []
    for i in wordDICT.items():
        wordCountLIST.append(i)
        
    wordCountLIST.sort(key=lambda c: c[1], reverse=True)
    return wordCountLIST

# get rid of function words
def contentWordPlusPosCounter(inputSTR):
    inputLIST = inputSTR.split("/")
    
    wordDICT = {}
    for w in inputLIST:
        if w in inputLIST:
            pass
        else:
            wordDICT[w] = inputLIST.count[w]
            
    wordCountLIST= []
    wordCountLIST.sort(key=lambda c: c[1], reverse=True)
    return wordCountLIST

if __name__ == "__main__":
    with open ("dbp.txt", encoding="utf-8") as f:
        dbpSTR = f.read()
    with open("pbd.txt", encoding="utf-8") as f:
        pbdSTR = f.read()
        
   # count the character
    charCount_dbp = charCounter(dbpSTR)
    charCount_pbd = charCounter(pbdSTR)
    
    articut = ArticutAPI.Articut()

   
   # count the word: parsing with Articut
   
    #what iF i PUT dbp all first?

#dbp
    seg_dbpSTR = ""
    for i in range(0, len(dbpSTR), 2000):
       
        resultDICT = articut.parse(dbpSTR[i:i+2000])
        seg_dbpSTR = seg_dbpSTR + resultDICT['result_segmentation']
    wordCount_dbp = wordCounter(seg_dbpSTR)
    
    pos_dbpLIST = []   
    for i in range(0, len(dbpSTR), 2000):
        pos_dbpLIST.extend(resultDICT["result_pos"])
        pos_dbpSTR = "".join([p for p in pos_dbpLIST if len(p)>1])
    posWordCount_dbp = wordPlusPosCounter(pos_dbpSTR)
    
    content_dbpLIST = []
    for i in range(0, len(dbpSTR), 2000):
        contentLIST = articut. getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c)>0:
                for w in c:
                    content_dbpLIST.append(w[-1])
        posContent_dbpSTR = "/".join(content_dbpLIST)
    contentWord_dbp = contentWordPlusPosCounter(posContent_dbpSTR) 
    
    
    
    
# pbd
    seg_pbdSTR = ""
    for i in range(0, len(pbdSTR), 2000):
   
        resultDICT = articut.parse(pbdSTR[i:i+2000])
        seg_pbdSTR = seg_pbdSTR + resultDICT['result_segmentation']
    wordCount_pbd = wordCounter(seg_pbdSTR)
    
    pos_pbdLIST = []  
    for i in range(0, len(pbdSTR), 2000):
        pos_pbdLIST.extend(resultDICT["result_pos"])
        pos_pbdSTR = "".join([p for p in pos_pbdLIST if len(p)>1])
    posWordCount_pbd = wordPlusPosCounter(pos_pbdSTR)
    
    content_pbdLIST = []    
    for i in range(0, len(pbdSTR), 2000):
        contentLIST = articut. getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c)>0:
                for w in c:
                    content_pbdLIST.append(w[-1])
        posContent_pbdSTR = "/".join(content_pbdLIST)
    contentWord_pbd = contentWordPlusPosCounter(posContent_pbdSTR)


    jsonDICT = {
       "charCount_dbp": charCount_dbp,
       "charCount_pbd": charCount_pbd,
       "wordCount_dbp": wordCount_dbp,
       "wordCount_pbd": wordCount_pbd,
       "posWordCount_dbp": posWordCount_dbp,
       "posWordCount_pbd": posWordCount_pbd,
       "contentWord_dbp": contentWord_dbp,
       "contentWord_pbd": contentWord_pbd
    }
   
   #for discussion 
    print("dbp_content_word", jsonDICT["contentWord_dbp"])
    print("pbd_content_word", jsonDICT["contentWord_pbd"])
    
    jsonName = "week 11_ TermFrequency"
    jsonWriter(jsonDICT, jsonName)
    

   
    
