import json
def txtrw (file):
    with open (file, encoding="UTF-8") as f:
        content = f.read()
        return content

def jsonrw (dict,filename):
    with open (filename ,mode = "w") as f:
        json.dump(dict, f, ensure_ascii = False)

if __name__ == "__main__":
    txtfile = "./example/example.txt"
    txt = txtrw(txtfile)
    print(txt)
    jsonDICT = {
    "name": {"zh":"", "en":""},
    "birth": {"year":"", "month":"", "date":""},
    "job":"",
    "language":[],
    "education":[],
    "spouse":""
    }

    jsonDICT["name"]["zh"] = txt.split("\n")[0].split(" ")[1]
    jsonDICT["name"]["en"] = " ".join(txt.split("\n")[1].split(" ")[1:])
    jsonDICT["birth"]["year"] = txt.split("\n")[2].split(" ")[1]
    jsonDICT["birth"]["month"] = txt.split("\n")[2].split(" ")[3]
    jsonDICT["birth"]["date"] = txt.split("\n")[2].split(" ")[5]
    jsonDICT["job"] = txt.split("\n")[3].split("\t")[1]
    jsonDICT["language"] = txt.split("\n")[4].split(" ")[1].split("、")
    jsonDICT["education"] = txt.split("\n")[5].split(" ")[1].split("、")
    jsonDICT["spouse"] = txt.split("\n")[6].split(" ")[1].split("（")[0]
    print("json:",jsonDICT,sep="\n")
    jsonfilename = "week03_40947029S.json"
    jsonrw(jsonDICT,jsonfilename)
