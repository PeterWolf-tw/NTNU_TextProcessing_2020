#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def read(textFile):
    with open(textFile, encoding="utf-8")as f:
        text_str=f.read()
    return text_str

def cnt(FT):
    Fir_str=read(FT)
    x=Fir_str.count("婦人")
    y=Fir_str.count("土狗")
    z=Fir_str.count("男")
    return [("婦人",x),("土狗",y),("男",z)]

if __name__ == "__main__":
    file_tuple=("./example/dbp.txt", "./example/pbd.txt")
    
    print("dbp.txt: ",cnt(file_tuple[0]))
    print("pbd.txt: ",cnt(file_tuple[1]))