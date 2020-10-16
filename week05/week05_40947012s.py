#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def cCommandCoRefResolver(inputLIST, coRefKeySTR, personSTR):
  
    if  coRefKeySTR in inputLIST:
       pass
    else:
        raise Error

    if personSTR in inputLIST:
        pass
    else:
        raise Error

    personSTRIndex = inputLIST.index(personSTR)
    if inputLIST[personSTRIndex+1] == "的":
        return None
    else:
        pass

    coRefKeyIndex = inputLIST.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False

if __name__ == "__main__":
    inputSTR = "大雄聽胖虎說靜香愛的是自己 "
    inputLIST = ["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT = {inputLIST[10]:[]}

    resultBOOL = cCommandCoRefResolver( inputSTR,inputLIST[10], inputLIST[0])
    if resultBOOL == True:
        coRefDICT["自己"].append("大雄")
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, "自己", "靜香")
    if resultBOOL == True:
        coRefDICT["自己"].append("靜香")
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, "自己", "胖虎")
    if resultBOOL == True:
        coRefDICT["自己"].append("胖虎")
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, "自己", "妹妹")
    if resultBOOL == True:
        coRefDICT["自己"].append("妹妹")
    elif resultBOOL == None:
        pass
    else:
        pass

    print(coRefDICT)