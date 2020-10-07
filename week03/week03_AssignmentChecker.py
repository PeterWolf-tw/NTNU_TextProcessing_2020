#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os

expectedDICT = {
    "name": {"zh":"柯佳嬿", "en":"Alice Ko"},
    "birth": {"year":"1985", "month":"1", "date":"10"},
    "job": "演員",
    "language":["國語", "臺語", "英語", "日語"],
    "education":["實踐大學應用外語學系肄業", "泰北高中", "臺北市立蘭雅國民中學", "臺北市士林區雨農國民小學"],
    "spouse":"謝坤達"
}

def week03JsonChecker(jsonFile):
    try:
        with open(jsonFile, encoding="utf-8") as f:
            jsonDICT = json.loads(f.read())
    except UnicodeDecodeError:
        try:
            with open(jsonFile, encoding="big5") as f:
                jsonDICT = json.loads(f.read())
        except UnicodeDecodeError:
            with open(jsonFile, encoding="gb") as f:
                jsonDICT = json.loads(f.read())

    if jsonDICT == expectedDICT:
        return True
    else:
        return False

if __name__ == "__main__":
    week03JsonFileLIST = [j for j in os.listdir("./") if j.endswith(".json") and j!="week03_YourSchoolID.json"]
    week03JsonFileLIST.sort()
    for j in week03JsonFileLIST:
        schoolID = j.split("_")[1].split(".json")[0]
        checkResultBOOL = week03JsonChecker(j)
        print("學號：{}，作業通過：{}".format(schoolID, checkResultBOOL))
