#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(inputSTR):
    '''
    這支程式的主要函式(「函式」就是「功能」的意思！)
    '''
    print("Hello {},".format(inputSTR))
    inputSubSTR = inputSTR.split()
    #or myNameSTR = inputSTR[0:2]
    #   myIDSTR = inputSTR[4:12]

    messageSTR = """
    「程式設計與基礎資料型態與中文構詞學」
    整堂課的資訊量爆炸，在知識的海洋裡衝浪
    超過癮的啊啊啊啊！
    """
    print(messageSTR)
    print("我的名字：{}".format(inputSubSTR[0]))
    #print("我的名字：{}".format(myNameSTR))
    print("我的學號：{}".format(inputSubSTR[1]))
    #print("我的學號：{}".format(myIDSTR))


#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR = "陳孜旻 40621132L"
    main(nameSTR)
