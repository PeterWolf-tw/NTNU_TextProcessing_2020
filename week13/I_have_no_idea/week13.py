#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from gensim.models import word2vec
from gensim import models


if __name__ == "__main__":

    simLIST = []

    model = models.Word2Vec.load("wiki2019tw_word2vec_cbow_d100.model") #請適度調整你的模型目錄位置

    for s in simLIST:
        simResult = model.most_similar((s),topn = 10)
        for simWord in simResult:
            print("{}, {}".format(simWord[0], str(simWord[1])))
        print('\n')

    #將上述結果，依作業說明另開一個新檔並儲存起來後，上傳 github 繳交。