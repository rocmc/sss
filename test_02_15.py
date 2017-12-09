#coding: euc-kr

count = 1
total = 0

while count <= 100:
    total = total + count
    count = count + 1
    if count % 2 == 1:
        print(count)

print("1~100까지의 합은:", total)

