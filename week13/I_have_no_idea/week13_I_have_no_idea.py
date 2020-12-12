#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

from gensim.models import word2vec
from gensim import models

def jsonWriter(jsonName, jsonDICT):
    with open (jsonDICT,"w", encoding = 'utf-8') as f:
        json.dump(jsonDICT,f, ensure_ascii=False )



if __name__ == "__main__":

    simLIST = ["鬼滅之刃","宮崎駿","望塵莫及","望其項背","望梅止渴","奶茶","珍珠","仙草","伯爵","芋頭"]

    model = models.Word2Vec.load("wiki2019tw_word2vec_cbow_d100.model") #請適度調整你的模型目錄位置

    jsonDICT = {}
    
    for s in simLIST:
        simResult = model.most_similar((s),topn = 10)
        #儲存格式!!
        for simWord in simResult:
            print("{}, {}".format(simWord[0], str(simWord[1])))
        print('\n')
        
    jsonDICT[s] = simLIST
    #將上述結果，依作業說明另開一個新檔並儲存起來後，上傳 github 繳交。
    
    jsonWriter("./week13_vec_I have no idea.json", jsonDICT)