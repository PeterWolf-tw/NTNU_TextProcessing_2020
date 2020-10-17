#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def cCommandCoRefResolver(inputList, coRefKeySTR, personSTR):
    if not ((coRefKeySTR in inputList) and (personSTR in inputList)):
        raise ValueError
    personSTRIndex = inputList.index(personSTR)
    if inputList[personSTRIndex + 1] in ["的", "之"]:
        return None
    coRefKeyIndex = inputList.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False

if __name__ == "__main__":
    inputList = ["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"]
    personList = [0,6, 2, 4]
    target = inputList[10]
    coRefDict = {target:[]}
    for i in range(len(personList)):
        resultBOOL = cCommandCoRefResolver(inputList, target, inputList[personList[i]])
        if resultBOOL == True:
            coRefDict[target].append(inputList[personList[i]])
        elif resultBOOL == None:
            pass
        else:
            pass
    print(coRefDict)