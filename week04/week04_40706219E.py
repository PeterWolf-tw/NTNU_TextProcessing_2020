#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def RCP(txtTuple, targetList):
    for i in range(len(txtTuple)):
        with open(txtTuple[i], encoding="utf-8") as F:
            txtSTR = F.read()
        txtName = txtTuple[i].split("/")[1].split(".")[0]
        countList = []
        for j in range(len(targetList)):
        	countList.append((targetList[j], txtSTR.count(targetList[j])))
        print(txtName, ':', countList)
    return None

if __name__ == "__main__":
    txtTuple=("example/dbp.txt", "example/pbd.txt")
    targetList=["婦人", "土狗", "男"]
    RCP(txtTuple, targetList)