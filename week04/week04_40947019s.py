#!/usr/bin/env python3
# -*-coding:utf-8 _*_
def main(textFILE):
    with open(textFILE,encoding="UTF-8") as f:
        txt = f.read()
    return txt
if __name__=='__main__':
    fileTUPLE=("example/dbp.txt","example/pbd.txt")
    for i in range (2):
        resultSTR = main(fileTUPLE[i])
        xINT = resultSTR.count("婦人")
        yINT = resultSTR.count("土狗")
        zINT = resultSTR.count("男")
        dbpLIST = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]

        print(fileTUPLE[i].split("/")[1].split(".")[0]+':',format(dbpLIST).replace("\'","\""),sep='')
