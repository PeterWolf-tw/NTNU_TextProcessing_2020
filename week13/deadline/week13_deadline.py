#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from gensim.models import word2vec
from gensim import models
import json

def creatJson(path, item):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(item, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    simLIST = ["貓", "口罩", "雞胸肉", "巧克力", "屍體", "工程師", "肝", "耳機", "水壺", "廢物"]
    resultDict = {}
    model = models.Word2Vec.load("./wiki2019tw_word2vec_cbow_d300.model")
    for s in simLIST:
        simResult = model.most_similar((s),topn = 10)
        resultList = []
        for simWord in simResult:
            resultList.append(simWord[0])
            print("{}, {}".format(simWord[0], str(simWord[1])))
        print('\n')
        resultDict[s] = resultList
    creatJson("./w2v_deadline.json", resultDict)
