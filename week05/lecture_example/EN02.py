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

    inputSTR = "The handsome boy stared at John and said nothing: he seemed offended by his manner. "
    coRefDICT = {"he":[],
                 "his":[]}

    resultBOOL = coRefResolver(inputSTR, " he ", "boy")
    if resultBOOL == True:
        coRefDICT["he"].append("boy")
    else:
        pass

    resultBOOL = coRefResolver(inputSTR, " he ", "John")
    if resultBOOL == True:
        coRefDICT["he"].append("John")
    else:
        pass

    resultBOOL = coRefResolver(inputSTR, "his", "boy")
    if resultBOOL == True:
        coRefDICT["his"].append("boy")
    else:
        pass

    resultBOOL = coRefResolver(inputSTR, "his", "John")
    if resultBOOL == True:
        coRefDICT["his"].append("John")
    else:
        pass

    print(coRefDICT)