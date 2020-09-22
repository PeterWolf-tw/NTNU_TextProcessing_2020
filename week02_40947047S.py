#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def myfunction(inputSTR):
    inputList=[]
    myName=inputSTR[0:2]
    myID=inputSTR[4:12]
    inputList_split=inputSTR.split(" ")
    print("姓名:{} 學號:{} ".format(myName,myID))


#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR = "洪盛益 40947047S"

    myfunction(nameSTR)