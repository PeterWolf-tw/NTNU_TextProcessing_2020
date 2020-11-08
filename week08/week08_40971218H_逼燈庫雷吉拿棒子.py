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
    inputSTR = """(1) 朱品華 40971218H 科技113 syuhinka@gmail.com
    (2) 黃敏智 40971204H 科技113 mike0975400248@gmail.com
    (3) 黃彥明 40971214H 科技113 morefun.wp@gmail.com
    (4) 林楙惟 40971226H 科技113 waynelin0517@gmail.com
    (5) 古景睿 40971216H 科技113 3253qqz@gmail.com"""

    posSTR = "(Cbb)  (WHITESPACE) 朱品華(Nb)  40971218(Neu) H (FW) 科技(Na) 113(Neu)  syuhinka@gmail(FW) .com\n(FW) (2)(Neu)  (WHITESPACE) 黃敏智(Nb)  40971204(Neu) H (FW) 科技(Na) 113 mike0975400248@gmail(FW) .com\n(FW) (3)(Neu)  (WHITESPACE) 黃彥明(Nb)  40971214(Neu) H (FW) 科技(Na) 113 morefun.wp@gmail(FW) .com\n(FW) (4)(Neu)  (WHITESPACE) 林楙惟(Nb)  40971226(Neu) H (FW) 科技(Na) 113 waynelin0517@gmail(FW) .com\n(FW) (5)(Neu)  (WHITESPACE) 古景睿(Nb)  40971216H(Neu) H (FW) 科技(Na) 113 3253qqz@gmail(FW) .com"

    reresult=re.findall(r"(?<=\(WHITESPACE\)\s)(.+?)(?=\(N[ab]\))",posSTR)
    resultLIST=nameMail(inputSTR)
    print("CKIPTagger: ", reresult)
    print("re: ", resultLIST)
    