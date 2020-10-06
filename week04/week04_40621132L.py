#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def openfile(txtFILE):
    with open (txtFILE, encoding="UTF-8") as f:
        txtSTR = f.read()
    return txtSTR

if __name__ == '__main__':
    txtfileTUPLE = ("example/dbp.txt","example/pbd.txt")

    for i in range (len(txtfileTUPLE)):
        resultSTR = openfile(txtfileTUPLE[i])
        
        xINT = resultSTR.count("婦人")
        yINT = resultSTR.count("土狗")
        zINT = resultSTR.count("男")
        countLIST = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]
        print(txtfileTUPLE[i].split("/")[1], ":", countLIST)

