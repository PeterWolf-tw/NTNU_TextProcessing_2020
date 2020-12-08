#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
def txtReader(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()
def getItemLIST(inputLIST):
    resultLIST = []
    try:
        for i in inputLIST:
            if i != [] and len(i[0]) == 3:
                resultLIST.append(i[0][2])
            elif i != [] and len(i) == 2:
                resultLIST.append(i)
    except TypeError:
        pass
    return resultLIST
def jsonWriter(jsonFileName, jsonFileObject, inputDATALIST):
    resultDICT = {}
    with open(jsonFileName, "w", encoding="utf-8") as f:
        for o in jsonFileObject:
            resultDICT.setdefault(o,inputDATALIST[jsonFileObject.index(o)])
        json.dump(resultDICT, f, ensure_ascii=False)
    return None

if __name__ == "__main__":
    from ArticutAPI import ArticutAPI
    myArti = ArticutAPI.Articut()
    FilePaths = ["example/text.txt", "example/pentext.txt"]
    jsonFileName = "week12_平均大4+.json"
    jsonFileObject = ["倉鼠", "皇帝企鵝"]

    resultEventLIST = []
    for p in FilePaths:
    ##取 event 和 verb list##
        try:
            print(myArti.parse(txtReader(p), level="lv3"))#確認用
            Event = getItemLIST(myArti.parse(txtReader(p), level="lv3")["event"])
            Dict = myArti.parse(txtReader(p), level="lv2")
            VList = getItemLIST(myArti.getVerbStemLIST(Dict))
        except MaxRetryError and ConnectionError:
            pass
        resultEventLIST.append(Event)
        print("Event:", Event)#確認用
        print("VList:", VList)#確認用
    ##比較不同之處並印出##
        ranELIST = []
        for i in Event:
            if len(i)==2:
                ranELIST.append(i[0])
                ranELIST.append(i[1])
            else:
                ranELIST.append(i)
        DiffLIST = []
        for i in VList:
            if i not in ranELIST:
                DiffLIST.append(i)
        print("event未提及的動詞：", DiffLIST)
    ##建檔##
    jsonWriter(jsonFileName, jsonFileObject, resultEventLIST)

    print(resultEventLIST)#確認用
