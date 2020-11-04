#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

def nameMail(inputSTR):
    resultLIST = []
    patREGEX = re.compile(r"((?<=\(\d\)\s)\D+?(?=\s)).*?((?<=\s)[\w,\.]+?\@[\w,\.]+)")
    resultLIST = []    
    moLIST = patREGEX.findall(inputSTR)
    resultLIST.extend(moLIST)
    
    return resultLIST


if __name__ == "__main__":
    inputSTR = """(1) 陳孜旻 40621132L 英語110 40621132L@gapps.ntnu.edu.tw
    (2) 陳昕淼 40621138L 英語110 c1448422583@gmail.com
    (3) 陳峻逸 40775006H 電機111 dtank883@gmail.com
    (4) 黃冠瑋 40976013H 車能113 nightchen.huang@gmail.com
    (5) 顏毓廷 40640315S 數學110 yut061332@gmail.com"""
    pos = "(1)(Cbb)  (WHITESPACE) 陳孜旻(Nb)  40621132(Neu) L (FW) 英語(Na) 110 40621132(Neu) L@gapps.ntnu.edu.tw\n(FW) (2)(Neu)  (WHITESPACE) 陳昕淼(Nb)  40621138(Neu) L (FW) 英語(Na) 110(Neu)  c1448422583@gmail.com\n(FW) (3)(Neu)  (WHITESPACE) 陳峻逸(Nb)  40775006(Neu) H (FW) 電機(Na) 111 dtank(Neu) 883@gmail.com\n(Neu) (4)(Cbb)  (WHITESPACE) 黃冠瑋(Nb) 40976013(Neu) H (FW) 車能(Na) 113(Neu)  nightchen.huang@gmail(FW) .(DOTCATEGORY) com\n(FW) (5)(Neu)  (WHITESPACE) 顏毓廷(Nb)  (WHITESPACE) 40640315(Neu) S (FW) 數學(Na) 110(Neu)  yut(FW) 061332@gmail(Neu) .(DOTCATEGORY) com(FW)"
    NamePat = re.compile(r"(?<=\(WHITESPACE\)\s)\D+?(?=[\(Nb\), \(Na\)])")
    print("posName: ", NamePat.findall(pos))
    resultLIST = nameMail(inputSTR)
    print("regex:", resultLIST)