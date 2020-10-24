#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def sentence2LIST_v1(inputSTR):
    for item in ("「", "，", "…", "」", "。"):
        inputSTR = inputSTR.replace(item, item+"<My_Cutting_Mark>")
    resultLIST = inputSTR.split("<My_Cutting_Mark>")
    return resultLIST


if __name__== "__main__":
    inputSTR = "「不過SBL新球季改成單洋將，又限制身高，這樣讓我們這種4、5號位置的球員發揮空間較大，我當然希望可以多打一點…」范士恩說，「其實到現在我仍在學習，像是我的大學長周柏臣，感覺他在打內線的時候都很輕鬆。」"
    resultLIST = sentence2LIST_v1(inputSTR)
    print(resultLIST)