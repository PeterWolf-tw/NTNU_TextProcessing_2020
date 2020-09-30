#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(inputSTR):
    print("Hello {},".format(inputSTR))

    messageSTR = """
    「程式設計與基礎資料型態與中文構詞學」
    整堂課的資訊量爆炸，在知識的海洋裡衝浪
    超過癮的啊啊啊啊！
    """
    print(messageSTR)
    str=inputSTR.split()
    print(str[0])
    print(str[1])

#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR = "蘇子權 40947023S"
    main(nameSTR)