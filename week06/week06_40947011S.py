import json

#讀取 json 的程式

def jsonTextReader(jsonFilePath):
	with open(jsonFilePath , "r" , encoding = "UTF-8") as f:
		res = json.load(f)
	return res

#將字串轉為「句子」列表的程式

def text2Sentence(inputSTR):
	numbers = [str(e) for e in range(10)]
	for e in ("，","、","。",):
		inputSTR = inputSTR.replace(e , "{Bon}")
	for e in ("…","．．．","..."):
		inputSTR = inputSTR.replace(e , "")
	for i in range(len(inputSTR)):
		if inputSTR[i] == "," and inputSTR[i - 1] not in numbers:
			inputSTR = inputSTR[:i] + "{Bon}" + inputSTR[i + 1:]
	res = inputSTR.split("{Bon}")[:-1]
	return res

if __name__== "__main__":
    #設定要讀取的 news.json 路徑

	n_path = "./python/text_analyse/week03_40947011S.json"

    #將 news.json 利用 [讀取 json] 的程式打開

	news_txt = jsonTextReader(n_path)["text"]

    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST

	newsLIST = text2Sentence(news_txt)

    #設定要讀取的 test.json 路徑

	t_path = "./python/text_analyse/week03_40947011S.json"

    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST

	testLIST = jsonTextReader(t_path)["sentence"]

    #測試是否達到作業需求

	if newsLIST == testLIST:
		print("作業過關！")
	else:
		print("作業不過關，請回到上面修改或是貼文求助！")