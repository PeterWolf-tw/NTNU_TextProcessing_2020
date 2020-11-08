#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

def nameMail(inputSTR):

    resA = re.findall(u"[\u4e00-\u9fa5]{3}" , inputSTR)
    resB = re.findall(r"\w+@\w+[.\w]+" , inputSTR)
    res_all = []
    for i in range(len(resA)):
     res_all.append([resA[i] , resB[i]])
    return res_all


if __name__ == "__main__":
    inputSTR = """(1) 劉庭妤 40623206l 地理110 orangeyuu31@gmail.com
    (2) 林遠邦 40747016S 資工111 bonjk87@gmail.com
    (3) 黃冠棠 40947025S 資工113 40947025S@ntnu.edu.tw
    (4) 釋永生 40947059S 資工113 wongsasueb@hotmail.com
    (5) 陳柏聿 40947069S 資工113 patpatpat1015@gmail.com""" 

    posSTR = "(Cbb)  (WHITESPACE) 劉庭妤(Nb)  40623206(Neu) l (FW) 地理(Na) 110(Neu)  orangeyuu31@gmail(FW) .com\n(FW) (2)(Neu)  (WHITESPACE) 林遠邦(Nb)  40747016(Neu) S (FW) 資工(Na) 111 bonjk87@gmail.com\n(Neu) (3)(Neu)  (WHITESPACE) 黃冠棠(Nb)  40947025(Neu) S (FW) 資工(Na) 113 (Neu) 40947025(Neu)S@ntnu.edu.tw\n(FW) ((PARENTHESISCATEGORY) 4(Neu) )(PARENTHESISCATEGORY)  (WHITESPACE) 釋(VC) 永生(VH)  40947059(Neu) S (FW) 資工(Na) 113(Neu)  wongsasueb@hotmail(FW) .(DOTCATEGORY) com\n(FW) (5)(Neu)  (WHITESPACE) 陳柏聿(Nb)  40947069(Neu) S (FW) 資工(Na) 113(Neu)  patpatpat(FW) 1015@gmail(Neu) .(DOTCATEGORY) com(FW)"

    reresult=re.findall(r"(?<=\(WHITESPACE\)\s)(.+?)(?=\(N[ab]\))",posSTR)
    resultLIST=nameMail(inputSTR)
    print("CKIPTagger: ", reresult)
    print("re: ", resultLIST)