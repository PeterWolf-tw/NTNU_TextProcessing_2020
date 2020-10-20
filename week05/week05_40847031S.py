#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def coRefResolver(inputSTR, coRefKeySTR, personSTR):
    "給定要做消解的字串，回傳是否可能為指代字串"
    if coRefKeySTR in inputSTR:
        pass
    else:
        raise ValueError

    if personSTR in inputSTR:
        pass
    else:
        raise ValueError

    personSTRIndex = inputSTR.index(personSTR)
    if inputSTR[personSTRIndex + 1] == "的":
        return None
    else:
        pass

    coRefKeyIndex = inputSTR.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False

if __name__ == "__main__":

    #inputSTR = "小夫告訴大雄其實靜香喜歡的是他 "
    #inputSTR = "大雄知道靜香喜歡的是自己 "
    #inputSTR = "大雄聽胖虎說靜香愛的是自己 "
    # inputSTR = "大雄聽胖虎的妹妹說靜香愛的是自己"
    inputLIST = ["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT = {inputLIST[10]:[]}

    resultBOOL = coRefResolver(inputLIST, "自己", "大雄")
    if resultBOOL == True:
        coRefDICT["自己"].append("大雄")
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = coRefResolver(inputLIST, "自己", "靜香")
    if resultBOOL == True:
        coRefDICT["自己"].append("靜香")
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = coRefResolver(inputLIST, "自己", "胖虎")
    if resultBOOL == True:
        coRefDICT["自己"].append("胖虎")
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = coRefResolver(inputLIST, "自己", "妹妹")
    if resultBOOL == True:
        coRefDICT["自己"].append("妹妹")
    elif resultBOOL == None:
        pass
    else:
        pass

    print(coRefDICT)