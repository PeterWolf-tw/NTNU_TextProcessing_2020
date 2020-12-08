#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from gensim.models import word2vec
from gensim import models

def createJson(jsonPath, inputDict):
    with open(jsonPath, 'w', encoding='utf-8') as f:
        json.dump(inputDict, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":

    simLIST = ['吳文元', '裝弱', '踩地雷', '蘿莉控', '電神', '現充', '我就爛', '工程師', '土狗', '外星人']
    model = models.Word2Vec.load("./wiki2019tw_word2vec_cbow_d300.model")
    resultDict = {}

    for s in simLIST:
        simResult = model.most_similar((s),topn = 10)
        resultDict[s] = simResult 
        for simWord in simResult:
            print("{}, {}".format(simWord[0], str(simWord[1])))
        print('\n')
    createJson('./w2v_SedNeoCat.json', resultDict)