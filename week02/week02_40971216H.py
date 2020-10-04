#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def myfunction(inputSTR):

    inputList= inputSTR.split(" ")
 
    print("我的名字：{}".format(inputList[0]))
    print("我的學號：{}".format(inputList[1]))



#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR = "古景睿 40971216H"

    myfunction(nameSTR)
