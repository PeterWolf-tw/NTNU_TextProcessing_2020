#!/usr/bin/env python3
# -*- coding:utf-8 -*-



def main(txtFILE):
    with open(txtFILE, encoding="utf-8") as f:
        txtSTR = f.read()
    return txtSTR


if __name__== "__main__":
    fileTUPLE = ("./example/dbp.txt", "./example/pbd.txt")
    txtSTR = main(fileTUPLE[0])

    x = txtSTR.count("婦人")
    y = txtSTR.count("土狗")
    z = txtSTR.count("男")
    dbpLIST = [("婦人", x), ("土狗", y), ("男", z)]
    print(fileTUPLE[0].split("/")[1], dbpLIST)


    resultSTR = main(fileTUPLE[1])
    xINT = resultSTR.count("婦人")
    yINT = resultSTR.count("土狗")
    zINT = resultSTR.count("男")
    pbdLIST = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]
    print(fileTUPLE[1].split("/")[1], pbdLIST)