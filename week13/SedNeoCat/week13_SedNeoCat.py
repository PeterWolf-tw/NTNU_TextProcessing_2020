#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from gensim.models import word2vec
from gensim import models
import json

def createJson(jsonPath, inputDict):
    with open(jsonPath, 'w', encoding='utf-8') as f:
        json.dump(inputDict, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    simLIST = ['工程師', '貓', '狗', '外星人', '蘋果', '湯圓', '冬至', '物聯網', '女朋友', '臺灣']
    model = models.Word2Vec.load("./wiki2019tw_word2vec_cbow_d300.model")
    resultDict = {}
    for s in simLIST:
        simResult = model.most_similar((s),topn = 10)
        resultList = []
        for simWord in simResult:
            resultList.append(simWord[0])
            print("{}, {}".format(simWord[0], str(simWord[1])))
        print('\n')
        resultDict[s] = resultList
    createJson('./w2v_SedNeoCat.json', resultDict)
