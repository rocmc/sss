# conding: euc-kr

list = [1, 3, 5, 7, 9]
for i in list:
    print(i)




list = [1, 2, 3, 4, 5, 6, 7, 8]
for i in list:
    if i % 2 == 1: continue
    if i == 6: break
    print(i, "번 출력되었습니다.")

