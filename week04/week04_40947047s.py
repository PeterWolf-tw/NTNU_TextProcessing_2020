#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def fileRead(fileSTR):
    with open(fileSTR,encoding="utf-8") as f:
        resultSTR=f.read()
    return resultSTR

def counter(STR):
    x=STR.count("婦人")
    y=STR.count("土狗")
    z=STR.count("男")
    return x,y,z

if __name__ == "__main__":
    fileTUP=("example/dbp.txt","example/pbd.txt")

    resultSTR1=fileRead(fileTUP[0])
    xINT,yINT,zINT=counter(resultSTR1)
    print("dbp:[(\"婦人\",{0}),(\"土狗\",{1}),(\"男\",{2})]".format(xINT,yINT,zINT))

    resultSTR2=fileRead(fileTUP[1])
    xINT,yINT,zINT=counter(resultSTR2)
    print("pbd:[(\"婦人\",{0}),(\"土狗\",{1}),(\"男\",{2})]".format(xINT,yINT,zINT))
