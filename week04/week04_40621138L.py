#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def openfile(txtFILE):
    with open (txtFILE, encoding="UTF-8") as f:
        txtSTR = f.read()
    return txtSTR

def CountList(txtTuple):
    for i in range(len(txtTuple)):
        File = openfile(txtTuple[i])
        xINT = File.count('婦人')
        yINT = File.count('土狗')
        zINT = File.count('男')
        CountList = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]
        name = txtTuple[i][8:11]
        print(name,':',CountList)
    return None
    

if __name__ == '__main__':
    txtTuple = ("example/dbp.txt","example/pbd.txt")
    CountList(txtTuple)
