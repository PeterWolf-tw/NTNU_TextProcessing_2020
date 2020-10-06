#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def readTxt(path):
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()
    return txt

def count(fileStr):
    return [("婦人", fileStr.count("婦人")), ("土狗", fileStr.count("土狗")), ("男", fileStr.count("男"))]

if __name__ == "__main__":
    fileName = ('dbp.txt', 'pbd.txt')
    for i in range(2):
        print(fileName[i], ': ', count(readTxt('./example/' + fileName[i])))

