##Question 1
# print("hello world".title().swapcase()) #hELLO wORLD

##Question 2
# print("abc123".isalnum() and "abc".isalpha())#True

##Question 3
# print("Hello World".istitle())#True

##Question 4
# print("HELLO".lower().isupper())#False

##Question 5
# print("ABC123".isupper())#True

##Question 6
# print("abc".zfill(5))#00abc

##Question 7
# print("abc"*2)#abcabc

##Question 8
# print(",".join(["a","b","c"]))#a,b,c

##Question 9
# print("abc".index("d"))#value Error

##Question 10
# print("Hello".islower())#False

##Question 11
# print("10">"2")#False

##Question 12
# print("HELLO".lower().count("l"))#2

##Question 13
# print("python".capitalize().startswith("p"))#False

##Question 14
# print("python".lower().replace("p","P"))#Python

##Question 15
# print("hello".find("l"))#2

##Question 16
# print("abc".ljust(5,"-"))#abc--

##Question 17
# print("abc".replace("a","").upper())#BC

##Question 18
# print("abc".islower() and "ABC".isupper())#True

##Question 19
# a=[1,2,3]
# print(a*2)#[1, 2, 3, 1, 2, 3]

##Question 20
# a=[1,2,3]
# b=a[:] #yaha list sirf copy ho rahi hai, reference nahi ho rahi hai
# b.append(4)
# print(a)#[1, 2, 3]

##Question 21
# a = [1, 2, 3]
# b = a.copy()
# b[0] = 99
# print(a)#[1,2,3]

##Question 22
# a = [1, 2, 3]
# print(a[10])#IndexError: list index out of range

##Question 23
# a = [1, 2, 3]
# b = a
# a = a + [4]#yaha ak new list create ho gyi hai but b abhi bhi pahle wale a list ko hi refer kar rha hai
# print(b)#[1, 2, 3]

##Question 24
# a = [1, 2, 3]
# b = a
# b = None
# print(a)#[1, 2, 3]

##Question 25
# a = [1, 2, 3]
# b = a
# a += [4]
# print(b)#[1, 2, 3, 4] yaha par koi bhi new list nahi ban rhi hai balki a ke andar hi changes kiye gye hai jiski wajah se b ke andar bhu changes huye hai

##Question 26
# a = [1, 2, 3]
# b = a[:]
# a[0] = 100
# print(b)#[1, 2, 3]#b sirf a wali list ki copy hai agar ab a ke andar changes kiye jaate hai toh isse b ke andar koi change nahi hoga

##Question 27
# a = [1, 2, 3]
# print(a[100:200])#[]

##Question 28
# t = (1, 2, (3, 4))
# print(t[2][0])#3

##Question 29
# t = (1, 2, 3)
# t[0] = 100
# print(t)#error

##Question 30
# t = (1, 2, 3)
# t = list(t)
# t.append(4)
# print(tuple(t))#(1,2,3,4)

##Question 31
# t = (1,2,3)
# del t
# print(t)#NameError: name 't' is not defined

##Question 32
# a = [1,2,3]
# b = [4,5,6]
# print(list(zip(a,b)))#[(1, 4), (2, 5), (3, 6)]

##Question 33
# t = (1)
# print(type(t))#<class 'int'>

##Question 34
# t = ('Python')
# print(type(t))#str

##Question 35
# t = (1, 2, 3)
# print(t * 0)#0

##Question 36
# s = {1,2,3}
# s.remove(5)#Error

##Question 37
# s = "apple,banana,mango,grapes"
# print(s.rsplit(",", 2))#['apple,banana', 'mango', 'grapes']

##Question 38
# s = "mississippi"
# print(s.count("issi"))#1

##Question 39
# s = "Python3"
# print(s.isalpha(), s.isalnum())#False True

##Question 40
# s = "Python\nJava\nC++"
# print(s.splitlines()) #['Python', 'Java', 'C++']

##Question 41
# s = "report.pdf"
# print(s.removesuffix(".txt"))#report.pdf

##Question 42
# s = "Straße"
# print(s.casefold())#strasse

##Question 43
# s = "abcabcabc"
# print(s.find("abc", 1, 6))#3

##Question 44
# a = [1, 2, 3]
# a.remove(5)#Value error

##Question 45
# a = [1, 2, 3, 4]
# a.reverse()
# print(a)#[4, 3, 2, 1]

##Question 46
# a = [[1, 2], [3, 4]]
# b = a.copy()
# b[0].append(5)
# print(a)#[[1, 2, 5], [3, 4]]

##Question 47
# a = [1, 2]
# a.append([3, 4])
# print(len(a))#3
# print(a)

##Question 48
# a = [1, 2]
# a.extend([3, 4])
# print(len(a))#4 yaha sirf andar ki value add huyi hai naa ki puri list

##Question 49
# a = ["10", "2", "30", "4"]
# a.sort()
# print(a)#['10', '2', '30', '4']

##Question 50
# a = [10, 20, 30, 20, 40]
# print(a.index(20, 2, 4))#3