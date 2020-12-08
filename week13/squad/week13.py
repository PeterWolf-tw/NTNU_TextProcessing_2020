#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from gensim.models import word2vec
from gensim import models
import json

def createJson(jsonPath, inputDICT):
    with open(jsonPath, 'w', encoding='utf-8') as f:
        json.dump(inputDICT, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":

    simLIST = ["工程師"]

    model = models.Word2Vec.load("C:\\Users\\ALICE\\Desktop\\wiki2019tw_word2vec_cbow_d300\\wiki2019tw_word2vec_cbow_d300.model") #請適度調整你的模型目錄位置
    
    resultDICT = {}

    for s in simLIST:
        simResult = model.most_similar((s),topn = 10)
        resultLIST = []
        for simWord in simResult:
            resultLIST.append(simWord[0])
            #print("{}, {}".format(simWord[0], str(simWord[1])))
        #print('\n')
        resultDICT[s] = resultLIST
        
    createJson('./w2v_squad.json', resultDICT)

    #將上述結果，依作業說明另開一個新檔並儲存起來後，上傳 github 繳交。