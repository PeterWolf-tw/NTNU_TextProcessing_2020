#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import json
from ArticutAPI import ArticutAPI

# hamster knowledge
# hamster verb
# king penguine 


def textRead(txtPath):
    with open (txtPath,"r", encoding = "utf-8") as f:
        inputSTR = f.read()
        return inputSTR
    
# for the knowledge of hamsters

def getEvent(inputSTR, nlptool):
    eventDICT = articut.parse(inputSTR, level="lv3")
    return eventDICT

#compare to the event

def getVerb(inputSTR):
    verbDICT = articut.parse(inputSTR, level="lv2")
    verbLIST = articut.getVerbStemLIST(verbDICT,level = "lv2")
    return verbLIST

def jsonWriter(jsonDICT, jsonName):
    with open (jsonName, mode = "w") as f:
        json.dump(jsonDICT, f, ensure_ascii = False)
        



if __name__ == "_main_":
    # hamster
    
    inputSTR_Hamster = textRead("text.txt")
    articut = ArticutAPI.Articut()
    
    resultLIST = getEvent(inputSTR_Hamster, articut)
    eventLIST = resultLIST["event"]
    eventLIST_Hamster = list(filter(None, eventLIST)) 
    print(eventLIST_Hamster)
    
    # compare EVENTS and VERBS
    verbLIST = getVerb(inputSTR_Hamster)
    print(verbLIST)

    
    #king penguines
    
    inputSTR_Penguine = textRead("King_Penguines_Wiki.txt")
    articut = ArticutAPI.Articut()
    
    resultLIST = getEvent(inputSTR_Penguine, articut)
    eventLIST = resultLIST["event"]
    eventLIST_KingPenguines= list(filter(None, eventLIST)) 
    print(eventLIST_KingPenguines)
    
    jsonDICT = {
    "hamster": eventLIST_Hamster,
    "King penguines": eventLIST_KingPenguines
    }
    
    jsonName = "week12_I Have No Idea"
    jsonWriter(jsonDICT, jsonName)