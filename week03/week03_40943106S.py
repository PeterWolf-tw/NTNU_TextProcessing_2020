#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def textReadAndPrint(txtFILE):
    """Read the txtFile and print the content."""
    with open(txtFILE,encoding="utf-8") as f:txtContent= f.read()
    
    return txtContent

if __name__=="__main__":
    txtFilePath ="./example/example.txt"
    txt = textReadAndPrint(txtFilePath)
    jsonDICT = {
            "name":{"zh":"","month":"","date":""}
            "birth": {"year": "", "month": "", "date": ""},
            "job": "",
            "language": [],
            "education": [],
            "spouse": ""
        }
    
        jsonDICT["name"]["zh"] = txt.split("\n")[0].split(" ")[1]
        jsonDICT["name"]["en"] = "".join(txt.split("\n")[1].split(" ")[1:])
        jsonDICT["birth"]["year"] =  txt.split("\n")[2].split(" ")[1]
        jsonDICT["birth"]["month"] =  txt.split("\n")[2].split(" ")[3]
        jsonDICT["birth"]["date"] =  txt.split("\n")[2].split(" ")[5]
        jsonDICT["job"] = txt.split("\n")[3].split("\t")[1]
        jsonDICT["language"] = txt.split("\n")[4].split(" ")
        jsonDICT["education"] = txt.split("\n")[5].split(" ")
        jsonDICT["spouse"] = txt.split("\n")[6].split(" ")[1].split("(")[0]
    
        print(jsonDICT)
        jsonFileName = "week03_40571203H.json"
        jsonFileWriter(jsonDICT, jsonFileName)    