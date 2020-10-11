#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def myfunction(inputSTR):

    print("Dear Peterwolf:")

    messageSTR = """
    「程式設計與基礎資料型態與中文構詞學」
    整堂課的資訊量爆炸，在知識的海洋裡衝浪
    超過癮的啊啊啊啊！
    """
    print(messageSTR)

    inputSTRLIST = inputSTR.split(" ")
    print("我的名字：{}".format(inputSTRLIST[0]))
    print("我的學號：{}".format(inputSTRLIST[1]))

if __name__ == "__main__":
    nameSTR = "陳峻逸 40775006h"

    myfunction(nameSTR)