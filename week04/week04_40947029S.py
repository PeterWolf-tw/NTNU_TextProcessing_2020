#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def main(txtFILE):
    with open(txtFILE, encoding="UTF-8") as f:
        txt = f.read()
    return txt


if __name__ == '__main__':
    fileTUPLE = ("example/dbp.txt","example/pbd.txt")

    for i in range(2):
        readSTR = main(fileTUPLE[i])
        xint = readSTR.count("婦人")
        yint = readSTR.count("土狗")
        zint = readSTR.count("男")
        LIST = [("婦人" ,xint), ("土狗" ,yint), ("男" ,zint)]
        print(fileTUPLE[i].split("/")[1]+":",sep="",end="")
        print("{}".format(LIST).replace("\'","\""),end=",")
