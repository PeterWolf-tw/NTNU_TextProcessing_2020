#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def cCommandCoRefResolver(inputLIST,coRefKeySTR,personSTR):
    if coRefKeySTR in inputLIST:
        pass
    else:
        raise ValueError
    if personSTR in inputLIST:
        pass
    else:
        raise ValueError

    personSTRIndex=inputLIST.index(personSTR)
    if inputLIST[personSTRIndex+1]=='的':
        return None
    elif inputLIST[personSTRIndex+1]=='之':
        return None
    else:
        pass
    coRefKeySTRIndex=inputLIST.index(coRefKeySTR)
    if coRefKeySTRIndex > personSTRIndex:
        return True
    else:
        return False

def coRefResolver(inputSTR, coRefKeySTR, personSTR):        
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
    


if __name__=="__main__":
    
    inputLIST=["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"]
    personLIST=[0,6,2,4]
    coRefDICT={inputLIST[10]:[]}

    resultBOOL=cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[0])
    if resultBOOL==True:
        coRefDICT[inputLIST[10]].append(inputLIST[0])
    elif resultBOOL==None:
        pass
    else:
        pass
    
    resultBOOL=cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[2])
    if resultBOOL==True:
       coRefDICT[inputLIST[10]].append(inputLIST[2])
    elif resultBOOL==None:
        pass
    else:
        pass

    resultBOOL=cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[4])
    if resultBOOL==True:
        coRefDICT[inputLIST[10]].append(inputLIST[4])
    elif resultBOOL==None:
            pass
    else:
            pass    
    resultBOOL=cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[6])
    if resultBOOL==True:
       coRefDICT[inputLIST[10]].append(inputLIST[6])
    elif resultBOOL==None:
        pass
    else:
        pass

    print(coRefDICT)