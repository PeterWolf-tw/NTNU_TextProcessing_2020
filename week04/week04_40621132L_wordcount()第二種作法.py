#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def openfile(txtFILE):
    with open (txtFILE, encoding="UTF-8") as f:
        txtSTR = f.read()
    return txtSTR

def wordcount(txtFILE, targetLIST):
    resultSTR = openfile(txtFILE)
    countLIST = []
    
    for i in range(len(targetLIST)):    
        xINT = resultSTR.count(targetLIST[i])
        countLIST.append((targetLIST[i], xINT))
        #以tuple形式加入list
    return countLIST
    

if __name__ == '__main__':
    txtfileTUPLE = ("example/dbp.txt","example/pbd.txt")
    targetLIST = ["婦人", "土狗", "男"]

    for i in range (len(txtfileTUPLE)):
        countLIST = wordcount(txtfileTUPLE[i], targetLIST)
        print(txtfileTUPLE[i].split("/")[1], ":", countLIST)
