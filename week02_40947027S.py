#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def func(inputStr):
    print("Hello {},".format(inputStr))
    messageStr = """
    「程式設計與基礎資料型態與中文構詞學」
    整堂課的資訊量爆炸，在知識的海洋裡衝浪
    超過癮的啊啊啊啊！
    """
    print(messageStr)
    inputSubList = inputStr.split(' ')
    print("Split Input String")
    for i in inputSubList:
        print(i, end=' ')

#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameStr = "余原齊 40947027S"
    func(nameStr)