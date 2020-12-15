#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from gensim.models import word2vec
from gensim import models
import json

def createJSON(path, data):
  with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":

    simLIST = ["模型", "儲存", "格式", "課程", "智慧", "設計", "機器", "學習", "晚餐", "桌子"]

    model = models.Word2Vec.load("wiki2019tw_word2vec_cbow_d300.model") #請適度調整你的模型目錄位置
    result = {}
    for s in simLIST:
        simResult = model.most_similar((s),topn = 10)
        res = []
        for simWord in simResult:
            res.append(simWord[0])
            print("{}, {}".format(simWord[0], str(simWord[1])))
        print('\n')
        result[s] = res
    createJSON('./w2v_12345.json', result)

    #將上述結果，依作業說明另開一個新檔並儲存起來後，上傳 github 繳交。
