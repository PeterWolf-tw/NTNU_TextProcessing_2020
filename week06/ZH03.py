#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def sentence2LIST_v1(inputSTR):
    inputSTR = inputSTR.replace("\n", "")

    for item in ("「", "，", "、", "…", "」", "。"):
        inputSTR = inputSTR.replace(item, item+"<My_Cutting_Mark>")

    inputLIST = inputSTR.split("<My_Cutting_Mark>")
    return inputLIST


def sentence2LIST_v2(inputSTR):
    if "\n" in inputSTR:
        inputSTR = inputSTR.replace("\n", "")
    else:
        pass

    for item in ("「", "，", "、", "…", "」", "。"):
        inputSTR = inputSTR.replace(item, item+"<My_Cutting_Mark>")

    inputLIST = inputSTR.split("<My_Cutting_Mark>")
    return inputLIST

if __name__== "__main__":
    inputSTR = """一名男子今天清晨下大夜班，騎機車從中西區樹林街西
往東，清晨６時 10 分在南門路口遇上交通管制，繞了
３條路都繞不出南門路管制線，被困在府前路、南門路
與健康路包圍區域內，找不到回家的路，他詢問路口管
制交通的許姓警員。"""
    resultLIST = sentence2LIST_v1(inputSTR)
    print(resultLIST)