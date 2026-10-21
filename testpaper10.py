##Question  1
# a=[1,2,3]
# a.append(4)
# print(a)#[1,2,3,4]

##Question  2
# a=[1,2,3]
# a.pop()
# print(a)#[1,2]

##Question  3
# a = [1, 2, 3]
# a.extend([4, 5])
# print(a)#[1,2,3,4,5]

##Question  4
# a = [1, 2, 3]
# print(a * 2)#[1, 2, 3, 1, 2, 3]

##Question  5
# a = [1, 2, 3]
# print(a[:2])#[1,2]

##Question  6
# a = [1, 2, 3]
# print(a[::-2])#[3,1]

##Question  7
# a = [1,2,3]
# print(a * 0)#[]

##Question  8
# a = [1,2,3]
# print(a.index(3))#2

##Question  9
# a = [1,2,3]
# print(a[::-1][1])#2

##Question  10
# a = [1, 2, 3]
# print(a + None)#TypeError

##Question  11
# a = [1, 2, 3]
# b = a
# a += [4]
# print(b)#[1, 2, 3, 4]

##Question  12
# a = [1, 2, 3]
# b = a[:]
# a[0] = 100
# print(b)#[1,2,3]
# print(a)#[100,2,3]

##Question  13
# a = [[0]*3]*3
# a[0][0] = 1
# print(a)#[[1, 0, 0], [1, 0, 0], [1, 0,0]]

##Question  14
# a = [1, 2, 3]
# print(a[1:100])#[2,3]

##Question  15
# a = [1, 2, 3]
# print(a[100:200])#[]

##Question  16
# t = (1, 2, (3, 4))
# print(t[2][0])#3

##Question  17
# t = (1, 2, 3)
# t[0] = 100
# print(t)#type error

##Question  18
# t = (1, 2, 3)
# t[0] = 100#type error

##Question  19
# a = [1,2,3]
# print(list(enumerate(a)))#[(0, 1), (1, 2), (2, 3)]

##Question  20
# a = [1,2]
# a += [3,4]
# print(a)#[1, 2, 3, 4]

##Question  21
# t = (1)
# print(type(t))#<class 'int'>

##Question  22
# t = ()
# print(len(t))#0

##Question  23
# t = ('Python')
# print(type(t))#str

##Question  24
# t = (1, [2, 3], 4)
# t[1] = [5, 6]#type error

##Question  25
# s = {1,2,3}
# s.add([4,5])
# print(s)#Type error

##Question  26
# s = {1,2,3}
# print(s.pop())#1

##Question  27
# s = {1,2,3}
# s.remove(5)#key error

##Question  28
# a = {}
# print(type(a))#dict

##Question  29
# a = {1,2}
# b = {2,3}
# print(a ^ b)#{1, 3}

##Question  30
# s = {1,2,3}
# print(s == {3,2,1})#True

##Question  31
# s = frozenset([1,2,3])
# s.add(4)#AttributeError: 'frozenset' object has no attribute 'add'

##Question  32
# d = {"a":10}
# print(d.get("b"))#None

##Question  33
# d = {"a":1}
# d.pop("b",0)
# print(d)#{'a': 1}

##Question  34
# d={1:"A",True:"B"}
# print(d)#{1: 'B'}

##Question  35
# d=dict.fromkeys("ABC",0)
# print(d)#{'A': 0, 'B': 0, 'C': 0}

##Question  36
# d={"a":1}
# x=d.copy()
# x["a"]=100
# print(d["a"])#1

##Question  37
# a = [1, 2]
# a.extend("34")
# print(a)#[1, 2, '3', '4']

##Question  38
# a = [1, 2, 3]
# a.remove(5)#ValueError: list.remove(x): xnot in list

##Question  39
# a = [10, 20, 30, 40]
# x = a.pop()
# print(x, a)#40 [10, 20, 30]

##Question  40
# a = [10, 20, 30, 40]
# print(a.pop(-2))#30

##Question  41
# a = [3, 1, 4, 2]
# x = a.sort()
# print(a, x)#[1, 2, 3, 4] None

##Question  42
# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(a, b)#[1, 2, 3] [1, 2, 3, 4]

##Question  43
# a = [1, 2, 3]
# b = a
# a.clear()
# print(b)#[]

##Question  44
# a = [1, 2]
# a.append([3, 4])
# print(len(a))#3

##Question  45
# a = [1, 2]
# a.extend([3, 4])
# print(len(a))#4

##Question  46
# a = [1, 2, 3]
# a.insert(-1, 99)
# print(a)#[1, 2, 99, 3]

##Question  47
# a = [1, 2, 3]
# print(a.pop(5))#IndexError

##Question  48
# a = ["cat", "elephant", "dog", "ant"]
# a.sort(key=len, reverse=True)
# print(a)#['elephant', 'cat', 'dog', 'ant']

##Question  49
# a = [1, 2, 3]
# print(a.reverse())#None

##Question  50
# a = [10, 20, 30, 20, 40]
# print(a.index(20, 2, 4))#3
