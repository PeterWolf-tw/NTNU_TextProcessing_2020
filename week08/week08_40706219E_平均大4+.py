#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

def nameMail(inputSTR):
    resultLIST = []
    tempLIST = []
    pat_name = re.compile("(?<=\(Neu\)  \(WHITESPACE\) ).+?(?=\(Nb\))|(?<=\(Cbb\)  \(WHITESPACE\) ).+?(?=\(Nb\))")
    pat_email = re.compile("((?<=\(Na\) \d{3}).+?(?=\,)|(?<=\(Na\) \d{3} ).+?(?=\,)|(?<=\(VD\) \d{3}).+?(?=\\n))")

    tempLIST.append([n.group(0) for n in pat_name.finditer(inputSTR)])
    tempLIST.append([e.group(1) for e in pat_email.finditer(inputSTR)])
    tempLIST[1].append('')
    for n,e in zip(tempLIST[0],tempLIST[1]):
        resultLIST.append([n,e])

    return resultLIST



if __name__ == "__main__":
    inputSTR = "(1)(Neu)  (WHITESPACE) 楊名霖(Nb)  40585220(Neu) I (FW) 華語(Na) 109 yml(Neu) 514@gmail.com(Neu) ,(COMMACATEGORY)  \n(WHITESPACE)" \
               "(2)(Neu)  (WHITESPACE) 陳彥寧(Nb)  40671109(Neu) H (FW) 科技(Na) 110(Neu)  nehcny@gmail(FW) .(DOTCATEGORY) com(FW) ,(COMMACATEGORY)  \n(WHITESPACE)" \
               "(3)(Neu)  (WHITESPACE) 陳俊維(Nb)  40671115(Neu) h (FW) 科技(Na) 110 wiwiw(Neu) 987654@hotmail(Neu) .(DOTCATEGORY) com(FW) ,(COMMACATEGORY)  \n(WHITESPACE)" \
               "(4)(Cbb)  (WHITESPACE) 黃婕姝(Nb)  40706219E (Nb) 人(Na) 發(VD) 111 jie.shu(FW) 703344@gmail(Neu) .(DOTCATEGORY) com \n(FW)" \
               "(5)(Neu)  (WHITESPACE) 黃智遠(Nb)  (WHITESPACE) 40571203(Neu) H (FW) 科技(Na) 109(Neu)"

    resultLIST = nameMail(inputSTR)
    print(resultLIST)#[["人名", "email"], ["人名", "email"], ...]
    #ckiptagger result：
    #[{(141, 144, 'PERSON', '黃婕姝'), (19, 21, 'LANGUAGE', '華語'),
    #(5, 8, 'PERSON', '楊名霖'), (48, 51, 'PERSON', '陳彥寧'), (91, 94, 'PERSON', '陳俊維')}]
