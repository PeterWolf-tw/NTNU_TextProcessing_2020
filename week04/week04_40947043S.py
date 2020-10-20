#!/usr/bin/env python3
# -*- coding:utf-8 -*-



def main(txtFILE):
    with open(txtFILE, encoding="utf-8") as f :
           txtSTR = f.read()
           return txtSTR


if __name__ == "__main__":
    list =["example/dbp.txt","example/pbd.txt"]

    resultSTR = main(list[0])
    xINT = resultSTR.count("婦人")
    yINT = resultSTR.count("土狗")
    zINT = resultSTR.count("男")
    dbplist = [("婦人",xINT),("土狗",yINT),("男",zINT)]
    
    print(list[0].spilt(",")[1],dbplist)



    resultSTR = main(list[1])
    pINT = resultSTR.count("婦人")
    qINT = resultSTR.count("土狗")
    rINT = resultSTR.count("男")
    pdblist = [("婦人",pINT),("土狗",qINT),("男",rINT)]
    print(list[1].spilt(",")[1],pdblist)