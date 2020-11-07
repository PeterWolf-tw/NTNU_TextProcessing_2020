#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

def nameMail(inputSTR):
    resultLIST=re.findall(r"(?<=\(\d\)).+?(?=\s\d)|(?<=\d\s).+?(?=\s\()",inputSTR)
    resultLIST.append(re.findall(r"(\w+@\w+\.com)",inputSTR)[-1])
    return resultLIST



if __name__ == "__main__":
    inputSTR = "(1)楊家明 40647003S 資工110 40647003s@gapps.ntnu.edu.tw (2)鍾暿峒 40647004S 資工110 40647004s@gapps.ntnu.edu.tw (3)劉怡萱 40647012S 資工110 40647012s@gapps.ntnu.edu.tw (4)偕為昭 40647021S 資工110 40647021s@gapps.ntnu.edu.tw (5)洪珮榕 40684227I 華語110 tinacircle19970616@gmail.com"
    posSTR = "(1)(Cbb) 楊家明(Nb)  40647003(Neu) S (FW) 資工(Na) 110(Neu)  (WHITESPACE) 40647003(Neu) s@gapps(FW) .ntnu(FW) .edu(FW) .(DOTCATEGORY) tw (FW) (2)(Cbb) 鍾暿峒(Nb)  40647004(Neu) S (FW) 資工(Na) 110(Neu)  (WHITESPACE) 40647004(Neu) s@gapps(FW) .ntnu.edu.(FW) tw (FW) (3)(Cbb) 劉怡萱(Nb)  40647012(Neu) S (FW) 資工(Na) 110(Neu)  (WHITESPACE) 40647012(Neu) s@gapps.ntnu.edu.(FW) tw (FW) (4)(Cbb) 偕為(VG) 昭(VE)  40647021S (Neu) 資工(Na) 110 (Neu) 40647021s@gapps.ntnu.edu.(Neu) tw (FW) (5)(Neu) 洪珮榕(Nb)  40684227(Neu) I (FW) 華語(Na) 110 tinacircle(FW) 19970616@gmail(Neu) .(DOTCATEGORY) com(FW)"

    ResultLIST=re.findall(r"(?<=\(4\)\(Cbb\)\s).+?(?=\(VG\))|(?<=\(VG\)).+?(?=\(VE\))|(?<=\(Cbb\)\s).+?(?=\(N[a,b]\))|(?<=\(\d\)\(Neu\)\s).+?(?=\(Nb\))",posSTR)
    print(ResultLIST)
    resultLIST = nameMail(inputSTR)
    print(resultLIST)
