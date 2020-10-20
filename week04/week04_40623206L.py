'''
week04:
讀取 example 中的 dbp.txt 和 pbd.txt 兩個檔案的字串。
利用 .count() 計算 dbp 和 pbd 中的「婦人」、「土狗」、「男」各出現幾次，各自儲存為 x, y, z 三個變數。
將結果存在兩個 LIST 中，回傳 (return) 到程式進入點，並印出於畫面如後：dbp: [("婦人", x), ("土狗", y), ("男", z)], pbd: [("婦人", x), ("土狗", y), ("男", z)]！
'''

def openfile(txtFILE):
    with open (txtFILE, encoding="UTF-8") as f:
        txtSTR = f.read()
    return txtSTR

def CountList(txtTuple):
    for i in range(len(txtTuple)):
        resultSTR = openfile(txtTuple[i])
        xINT = resultSTR.count('婦人')
        yINT = resultSTR.count('土狗')
        zINT = resultSTR.count('男')
        CountList = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]
        name = txtTuple[i][8:11]
        print(name,':',CountList)
    return None
    

if __name__ == '__main__':
    txtTuple = ("example/dbp.txt","example/pbd.txt")
    CountList(txtTuple)