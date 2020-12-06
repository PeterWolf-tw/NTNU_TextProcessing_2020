#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json, nltk
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
from nltk import word_tokenize, sent_tokenize, pos_tag, ne_chunk
from collections import OrderedDict

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath, encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=OrderedDict)
def jsonRewriter(jsonFileName, jsonFileObject, inputDATALIST):
    resultDICT = {}
    origDICT = jsonTextReader(jsonFileName)
    with open(jsonFileName, "w", encoding="utf-8") as f:
        for o in jsonFileObject:
            resultDICT.setdefault(o,inputDATALIST[jsonFileObject.index(o)])
        origDICT.update(resultDICT)
        json.dump(origDICT, f, ensure_ascii=False)
    return None
def SWPNprocessReLIST(inputSTR):
    sentLIST = sent_tokenize(inputSTR)
    wordLIST = [word_tokenize(s) for s in sentLIST]
    POS = [pos_tag(w) for w in wordLIST]
    NER = [ne_chunk(t) for t in POS]
    return [sentLIST, wordLIST, POS, NER]


if __name__ == "__main__":
    ##斷句，foxsentenceLIST，sent_tokenize()
    ##段詞，foxwordLIST，word_tokenizer()
    ##POS處理，foxPOS，pos_tag()
    ##NER處理，foxNER，ne_chunk()
    ##重寫入原檔
    jsonFilePath = "foxnews.json"
    jsonFileObject = ["foxsentenceLIST", "foxwordLIST", "foxPOS", "foxNER"]
    inputSTR = jsonTextReader(jsonFilePath)["content"]
    DataLIST = SWPNprocessReLIST(inputSTR)
    jsonRewriter(jsonFilePath, jsonFileObject, DataLIST)
    ##確認重建檔能否讀取
    print(jsonTextReader(jsonFilePath)["foxNER"])
    ##確認能否在NER處理分別 White House // white house
    TinputSTR = jsonTextReader(jsonFilePath)["content"].replace("White House", "white house")
    TDataLIST = SWPNprocessReLIST(TinputSTR)
    DiffLIST = []
    for i in TDataLIST[3][0]:
        if i not in DataLIST[3][0]:
            DiffLIST.append(i)
    print("NER處理的不同結果：", DiffLIST)
