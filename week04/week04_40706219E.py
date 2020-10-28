#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def RCP(txtTuple):
    for i in range(len(txtTuple)):
        with open(txtTuple[i], encoding="utf-8") as F:
            txtSTR = F.read()
        xINT = txtSTR.count("婦人")
        yINT = txtSTR.count("土狗")
        zINT = txtSTR.count("男")
        txtName = txtTuple[i].split("/")[1].split(".")[0]
        countList = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]
        print(txtName, ':', countList)
    return None

if __name__ == "__main__":
    txtTuple=("example/dbp.txt", "example/pbd.txt")
    RCP(txtTuple)
