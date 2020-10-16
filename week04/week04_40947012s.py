#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(text):
        with open(text, encoding="utf-8") as f:
               txt = f.read()
        return txt



if __name__ == "__main__":
    a = ("./example/dbp.txt", "./example/pbd.txt")
    
    result = main(a[0])
    result = main(a[1])
    x = result.count("婦人")
    y = result.count("土狗")
    z = result.count("男")
    dbp = [("婦人", x), ("土狗", y), ("男", z)]
    pbd = [("婦人", x), ("土狗", y), ("男", z)]
    print("dbp:",dbp,", pbd:", pbd)
  