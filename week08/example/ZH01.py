#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re




if __name__ == "__main__":
    inputLIST= ["這天章魚在街上撞到了一本書。",
    "這天章魚在桌面上看到了一本書。"]

    resultLIST = []
    pat = re.compile("(?<=在).*?(?=上)")
    for i in inputLIST:
        resultLIST.append([p.group(0) for p in pat.finditer(i)])

    print(resultLIST)
