#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re

def nameMail(inputSTR):
    regexNameMail = re.compile(r"(?<=\(\d\)\s)(.+?)(?=\s).*?(?<=\s)(\w+\@[\w,\.]+)")
    resultLIST = []
    for i in regexNameMail.findall(inputSTR):
        resultLIST.append([i[0], i[1]])
    return resultLIST

if __name__ == "__main__":
    inputSTR = '(1) 余原齊 40947027S 資工113 adam20001002@gmail.com (2) 洪盛益 40947047S 資工113 i19780219111@kimo.com (3) 吳文元 40947030S 資工113 jw910731@ntnu.edu.tw (4) 李名宥 40947042S 資工113 jerry1030361@gmail.com (5) 蘇子權 40947023S 資工113 index20010928@gmail.com'
    pos = '(1)(Cbb)  (WHITESPACE) 余原齊(Nb)  40947027(Neu) S (FW) 資工(Na) 113 adam(FW) 20001002@gmail(Neu) .com (FW) (2)(Neu)  (WHITESPACE) 洪盛益(Nb)  40947047(Neu) S (FW) 資工(Na) 113(Neu)  i19780219111@kimo.com (FW) (3)(Neu)  (WHITESPACE) 吳文元(Nb)  40947030(Neu) S (FW) 資工(Na) 113(Neu)  jw(FW) 910731@ntnu.edu(Neu) .(DOTCATEGORY) tw (FW) (4)(Neu)  (WHITESPACE) 李名宥(Nb)  40947042(Neu) S (FW) 資工(Na) 113 jerry(Neu) 1030361@gmail.com (Neu) (5)(Neu)  (WHITESPACE) 蘇子權(Na)  40947023(Neu) S (FW) 資工(Na) 113(Neu)  index(FW) 20010928@gmail(Neu) .(DOTCATEGORY) com(FW)'
    regexName = re.compile(r"(?<=\(WHITESPACE\)\s)(.+?)(?=[\(Na\), \(Nb\)])")
    print(regexName.findall(pos))
    resultLIST = nameMail(inputSTR)
    print(resultLIST)