<<<<<<< HEAD:week05/week05_40947033S.py
def cCommandCoRefResolver(inputSTR, coRefKeySTR, personSTR):
    "給定要做消解的字串，利用 c-command 定理濾除不可能的人名，回傳可能的指代字串"
    "[注意]：這只是極度簡化，做為初步教學說明的版本！"

    if coRefKeySTR in inputSTR:
        pass
    else:
        raise KeyError

    if personSTR in inputSTR:
        pass
    else:
        raise KeyError

    personSTRIndex = inputSTR.index(personSTR)
    if inputSTR[personSTRIndex+len(personSTR)] == "的":
        return None
    else:
        pass

    coRefKeyIndex = inputSTR.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False

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

    #inputSTR = "小夫告訴大雄其實靜香喜歡的是他 "
    #inputSTR = "大雄知道靜香喜歡的是自己 "
    #inputSTR = "大雄聽胖虎說靜香愛的是自己 "
    #inputSTR = "大雄聽胖虎的妹妹說靜香愛的是自己"
    inputLIST = ["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT = {inputLIST[10]:[]}

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[0])
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

=======
def cCommandCoRefResolver(inputSTR, coRefKeySTR, personSTR):
    "給定要做消解的字串，利用 c-command 定理濾除不可能的人名，回傳可能的指代字串"
    "[注意]：這只是極度簡化，做為初步教學說明的版本！"

    if coRefKeySTR in inputSTR:
        pass
    else:
        raise KeyError

    if personSTR in inputSTR:
        pass
    else:
        raise KeyError

    personSTRIndex = inputSTR.index(personSTR)
    if inputSTR[personSTRIndex+len(personSTR)] == "的":
        return None
    else:
        pass

    coRefKeyIndex = inputSTR.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False

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

    #inputSTR = "小夫告訴大雄其實靜香喜歡的是他 "
    #inputSTR = "大雄知道靜香喜歡的是自己 "
    #inputSTR = "大雄聽胖虎說靜香愛的是自己 "
    #inputSTR = "大雄聽胖虎的妹妹說靜香愛的是自己"
    inputLIST = ["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT = {inputLIST[10]:[]}

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[0])
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

>>>>>>> 94503848294fa42910d91d52b119a41135a6be48:week05/week05_40621132L.py
    print(coRefDICT)