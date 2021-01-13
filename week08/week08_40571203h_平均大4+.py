#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

def nameMail():
    resultLIST=[]
    pat = re.compile("((?<=\(\d\)).+?(?=\s))")
    o = pat.findall(inputSTR)
    resultLIST.extend(o)

    return resultLIST



if __name__ == "__main__":
    inputSTR = "(1) 楊名霖 40585220I 華語109 yml514@gmail.com, (2) 陳彥寧 40671109H 科技110 nehcny@gmail.com, (3) 陳俊維 40671115h 科技110 wiwiw987654@hotmail.com, (4) 黃婕姝 40706219E 人發111 jie.shu703344@gmail.com,(5) 黃智遠 40571203H 科技109 hcytw0406@gmail.com,"
    posSTR="(1)(Cbb)  (WHITESPACE) 楊名霖(Nb)  40585220(Neu) I (FW) 華語(Na) 109 yml(FW) 514@gmail(Neu) .(DOTCATEGORY) com(FW) ,\n (FW) (2)(Cbb)  (WHITESPACE) 陳彥寧(Nb)  (WHITESPACE) 40671109(Neu) H (FW) 科技(Na) 110(Neu)  nehcny@gmail(FW) .(DOTCATEGORY) com(FW) ,\n(FW)  (WHITESPACE) (3)(Neu)  (WHITESPACE) 陳俊維(Nb)  (WHITESPACE) 40671115(Neu) h (FW) 科技(Na) 110(Neu)  wiwiw(FW) 987654@hotmail(Neu) .(DOTCATEGORY) com(FW) ,\n(FW)  (WHITESPACE) (4)(Cbb)  (WHITESPACE) 黃婕姝(Nb)  40706219(Neu) E (FW) 人(Na) 發(VD) 111(Neu)  jie(FW) .(DOTCATEGORY) shu(FW) 703344@gmail(Neu) .(DOTCATEGORY) com(FW) ,\n (FW) (5)(Neu)  (WHITESPACE) 黃智遠(Nb)  (WHITESPACE) 40571203(Neu) H (FW) 科技(Na) 109(Neu)  hcytw(FW) 0406@gmail(Neu) .(DOTCATEGORY) com(FW) ,(COMMACATEGORY)  (WHITESPACE)"
    resultLIST = nameMail(inputSTR)
    print(resultLIST)