#!/usr/bin/env python3
# -*- coding:utf-8 -*-



def main(txtFILE):
    with open(txtFILE, encoding="utf-8") as f:
        txtSTR = f.read()

    xINT = txtSTR.count("婦人")
    yINT = txtSTR.count("土狗")
    zINT = txtSTR.count("男")
    LIST = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]
    return LIST



if __name__== "__main__":
    fileTUPLE = ("example/dbp.txt", "example/pbd.txt")
    resultSTR = main(fileTUPLE[0])

    print(fileTUPLE[0].split("/")[1][:-4]+":", resultSTR, end=", ")


    resultSTR = main(fileTUPLE[1])
    print(fileTUPLE[1].split("/")[1][:-4]+":", resultSTR)
