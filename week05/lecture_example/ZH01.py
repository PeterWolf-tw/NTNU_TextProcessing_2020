#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def coRefResolver(inputSTR, coRefKeySTR, personSTR):
    "給定要做消解的字串，回傳可能的指代字串"
    if coRefKeySTR in inputSTR:
        pass
    else:
        raise KeyError

    if personSTR in inputSTR:
        pass
    else:
        raise KeyError

    personSTRIndex = inputSTR.index(personSTR)
    coRefKeyIndex = inputSTR.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False

if __name__ == "__main__":

    inputSTR = "小夫告訴大雄其實靜香喜歡的是他"
    coRefDICT = {"他":[]}

    resultBOOL = coRefResolver(inputSTR, "他", "小夫")
    if resultBOOL == True:
        coRefDICT["他"].append("小夫")
    else:
        pass

    resultBOOL = coRefResolver(inputSTR, "他", "大雄")
    if resultBOOL == True:
        coRefDICT["他"].append("大雄")
    else:
        pass

    print(coRefDICT)