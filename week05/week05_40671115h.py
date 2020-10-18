#!/usr/bin/env python3
# -*- coding:utf-8 -*-





def ccommandCoRefResolver(inputSTR, coRefKeySTR, personSTR):
   
   
   
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

def ccommandCoRefResolver(inputSTR, coRefKeySTR, personSTR):

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
        #inputSTR = ""
        #inputSTR
        #inputSTR
        inputSTR = "大雄聽胖虎的妹妹說靜香愛的是自己"
        inputLIST = {"大雄" , "聽" , "胖虎" , "的" , "妹妹" , "說" , "靜香" , "愛" , "的" , "是" , "自己"}
        coRefKeySTR = {inputLIST[10]:[]}
        
        resultBOOL = ccommandCoRefResolver(inputSTR , inputLIST[10] , inputLIST[0])
        if resultBOOL == True:
            coRefDICT["自己"].append("大雄")
        elif resultBOOL == None:
            pass
        else:
            pass
        
        resultBOOL = ccommandCoRefResolver(inputSTR , inputLIST[10] , inputLIST[6])
        if resultBOOL == True:
            coRefDICT["自己"].append("靜香")
        elif resultBOOL == None:
            pass
        else:
             pass
         
         resultBOOL = ccommandCoRefResolver(inputSTR , inputLIST[10] , inputLIST[2])
         if resultBOOL == True:
             coRefDICT["自己"].append("胖虎")
         elif resultBOOL == None:
             pass
         else:
             pass
     
         resultBOOL = ccommandCoRefResolver(inputSTR , inputLIST[10] , inputLIST[4])
         if resultBOOL == True:
             coRefDICT["自己"].append("妹妹")
         elif resultBOOL == None:
             pass
         else:
             pass
     
         print(coRefDICT)         