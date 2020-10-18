def cCommandCoRefResolver(inputLIST,coRefKeySTR,personSTR):
    if coRefKeySTR in inputLIST:
        pass
    else:
        raise KeyError

    if personSTR in inputLIST:
        pass
    else:
        raise KeyError

    personSTRIndex = inputLIST.index(personSTR)
    if inputLIST[personSTRIndex+1]=="的":
        return None
    elif inputLIST[personSTRIndex+1]=="之":
        return None
    else:
        pass

    CoRefKeyIndex = inputLIST.index(coRefKeySTR)
    if CoRefKeyIndex > personSTRIndex:
        return True
    else:
        return False


def coRefResolver(inputSTR,coRefKeySTR,personSTR):
    if coRefKeySTR in inputSTR:
        pass
    else:
        raise KeyError

    if personSTR in inputSTR:
        pass
    else:
        raise KeyError
    
    personSTRIndex = inputSTR.index(personSTR)
    CoRefKeyIndex = inputSTR.index(coRefKeySTR)

    if CoRefKeyIndex > personSTRIndex:
        return True
    else:
        return False

if __name__=="__main__":
    #inputSTR = "小夫告訴大雄其實靜香喜歡的是他 "
    #inputSTR = "大雄知道靜香喜歡的是自己 "
    #inputSTR = "大雄聽胖虎說靜香愛的是自己 "
    #inputSTR = "大雄聽胖虎的妹妹說靜香愛的是自己"
    inputLIST = ["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT = {inputLIST[10]:[]}

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10],inputLIST[0])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[0])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10],inputLIST[2])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[2])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10],inputLIST[4])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[4])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10],inputLIST[6])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[6])
    elif resultBOOL == None:
        pass
    else:
        pass

    print(coRefDICT)