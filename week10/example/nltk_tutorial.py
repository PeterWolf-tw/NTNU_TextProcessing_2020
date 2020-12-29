#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import nltk

def main(inputSTR):
    sentenceLIST = nltk.sent_tokenize(inputSTR)
    return sentenceLIST


if __name__ == "__main__":
    inputSTR01 = """I went to Japan. (NOT I went to the Japan.)
He played tennis with Ben. (NOT He played tennis with the Ben.)
They had breakfast at 9 o’clock. (NOT They had a breakfast at 9 o'clock.)
(Some words don't have an article. We don't usually use articles for countries, meals or people.)"""


    inputSTR02 = """In essence, that's about as far as President Trump is likely to go. Even if he eventually acknowledges he won't be president from 20th January, he'll probably never relinquish his unsubstantiated claims that he was beaten in a fraudulent vote."""

    inputSTR03 = """雙 11 都過了。還在猶豫要不要入手新鍵盤嗎？K8 $200 折價券使用時間只到今天晚上 12 點，趕快把握時間下手最優惠！"""
    #resultLIST = main(inputSTR03)
    #print(resultLIST)

    #from nltk.stem import WordNetLemmatizer
    #lemm = WordNetLemmatizer()

    #from nltk.stem import PorterStemmer
    #stem = PorterStemmer()

    #inputWord = "communicating"
    #print("WordNetLemmatizer:", lemm.lemmatize(inputWord, pos="v"))
    #print("PorterStemmer:", stem.stem(inputWord))

    from nltk.corpus import stopwords

    #inputSTR01_content = ""
    #for i in inputSTR01:
        #if i.lower() in stopwords.words("english"):
            #inputSTR01_content = inputSTR01_content + "□"*len(i)
        #else:
            #inputSTR01_content = inputSTR01_content + i
    #print(inputSTR01_content)

    sentenceLIST = nltk.sent_tokenize(inputSTR01)
    wordLIST = []
    for s in sentenceLIST:
        wordLIST.extend(nltk.word_tokenize(s))
    #print(wordLIST)

    #contentLIST = []
    #for w in wordLIST:
        #if w.lower() in stopwords.words("english"):
            #contentLIST.append("□"*len(w))
        #else:
            #contentLIST.append(w)
    #print(contentLIST)
    #print(" ".join(contentLIST))

    posLIST = nltk.pos_tag(wordLIST)
    #print(posLIST)

    nerLIST = nltk.ne_chunk(posLIST)
    print(nerLIST)