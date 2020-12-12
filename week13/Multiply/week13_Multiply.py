#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from gensim.models import word2vec
from gensim import models


if __name__ == "__main__":

    simLIST = ["銀河" , "藪貓" , "大敗" , "地墊" , "馬祖" , "冷氣" , "充電器" , "棒球" , "罌粟" , "法拉利"]

    print("\nNow loading the model, please wait... it may take a few minutes\n")

    model = models.Word2Vec.load("D:/Download/wiki2019tw_word2vec_cbow_d300/wiki2019tw_word2vec_cbow_d300.model") #請適度調整你的模型目錄位置

    result = {}

    print("\nStart processing... please wait...\n")

    for s in simLIST:
        simResult = model.most_similar((s),topn = 10)
        result[s] = []
        for simWord in simResult:
            result[s].append(simWord[0])
            #print("{}, {}".format(simWord[0], str(simWord[1])))

    print("\nNow writing to w2v_Multiply.json...\n")

    with open("./w2v_Multiply.json" , "w" , encoding = "utf-8") as f:
        json.dump(result , f , ensure_ascii = False , indent = 4)

    print("\nDone!\n")

    #將上述結果，依作業說明另開一個新檔並儲存起來後，上傳 github 繳交。