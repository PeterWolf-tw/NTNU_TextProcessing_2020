#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def myfunction(inputSTR):
    '''
    這支程式的主要函式(「函式」就是「功能」的意思！)
    '''
    print("Hello {},".format(inputSTR))

    myNameSTR = inputSTR[0:3]
    myIDSTR = inputSTR[4:]

    print("我的名字:{}".format(myNameSTR))
    print("我的學號:{}".format(myIDSTR))


    inputSTRLIST = inputSTR.split(" ")
    print(inputSTRLIST)
    print("我的名字：{}".format(inputSTRLIST[0]))
    print("我的學號：{}".format(inputSTRLIST[1]))





#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR = "顏毓廷 40640315S"

    myfunction(nameSTR)