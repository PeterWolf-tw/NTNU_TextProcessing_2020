#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def main(inputSTR):

    inputSTRLIST = inputSTR.split(" ")
    print(inputSTRLIST)

    print("Name：{}".format(inputSTRLIST[0]))
    print("ID：{}".format(inputSTRLIST[1]))


    messageSTR = """
    「程式設計與基礎資料型態與中文構詞學」
    整堂課的資訊量爆炸，在知識的海洋裡衝浪
    超過癮的啊啊啊啊！
    """
    print(messageSTR)
#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR= "黃智遠 40571203H"
    main(nameSTR)