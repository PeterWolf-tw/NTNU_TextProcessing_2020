# !/usr/bin/env python3
# -*-coding:utf8 -*-
import re
def nameMail(inputSTR):
    ResultLIST=re.findall(r"(?<=\)).+?(?= )|(?<=\d ).+?(?= \(\d)",inputSTR)
    return ResultLIST
if __name__ == "__main__":
    inputSTR="(1)黃至瑜 40947012S 資工113 selina221947@gmail.com (2)孫韻婷 40947013S 資工113 melodysun90@gmail.com (3)彭安慈 40947019S 資工113 anci.peng@gmail.com (4)林彤頤 40947036S 資工113 walker2sunny@gmail.com (5)丁語婕 40947067S 資工112 sarah30135@gmail.com"
    PosSTR='(FW) (1)(Cbb) 黃至瑜(Nb)  40947012(Neu) S (FW) 資工(Na) 113 selina(Neu) 221947@gmail(Neu) .(DOTCATEGORY) com (FW) (2)(Cbb) 孫韻婷(Nb)  40947013(Neu) S (FW) 資工(Na) 113 melodysun(FW) 90@gmail(Neu) .(DOTCATEGORY) com (FW) (3)(Cbb) 彭安慈(Nb)  (WHITESPACE) 40947019(Neu) S (FW) 資工(Na) 113(Neu)  anci(FW) .(DOTCATEGORY) peng@gmail(FW) .(DOTCATEGORY) com (FW) (4)(Cbb) 林彤頤(Nb)  40947036(Neu) S (FW) 資工(Na) 113 walker2sunny@gmail(FW) .com (FW) (5)(Cbb) 丁語婕(Na)  40947067(Neu) S (FW) 資工(Na) 112 sarah(FW) 30135@gmail(Neu) .(DOTCATEGORY) com(FW)'
    ReResulLIST=re.findall(r"(?<=\(Cbb\) ).+?(?=\(Nb\))|(?<=\(Cbb\) ).+?(?=\(Na\))",PosSTR)
    ResultLIST=nameMail(inputSTR)
    print(ReResulLIST)
    print(ResultLIST)