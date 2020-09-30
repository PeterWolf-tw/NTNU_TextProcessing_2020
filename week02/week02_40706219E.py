def main(inputSTR):
 nameSTR = inputSTR[:3]
 IDSTR = inputSTR[4::]
 print('1.利用substring index：')
 print('  我的姓名:{} 我的學號:{}'.format(nameSTR,IDSTR))
 print()
 inputSTRLIST=inputSTR.split(' ')
 print('2.利用split()：')
 print('  我的姓名:{} 我的學號:{}'.format(inputSTRLIST[0],inputSTRLIST[1]))
 print()
 messageSTR = """
 「程式設計與基礎資料型態與中文構詞學」
 整堂課的資訊量爆炸，在知識的海洋裡衝浪
 超過癮的啊啊啊啊！
 """
 print('附註：',messageSTR)

if __name__=='__main__':
    inputSTR='黃婕姝 40706219E'
main(inputSTR)
