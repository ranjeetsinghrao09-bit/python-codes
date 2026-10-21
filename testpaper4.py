'''  PYTHON FUNCTIONS AND LOOPS TEST ---4'''
#Question 3
# sum=0
# for i in range(1,5): #isme 5 include nahi hoga isa liye answer 10 aaya hai
#     sum+=i
# print(sum)

#question 4
# for i in range(3):
#     print(i) #yaha par continue kisi bhi codition ke sath nahi hai balki ye agli condition ke liye likha hua hai
#     continue
#     print("hello")
# #/ how many times will "hello" print?

# for i in range(3):#aisi coditions mein zero bhi include hota hai
#     for j in range(3):
#         if j==1:
#             continue
#         print(i,j)

#Question 5
# for i in range(1,5):
#     for j in range(i): #yaar meine dhyan kyu nahi diya yaha par bhi i include nahi hoga isa liye answer 10 aaya hai
#         print("*",end="")
#     print()
# #/ How many times will "*" print?

#Question 7
# for i in range(2,8,2):
#     print(i,end=" ") #yaha 2 include hua hai

#Question 8
# i=5
# while i>2:
#    print(i,end=" ")
#    i-=1 #5 4 3

#Question 16
# for i in range(1,10,3):
#     print(i,end=" ") #1 4 7 #aakhir maine dhyan kyu nahi diya waha 3 step diya tha meine 2 step wale number likha diye

#Question 18
# for ch in "ABC":
#      print(ch.lower(),end=" ") #a b c#😭 aakhir itni chhoti chhoti mistake meine aaram se 86 tak pahuch jaata but sirf ak space ki mistake ho gayi

#Question 22
# def fun(n):
#     if n==0:
#         return 0
#     return n+fun(n-1) unwiding wale abhi dekhna baaki hai
# print(fun(4))

#question 25
# def fun(a):
#     if a > 5:
#         return a
#     return fun(a + 2) isa concept ko samajhna baaki hai
# print(fun(1))

#Question 26
# def fun(x):
#     return x+1
# def show():
#     return fun(5)
# print(show())

#Question 27
# def fun(a,b):
#     return a and b
# print(fun(5,0)) #yaha and actual value hi return karta hai isi liye false naa aakar 0 aaya

#Question 28
def fun(x):
    if x<=1:
        return x
    return fun(x-1)+fun(x-2)
print(fun(5)) ###################

#Question 30:
# def fun(x):
#     if x==0:
#         return 0
#     return x+fun(x//2)
# print(fun(10)) # 10+5+2+1+0=18 kyuki 10//2=5, 5//2=2, 2//2=1, 1//2=0, 0//2=0
