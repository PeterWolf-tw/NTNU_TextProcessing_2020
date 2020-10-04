#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def myfunction(inputSTR):
    print(" ")
    print("Hello {}, {}".format(inputSTR, "你好"))

    inputSTRLIST = inputSTR.split(" ")
    print("我的名字：{}".format(inputSTRLIST[0]))
    print("我的學號：{}".format(inputSTRLIST[1]))


    messageSTR = """
    「程式設計與基礎資料型態與中文構詞學」
    整堂課的資訊量爆炸，在知識的海洋裡衝浪
    超過癮的啊啊啊啊！
    """
    print(messageSTR)
    
if __name__ == "__main__":
    nameSTR = "李名宥 40947042s"
    myfunction(nameSTR)