#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random


def main(csvFILE):
    with open(csvFILE, encoding="big5") as f:
        csvSTR = f.read()
    csvLIST = csvSTR.split("\n")[1:-1]
    nameLIST = []
    while len(nameLIST)<=10:
        pickItem = random.choice(csvLIST)
        if pickItem in nameLIST:
            pass
        else:
            nameLIST.append(pickItem.split(",")[1:])

    return nameLIST

if __name__== "__main__":
    csvFileName = "./week04/all.csv"
    resultLIST = main(csvFileName)
    resultLIST.sort()
    for r in resultLIST:
        print(r)