#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def of(txtFILE):
    with open (txtFILE, encoding="UTF-8") as f:
        txtSTR = f.read()
    return txtSTR

def wordcount(txtFILE):
    resultSTR = of(txtFILE)
        
    xINT = resultSTR.count("婦人")
    yINT = resultSTR.count("土狗")
    zINT = resultSTR.count("男")
    countLIST = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]
    return countLIST
    

if __name__ == '__main__':
    txtfiles = ("example/dbp.txt","example/pbd.txt")

    for i in range (len(txtfiles)):
        countLIST = wordcount(txtfiles[i])
        print(txtfiles[i].split("/")[1], ":", countLIST)