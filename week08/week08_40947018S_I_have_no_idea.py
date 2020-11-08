#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

def nameMail(inputSTR):
    resultLIST = []
    pat = re.compile(r"((?<=\(\d\)\s)\D+?(?=\s)).*?((?<=\s)[\d,\.,\w]+\@[\w,\.]+|(?<=\d)未知)")
    resultLIST = pat.findall(inputSTR)

    return resultLIST



if __name__ == "__main__":
    inputSTR = "(1) 徐政皓  40947043S 資工113    hsujinho@gmail.com(2) 陳辰      40784207I 華語111     40784207i@gapps.ntnu.edu.tw(3) 蔡杰穎  40943106S 生科113   [10/31未知](4) 劉鎧葶  40947018S 資工113   40947018s@gapps.ntnu.edu.tw(5) 溫嘉煒  409470  S 資工113     denny34456@gmail.com"
    
    posSTR = "(1)(Cbb)  (WHITESPACE) 徐政皓(Nb)   40947043(Neu) S (FW) 資工(Na) 113    hsujinho@gmail(FW) .com \n(FW) ((PARENTHESISCATEGORY) 2(Neu) )(PARENTHESISCATEGORY)  (WHITESPACE) 陳辰      40784207I (Nb) 華語(Na) 111     40784207i@gapps.ntnu.edu.tw\n(Neu) (3)(Cbb)  (WHITESPACE) 蔡杰穎(Nb)   40943106(Neu) S 生科(Na) 113   [10/31(Nd) 未知(VJ) ]\n(FW) (4)(Cbb)  (WHITESPACE) 劉鎧葶(Nb)   40947018S (FW) 資工(Na) 113   40947018s@gapps.ntnu.edu.tw\n(Neu) (5)(Neu)  (WHITESPACE) 溫嘉煒(Nb)   409470(FW)   S (FW) 資工(Na) 113(Neu)      denny(FW) 34456@gmail(Neu) .(DOTCATEGORY) com(FW)"
    pat = re.compile(r"(?<=\(WHITESPACE\)).+?(?=[\(Nb\)\s])")
    print("Names",pat.findall(posSTR))
    
    resultLIST = nameMail(inputSTR)
    print("resultLIST",resultLIST)