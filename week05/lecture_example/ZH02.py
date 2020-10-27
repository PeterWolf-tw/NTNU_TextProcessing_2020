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

    inputSTR = "大雄知道靜香喜歡的是自己 "
    coRefDICT = {"自己":[]}

    resultBOOL = coRefResolver(inputSTR, "自己", "大雄")
    if resultBOOL == True:
        coRefDICT["自己"].append("大雄")
    else:
        pass

    resultBOOL = coRefResolver(inputSTR, "自己", "靜香")
    if resultBOOL == True:
        coRefDICT["自己"].append("靜香")
    else:
        pass

    resultBOOL = coRefResolver(inputSTR, "自己", "胖虎")
    if resultBOOL == True:
        coRefDICT["自己"].append("胖虎")
    else:
        pass

    print(coRefDICT)