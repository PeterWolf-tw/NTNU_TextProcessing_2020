#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

jsonDict = dict()
jsonPath = './week03_40947027S.json'

def readTxt():
    print('Txt: ')
    with open('./example/example.txt', 'r', encoding='UTF-8') as f:
        txt = f.read()
        print(txt)
    return txt.split('\n')

def addJson():
    with open(jsonPath, 'w', encoding='UTF-8') as f:
        json.dump(jsonDict, f, ensure_ascii=False, indent=4)
    print('Add Json Successful\n')

def PrintJson():
    print('Json: ')
    with open(jsonPath, 'r', encoding='UTF-8') as f:
        js = json.loads(f.read())
        print(js)

if __name__ == "__main__":
    txtList = readTxt()
    jsonDict = {
        "name": {"zh":"", "en":""},
        "birth": {"year":"", "month":"", "date":""},
        "job": "",
        "language":[],
        "education":[],
        "spouse":""
    }
    for i in range(len(txtList)):
        if i==3: txt = txtList[i].split('\t')
        else: txt = txtList[i].split(' ')
        if i==0: jsonDict["name"]["zh"] = txt[1]
        elif i==1: jsonDict["name"]["en"] = " ".join(txt[1:])
        elif i==2:
            jsonDict["birth"]["year"] = txt[1]
            jsonDict["birth"]["month"] = txt[3]
            jsonDict["birth"]["date"] = txt[5]
        elif i==3: jsonDict["job"] = txt[1]
        elif i==4: jsonDict["language"] = txt[1].split('、')
        elif i==5: jsonDict["education"] = txt[1].split('、')
        elif i==6: jsonDict["spouse"] = txt[1].split('（')[0]
    addJson()
    PrintJson()