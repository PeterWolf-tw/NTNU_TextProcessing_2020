#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# in cmd: 

    #pip install nltk
    #pip install numpy
#python:
    #nltk.download('wordnet')
    #nltk.download('punkt')
    #nltk.download('stopwords')
    #nltk.download('maxent_ne_chunker')
    #nltk.download('averaged_perceptron_tagger')
    #nltk.download('words')

#"""read, write, nltk,sentence+words+pos+ner """

#assignment: read the file and turn it into STRING 


import json
import nltk

#week03 !!
def jsonReader(jsonFilePath):
    try:    
        with open (jsonFilePath, "r", encoding = "utf-8") as f:
            jsonContent = json.load(f)
    # !! UnicodeDecodeError!!
    except UnicodeDecodeError:
        try:
            with open(jsonFilePath, "r", encoding = "cp950") as f:
                jsonContent = json.load(f)
        except:
            with open(jsonFilePath, "r", encoding = "gb") as f:
                jsonContent = json.load(f)            
    return jsonContent
    #unexpected unindent ? 
    
def jsonWriter(jsonDICT, jsonFileName):
    with open (jsonFileName, mode = "w", encoding = "utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii= False)

#assignment b : 

def nltk_processed(jsonDICT):
    
#SegSentence:
    news= jsonDICT["content"]
    foxsentenceLIST = nltk.sent_tokenize(news)

#SegWords:
    foxWordLIST = []
    for s in foxsentenceLIST:
        foxWordLIST.extend(nltk.word_tokenize(s))

#newsPOS:
    foxPOS = nltk.pos_tag(foxWordLIST)

#def newsNER:
    foxNER = nltk.ne_chunk(foxPOS)
    
    jsonDICT["foxsentenceLIST"] = foxsentenceLIST
    jsonDICT["foxWordLIST"] = foxWordLIST
    jsonDICT["foxPOS"] = foxPOS
    jsonDICT["foxNER"] = foxNER

    return jsonDICT


if __name__ == "__main__":
    jsonFilePath = "./foxnews.json"
    jsonDICT= jsonReader(jsonFilePath)
    
    resultDICT = nltk_processed(jsonDICT)

    print(resultDICT["foxNER"])
    
    
    jsonWriter(resultDICT, jsonFilePath)
    
# NER: 
# swap White House for white house to see the whether Name Entity Recognition result is different or not
    swapDICT = {}
    swapDICT["content"] = resultDICT["content"].replace("White House", "white house")
    print(swapDICT["content"])
    NER_testerDICT = nltk_processed(swapDICT)
    
    #TypeError: string indices must be integers
    #TypeError: list indices must be integers or slices, not str
    
    #solution:｛｝
    
    print("foxNER_capital:", resultDICT["foxNER"])
    print("foxNER_lower", NER_testerDICT["foxNER"])
    
    #NER_TEST　　　　FACILITY versus 