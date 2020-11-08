#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

nameMailRegexp = r'(?<=\) )(.*?) \d{8}[a-zA-Z] 資工113 (.*?)$'
posRegexp = r'(?<=\(WHITESPACE\) )(.*?)(?=\(Nb\))'
posData = '(1)(Cbb)  (WHITESPACE) 李詳弘(Nb)  40947026(Neu) S (FW) 資工(Na) 113 hello@birkhoff.me\n(FW) (2)(Neu)  (WHITESPACE) 何明曦(Nb)  40947029(Neu) S (FW) 資工(Na) 113 seanho12345@gmail(Neu) .com\n(FW) (3)(Neu)  (WHITESPACE) 郭泰維(Nb)  40847031(Neu) S (FW) 資工(Na) 113 511359@stu.tnssh.tn.edu.tw\n(Neu) (4)(Neu)  (WHITESPACE) 李紀為(Nb)  40947033(Neu) S (FW) 資工(Na) 113 wiki(FW) 900625@gmail.com\n(Neu) (5)(Neu)  (WHITESPACE) 蕭文政(Nb)  40947011(Neu) A (FW) 資工(Na) 113(Neu)  Beckxiao(FW) 2001323@gmail(Neu) .(DOTCATEGORY) com (FW)'

def nameMail(data):
  resultLIST = []
  
  for m in re.finditer(nameMailRegexp, data, re.MULTILINE):
    resultLIST.append([m.group(1), m.group(2)])

  return resultLIST

if __name__ == "__main__":
  p = re.findall(posRegexp, posData)
  print(p)
  
  inputSTR = """(1) 李詳弘 40947026S 資工113 hello@birkhoff.me
(2) 何明曦 40947029S 資工113 seanho12345@gmail.com
(3) 郭泰維 40847031S 資工113 511359@stu.tnssh.tn.edu.tw
(4) 李紀為 40947033S 資工113 wiki900625@gmail.com
(5) 蕭文政 40947011A 資工113 Beckxiao2001323@gmail.com"""

  resultLIST = nameMail(inputSTR)
  print(resultLIST)
