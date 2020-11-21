#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import nltk

#nltk.download('wordnet')
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perception_tagger')
#

#assignment: read the file and turn it into STRING 

def jsonReader ():
    with open (jsonFile, encoding = "utf-8") as f:
        jsonContent = json.loads(f)
        
    return jsonContent

#assignment b : split the sentence


    
def newsSegSentence():
    foxsentenceLIST = nltk.sent_tokenize(jsonContent, "chinese")
    print(foxsentenceLIST)
    return foxsentenceLIST

def newsSegWords():
    foxWordLIST = []
    for s in foxsentenceLIST:
        foxWordLIST.extend(nltk.word_tokenize(s, "chinese"))
    print(foxWordLIST)
    return foxWordLIST

def newsPOS():
    foxPOS = nltk.pos_tag(foxWordLIST)
    print(foxPOS)
    return foxPOS

def newsNER():
    foxNER = nltk.ne_chunk(foxPOS)
    print(foxNER)
    return foxNER

    
    