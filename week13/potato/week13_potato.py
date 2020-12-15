#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

from gensim.models import word2vec
from gensim import models

def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w", encoding="utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

if __name__ == "__main__":

    simLIST = ["快樂", "恐龍", "書包", "蝴蝶", "運動", "睡覺", "小琉球", "充電器", "白板", "肉桂"]

    resultDICT = {}
    model = models.Word2Vec.load("wiki2019tw_word2vec_cbow_d300.model") #請適度調整你的模型目錄位置

    for s in simLIST:
        simResult = model.most_similar((s),topn = 10)
        resultLIST = []
        for simWord in simResult:
            resultLIST.append(simWord[0])
            print("{}, {}".format(simWord[0], str(simWord[1])))
        print('\n')
        resultDICT[s] = resultLIST
    jsonFileWriter(resultDICT, "./w2v_potato.json")

    #將上述結果，依作業說明另開一個新檔並儲存起來後，上傳 github 繳交。