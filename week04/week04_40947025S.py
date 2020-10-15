#!/usr/bin/env python3
# -*- coding:utf-8 -*-



def ReadAndCount(txtFILE):
    with open(txtFILE, encoding="utf-8") as f:
        txtSTR = f.read()
    xINT = txtSTR.count("婦人") 
    yINT = txtSTR.count("土狗")
    zINT = txtSTR.count("男")
    List = [xINT , yINT , zINT]
    return List







if __name__== "__main__":
    fileTUPLE = ("./example/dbp.txt", "./example/pbd.txt")
    dbpLIST = ReadAndCount(fileTUPLE[0])

    pbdLIST = ReadAndCount(fileTUPLE[1])

    print("dbp: [(\"婦人\", " + str(dbpLIST[0]) + "), (\"土狗\",  " +  str(dbpLIST[1]) + "), (\"男\", " +  str(dbpLIST[2]) + ")], pbd: [(\"婦人\", " +  str(pbdLIST[0]) + "), (\"土狗\", " + str(pbdLIST[1]) + "), (\"男\", " + str(pbdLIST[2]) + ")]！")
    