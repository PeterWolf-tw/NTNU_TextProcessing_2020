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

    inputSTR = "The handsome boy stared at Mary and said nothing: he seemed offended by her manner. "
    coRefDICT = {"he":[],
                 "her":[]}

    resultBOOL = coRefResolver(inputSTR, " he ", "boy")
    if resultBOOL == True:
        coRefDICT["he"].append("boy")
    else:
        pass

    resultBOOL = coRefResolver(inputSTR, "her", "Mary")
    if resultBOOL == True:
        coRefDICT["her"].append("Mary")
    else:
        pass

    print(coRefDICT)