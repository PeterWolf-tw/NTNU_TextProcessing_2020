#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def cCommandCoRefResolver(inputSTR, coRefKeySTR, personSTR):
    "給定要做消解的字串，利用 c-command 定理濾除不可能的人名，回傳可能的指代字串"
    "[注意]：這只是極度簡化，做為初步教學說明的版本！"

    if coRefKeySTR in inputSTR:
        pass
    else:
        raise ValueError

    if personSTR in inputSTR:
        pass
    else:
        raise ValueError

    personSTRIndex = inputSTR.index(personSTR)
    if inputSTR[personSTRIndex+len(personSTR)] == "的":
        return None
    elif inputSTR[personSTRIndex+len(personSTR)] == "之":
        return None
    else:
        pass

    coRefKeyIndex = inputSTR.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False

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
    coRefKeyIndex = inputSTR.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False

if __name__ == "__main__":

    #inputSTR = "小夫告訴大雄其實靜香喜歡的是他 "
    #inputSTR = "大雄知道靜香喜歡的是自己 "
    #inputSTR = "大雄聽胖虎說靜香愛的是自己 "
    inputSTR = "大雄聽胖虎的妹妹說靜香愛的是自己"
    inputLIST = ["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT = {inputLIST[10]:[]}

    resultBOOL = cCommandCoRefResolver(inputSTR, inputLIST[10], inputLIST[0])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[0])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputSTR, inputLIST[10], inputLIST[6])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[6])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputSTR, inputLIST[10], inputLIST[2])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[2])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputSTR, inputLIST[10], inputLIST[4])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[4])
    elif resultBOOL == None:
        pass
    else:
        pass

    print(coRefDICT)