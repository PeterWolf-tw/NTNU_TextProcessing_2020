#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def myfunction(inputSTR):
    '''
    這支程式的主要函式(「函式」就是「功能」的意思！)
    '''
    print("Hello {},".format(inputSTR))
    inputSplitSTR = inputSTR.split()

    print('我的名字:{}'.format(inputSplitSTR[0]))
    print('我的学号:{}'.format(inputSplitSTR[1]))


#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR = "陈昕淼 40621138L"

    myfunction(nameSTR)
