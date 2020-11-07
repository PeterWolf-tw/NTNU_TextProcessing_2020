#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

def nameMail(inputSTR):
    resultLIST = []
    pat4Mail = re.compile(r"((?<=\(\d\)\s)\D+?(?=\s)).*?((?<=\s)[\d,\.,\w]+\@[\w,\.]+)")
    mailLIST = pat4Mail.findall(inputSTR)
    resultLIST.append(mailLIST)

    return resultLIST



if __name__ == "__main__":
    inputSTR = "(1) 徐政皓  40947043S 資工113    hsujinho@gmail.com (2) 陳辰      40784207I 華語111     40784207i@gapps.ntnu.edu.tw(3) 蔡傑穎  40943106S 生科113   1031_blank@we.still.dont.know (4) 劉鎧葶  40947018S 資工113   40947018s@gapps.ntnu.edu.tw(5) 溫嘉煒  40947057S 資工113   denny34456@gmail.com"
#因為有一名組員缺電子郵件
#原本是[10/30未知]但這樣我想不出來怎麼切，我就先修改了他的形式
    pos = "(1)(Cbb)  (WHITESPACE) 徐政皓(Nb)   40947043(Neu) S (FW) 資工(Na) 113    hsujinho@gmail(FW) .com \n(FW) ((PARENTHESISCATEGORY) 2(Neu) )(PARENTHESISCATEGORY)  (WHITESPACE) 陳辰      40784207I (Nb) 華語(Na) 111     40784207i@gapps.ntnu.edu.tw\n(Neu) (3)(Cbb)  (WHITESPACE) 蔡傑穎(Nb)   40943106S 生科(Neu) 113   10/31_blank@we.still.dont.know\n(Neu) (4)(Neu)  (WHITESPACE) 劉鎧葶(Nb)   40947018S (FW) 資工(Na) 113   40947018s@gapps.ntnu.edu.tw\n(Neu) (5)(Neu)  (WHITESPACE) 溫嘉煒(Nb)   40947057(FW) S (FW) 資工(Na) 113(Neu)    denny(FW) 34456@gmail(Neu) .(DOTCATEGORY) com(FW)"

    pat4NAME = re.compile(r"(?<=\(WHITESPACE\)).+?(?=[\(Nb\)\s])")
    print("NAMES",pat4NAME.findall(pos))

 
    resultLIST = nameMail(inputSTR)
    print("resultLIST",resultLIST)
