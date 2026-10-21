##Question 1
# print("PyThOn123".swapcase().lower()) #python123

##Question 2
# print("hello world".title().swapcase()) #hELLO wORLD

##Question 3
# print("ABC".isupper() and "abc".islower()) #True

##Question 4
# print("Hello World".istitle()) #True

##Question 5
# print("Hello world".istitle()) #False

##Question 6
# print("python".find("th")+"python".count("p"))#3

##Question 7
# print("banana".count("an")*"banana".find("na")) #4

##Question 8
# print("hello".upper().islower()) #False

##Question 9
# print(" ".isspace() and "A".isalpha()) #True

##Question 10
# print("mississippi".count("iss"))#2

##Question 11
# print("Hello123".isalnum() and not "Hello 123".isalnum()) #True

##Question 12
# print(" hello ".strip().upper()) #HELLO

##Question 13
# print("abcabc".find("abc", 1)) #3

##Question 14
# print("Hello".startswith("He") and "World".endswith("ld")) #True

##Question 15
# print("abc".zfill(5))#00abc

##Question 16
# print("hello".upper()) #HELLO

##Question 17
# print("Python"[::2])#pto

##Question 18
# print(" hi ".strip())#hi

##Question 19
# print(",".join(["a","b","c"]))#a,b,c

##Question 20
# print("abc".index("d"))#Value Error

##Question 21
# print("hello".count("l"))#2

##Question 22
# print("10" > "2")#False

##Question 23
# print(len(" "))#1

##Question 24
# print("HELLO".lower())#hello

##Question 25
# print(type("5"+"5"))#str

##Question 26
# print("abc".isalpha())#True

##Question 27
# print("123".isdigit()) #True

##Question 28
# print(" hello ".strip().upper())#HELLO

##Question 29
# print("abc".upper().lower())#abc

##Question 30
# print(" hello ".strip().replace("h","H"))#Hello

##Question 31
# print("abc".replace("a","A").islower()) #False

##Question 32
# print("  data  ".strip().capitalize()) #Data

##Question 33
# print("hello".startswith("he") and "hello".endswith("lo"))#True

##Question 34
# print("abc123".isalnum())#True

##Question 35
# print("123".zfill(5))#00123

##Question 36
# print("hello world".title())#Hello World

##Question 37
# print("abc".replace("a","").upper()) #BC

##Question 38
# print("123abc".isalpha())#False

##Question 39
# print("a,b,c".split(","))#['a', 'b', 'c']

##Question 40
# print("-".join(["x","y","z"]).upper())#X-Y-Z

##Question 41
# print("  PYTHON  ".strip().lower().startswith("p"))#True

##Question 42
# a = [1, 2, 3]
# a.pop()
# print(a)#[1,2]

##Question 43
# a = [1, 2, 3]
# a.append([4, 5])
# print(a)#[1, 2, 3, [4, 5]]

##Question 44
# a = [1, 2, 3]
# print(a * 2)#[1, 2, 3, 1, 2, 3]

##Question 45
# a = [1, 2, 3]
# print(a[:2])#[1,2]

##Question 46
# a = [1, 2, 3]
# print(a[::-2])#[3,1]

##Question 47
# a = [1, 2, 3]
# b = a.copy()
# b[0] = 99
# print(a)#[1,2,3]

##Question 48
# a = [1,2,3]
# print(a.index(3))#2

##Question 49pahle reverse karna aur phir [1] par jo element hai ushe find karna
# a = [1,2,3]
# print(a[::-1][1])#2

##Question 50
# a = [1, 2, 3]
# b = a
# b = None
# print(a)#[1,2,3]

##Question 51
# a = [[0]*3]*3
# a[0][0] = 1
# print(a)#[[1, 0, 0], [1, 0, 0], [1, 0, 0]]

##Question 52
# t = (1, 2, 3)
# t[0] = 100
# print(t)#type error

##Question 53
# t = (1, 2, 3)
# print(len(t))#3

##Question 54
# t = (10,)
# print(type(t))#tuple

##Question 55
# a = [1, 2, 3]
# b = a
# a = [4, 5]
# print(b)#[1,2,3]

##Question 56
# a = [1,2]
# a += [3,4]
# print(a)#[1,2,3,4] are yaar yaha par sirf andar wala number add hoga

##Question 57
# t = (1)
# print(type(t))#int

##Question 58
# t = ()
# print(len(t))#1

##Question 59
# t = (1,2,3,4,5)
# print(t[::2])#(1,3,5)

##Question 60
# t = (1, 2, 3)
# print(t + (4,))#(1,2,3,4)

