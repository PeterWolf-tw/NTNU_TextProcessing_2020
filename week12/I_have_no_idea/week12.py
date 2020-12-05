#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import json
from ArticutAPI import ArticutAPI

# hamster knowledge
# hamster verb
# king penguine 


def textRead():
    with open (txtPath,"r", encoding = "utf-8") as f:
        inputSTR = f.read()
        return inputSTR
    
# for the knowledge of hamsters

def getEvent(inputSTR, nlptool):
    eventDICT = articut.parse(inputSTR, level="lv3")
    return eventDICT

#compare to the event

def getVerb(inputSTR):
    verbDICT = articut.parse(inputSTR, level="lv3")
    verbLIST = articut.getVerbStemLIST(verbDICT,level = "lv2")
    return verbLIST

def jsonWriter(jsonDICT, jsonName):
    with open (jsonName, "w") as f:
        json.dump(jsonDICT, f, ensure_ascii = False)
        



if __name__ == "_main_":
    # hamster
    txtPath =  "text.txt"
    inputSTR_Hamster = textRead(txtPath)
    articut = ArticutAPI.Articut()
    
    eventDICT = getEvent(inputSTR_Hamster, articut)
    eventLIST = eventDICT["event"]
    eventLIST_Hamster = list(filter(None, eventLIST)) 
    print(eventLIST_Hamster)
    
    # compare EVENTS and VERBS
    verbLIST = getVerb(inputSTR_Hamster)
    

    
    #king penguines
    txtPath = "King_Penguines_Wiki.txt"
    inputSTR_Penguine = textRead(txtPath)
    articut = ArticutAPI.Articut()
    
    eventDICT = getEvent(inputSTR_Penguine, articut)
    eventLIST = eventDICT["event"]
    eventLIST_KingPenguines= list(filter(None, eventLIST)) 
    print(eventLIST_KingPenguines)
    
    jsonDICT = {
    "hamster": eventLIST_Hamster,
    "King penguines": eventLIST_KingPenguines
    }
    
    jsonName = "week12_I Have No Idea"
    jsonWriter(jsonDICT, jsonName)