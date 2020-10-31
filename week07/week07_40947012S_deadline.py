#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json,jieba,os
def text2cws(jsonFilePath):
    with open(jsonFilePath,'r',encoding="utf-8") as f:
        js=json.load(f.read())
    inputSTR = js["BODY"]
     for item in("…","..."):
     inputSTR=inputSTR.replace(item,"")