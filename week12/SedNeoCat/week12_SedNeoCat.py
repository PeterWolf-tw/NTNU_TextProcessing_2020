#!/usr/bin/env python3
import sys, typing, json
sys.path.append("../../week09/SedNeoCat/")
from ArticutAPI import ArticutAPI

def txtExtractor(path: str):
    with open(path, encoding="utf-8") as f:
        return f.readlines()

def text2Sentence(inputSTR: str):
    for item in ("、", "，", "。"):
        inputSTR = inputSTR.replace(item, '<cutting mark>')
    for item in ("...", "…"):
        inputSTR = inputSTR.replace(item, '')
    for i in range(len(inputSTR)):
        if inputSTR[i] == "," and inputSTR[i-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            inputSTR = inputSTR[:i]+"<cutting mark>"+inputSTR[i+1:]
    inputLIST = inputSTR.split('<cutting mark>')[:-1]
    return inputLIST

def keywordFilter(target: str, input: typing.List[str]):
    ret = []
    for x in input:
        pos = x.find(target)
        if pos >= 0:
            ret.append(x[pos:])
    return ret

def createJson(jsonPath, inputDict):
    with open(jsonPath, 'w', encoding='utf-8') as f:
        json.dump(inputDict, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    articut = ArticutAPI.Articut()
    result = {"倉鼠": [], "皇帝企鵝": []}
    mouseTxt = txtExtractor("text.txt")
    for txt in mouseTxt:
        tmp = articut.parse(txt, level="lv3")
        for x in tmp["event"]:
            if len(x) > 0:
                result["倉鼠"].append(tuple(x))
    penguinRawTxt = txtExtractor("penguin.txt")
    penguinSetence = []
    for x in penguinRawTxt:
        penguinSetence.extend(text2Sentence(x))
    penguinSetence = keywordFilter("皇帝企鵝", penguinSetence)
    for txt in penguinSetence:
        tmp = articut.parse(txt, level="lv3")
        for x in tmp["event"]:
            if len(x) > 0:
                result["皇帝企鵝"].append(tuple(x))
    print(result)
    createJson("week12_SedNeoCat.json", result)