def main(txtFILE):
    with open(txtFILE, encoding="utf-8") as f:
        txtSTR = f.read()
    return txtSTR

if __name__=="__main__":
    fileTUPLE = ("C:/Users/beckx/OneDrive/桌面/python/text_analyse/dbp.txt","C:/Users/beckx/OneDrive/桌面/python/text_analyse/pbd.txt")
    resultSTR = main(fileTUPLE[0])

    xINT = resultSTR.count("婦人")
    yINT = resultSTR.count("土狗")
    zINT = resultSTR.count("男")
    dbpLIST = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]
    print(fileTUPLE[0].spilt("/")[1], dbpLIST)

#   resultSTR = main(fileTUPLE[1])

#    xINT = resultSTR.count("婦人")
#    yINT = resultSTR.count("土狗")
#    zINT = resultSTR.count("男")
#    dbpLIST = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]
#    print(fileTUPLE[0].spilt("/")[1], pbdLIST)
