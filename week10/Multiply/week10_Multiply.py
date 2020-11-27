import json
import nltk

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath , encoding="utf-8") as f:
        jsonFile = json.loads(f.read())
    return jsonFile

def nltkProceing(inputSTR):
    foxsentenceLIST = nltk.sent_tokenize(inputSTR)
    foxwordLIST = []
    for s in foxsentenceLIST:
        foxwordLIST.extend(nltk.word_tokenize(s))
    foxPOS = nltk.pos_tag(foxwordLIST)
    foxNER = nltk.ne_chunk(foxPOS)
    
    jsonFile = {
    "content" : foxnewsSTR,
    "foxsentenceLIST" : foxsentenceLIST,
    "foxwordLIST" : foxwordLIST,
    "foxPOS" : foxPOS,
    "foxNER" : foxNER    
    }
    
    return jsonFile

if __name__== "__main__":
    FilePathSTR = "../example/foxnews.json"
    
    foxnewsSTR = jsonTextReader(FilePathSTR)["content"]
    
    jsonFile = nltkProceing(foxnewsSTR)
    
    print(jsonFile)
    
    with open('foxnews.json', 'w') as f:  
       json.dump(jsonFile, f,ensure_ascii=False,indent=2)
    
    foxnewsSTR = foxnewsSTR.replace('White House' , 'white house')
    
    jsonFile = nltkProceing(foxnewsSTR)
    
    print(jsonFile)