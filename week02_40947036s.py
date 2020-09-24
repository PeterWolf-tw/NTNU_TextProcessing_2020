def myfunction(inputSTR):

    inputList= inputSTR.split(" ")
 
    print("我的名字：{}".format(inputList[0]))
    print("我的學號：{}".format(inputList[1]))



#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR = "林彤頤 40947036S"

    myfunction(nameSTR)
