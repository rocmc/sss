num = [1, 2, 3, 4]  # 리스트선언
num.append(5); # 리스트 뒤에 추가
print(num)
num.insert(0, 0)  # 리스트 사이에 삽입 (몇번째 인덱스, 어떤값)
print(num)
num.extend([6, 7]) # 기존의 리스트에 extend(내용을 추가)
print(num)

color = ['red', 'blue', 'yellow', 'red']
print(color.index('red')) # red는 몇번째 인덱스에 있을까요  = 0
print(color.index('red', 1)) # 시작점을주면 시작점을 기점으로 찾습니다 = 3
print(color.count('red')) # red가 몇개 존재하나요 = 2
print(color.pop()) # 리스트 맨뒤의 값을 뻅니다. = red

color.sort() # 오름차순 정렬 ['blue', 'red', 'yellow']
print(color)
color.remove('blue') # 해당값 제거 ['red', 'yellow']
print(color)

