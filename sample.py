1
f = "x= %0.5f, y= %5.2f" % (1.234567, 9.87654321)
2
print(f)
3
print()
4
print("=" * 100)
5

6
i = 123
7
f = 1.14159
8
s = 'python'
9
s1 = "python-1"
10
print("i=%d, f=%f, s=%s, s1=%s1" % (i, f, s, s1))
11

12
print()
13
print("=" * 100)
14

15  # dictionary
16
p = {'name': 'HanSaLam', 'age': 28}
17
print("name=%(name)s age=%(age)d" % p)
18

19
print()
20
print("=" * 100)
21

22
print("i={0} f={1} s={2} s1={3}".format(123, 1.14159, 12345, 'python', 'python-1'))
23

24
print()
25

26  # int, float, bool, None: 파이썬의 자료형
27
x = 100
28
y = 200
29
print(x + y)
30

31
x = "100"
32
y = "200"
33
print(x + y)
34

35
print(int(7.5))
36

37
print(2e5)
38

39
print(float("1.6"))
40

41

42

43
print(bool(0))
44

45
print(bool(-1))
46

47
print(bool("false"))
48

49
a = None
50
print(a is None)
51

52
print(0b1010)
53

54
print(type(123))
55

56
print(7 / 4)
57

58
print(7 // 4)
59

60