##Question 61
# t = (1, [2, 3], 4)
# t[1].append(5)
# print(t)#(1, [2, 3, 5], 4)

##Question 62
# t = (1, 2, 3, 4, 5)
# print(t[-4:-1])#(2,3,4)

##Question 63
# s = {1, 2, 3}
# s.add((4, 5))
# print(s)#{(4, 5), 1, 2, 3}

##Question 64
# s = {1,2}
# s.update((3,4))
# print(s)#{1, 2, 3, 4}

##Question 65
# s = {1,2,3}
# print(s.pop())#C:Removes and returns an arbitrary element yaani yaha pop kisi bhi element ko remove kar sakta hai kyuki set ke andar indexing nahi hoti

##Question 66
# s = {1,2,3}
# s.discard(5)
# print(s)#{1, 2, 3}

##Question 67
# a = {1,2}
# b = {2,3}
# print(a ^ b)#{1,3}

##Question 68
# s = "Python Programming"
# print(s.startswith("Pro", 7))#True

##Question 69
# s = "a-b-c-d"
# print(s.partition("-"))#('a', '-', 'b-c-d')

##Question 70
# s = "a-b-c-d"
# print(s.rpartition("-"))#('a-b-c', '-', 'd') yaha square bracket nahi balki rounded bracket aayenge

##Question 71
# s = "-42"
# print(s.zfill(5))#-0042

##Question 72
# s = "Python3"
# print(s.isalpha(), s.isalnum())#False True 

##Question 73
# s = "abababab"
# print(s.replace("ab", "X", 2)) #XXabab

##Question 74
# s = "Python Java Python"
# print(s.rfind("Python"))#12

##Question 75
# s = "   "
# print(s.isspace())#True

##Question 76
# s = "hello WORLD"
# print(s.swapcase())#HELLO world

##Question 77
# s = "Python\nJava\nC++"
# print(s.splitlines())#['Python', 'Java', 'C++']

##Question 78
# s = "www.example.com"
# print(s.removeprefix("www."))#example.com

##Question 79
# s = "report.pdf"
# print(s.removesuffix(".txt"))#report.pdf

##Question 80
# s = "Straße"
# print(s.casefold())#strasse

##Question 81
# s = "Python123"
# print(s.lower().endswith("123"))#True

##Question 82
# s = "abcabcabc"
# print(s.find("abc", 1, 6))#3

##Question 83
# a = [1, 2]
# a.extend("34")
# print(a)#[1, 2, '3', '4']

##Question 84
# a = [10, 20, 30]
# a.insert(10, 40)
# print(a)#[10, 20, 30, 40]

##Question 85
# a = [1, 2, 3]
# a.remove(5)#Value error aayegi yaar 

##Question 86
# a = [10, 20, 30, 40]
# x = a.pop()
# print(x, a)#40 [10, 20, 30]

##Question 87
# a = [10, 20, 30, 40]
# print(a.pop(-2))#30

##Question 88
# a = [5, 10, 5, 20, 5]
# print(a.count(5))#3

##Question 89
# a = [10, 20, 30, 20, 40]
# print(a.index(20, 2))#3

##Question 90
# a = [10, 20, 30]
# print(a.index(100))#Value error

##Question 91
# a = [3, 1, 4, 2]
# x = a.sort()
# print(a, x)#[1, 2, 3, 4] None

##Question 92
# words = ["apple", "kiwi", "banana", "fig"]
# words.sort(key=len)
# print(words)#['fig', 'kiwi', 'apple', 'banana']

##Question 93
# a = [5, 1, 4, 2]
# a.sort(reverse=True)
# print(a)#[5, 4, 2, 1]

##Question 94
# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(a, b)#[1, 2, 3] [1, 2, 3,4]

##Question 95
# a = [[1, 2], [3, 4]]
# b = a.copy()
# b[0].append(5)
# print(a)#[[1, 2, 5], [3, 4]]

##Question 96
# a = [1, 2, 3]
# a.insert(-1, 99)
# print(a)#[1, 2, 99, 3]

##Question 97
# a = ["10", "2", "30", "4"]
# a.sort()
# print(a)#['10', '2', '30', '4']

##Question 98
# a = [10, 20, 30]
# a.insert(-10, 5)
# print(a)#[5, 10, 20, 30]

##Question 99
# a = [1, 2]
# a.extend({"x": 10, "y": 20})
# print(a)#[1, 2, 'x', 'y']

##Question 100
# a = [10, 20, 30, 20, 40]
# print(a.index(20, 2, 4))#3