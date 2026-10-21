#Question 1
# n=2
# even_list=[]
# odd_list=[]
# for i in range(n):
#     num=int(input("enter a number"))
#     if num%2==0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)
# print("Even numbers:",even_list)
# print("Odd numbers:",odd_list)

#Question 2
# nums = list(map(int, input("Numbers likho (space se alag): ").split()))
# largest = nums[0]
# smallest = nums[0]
# for n in nums:
#     if n > largest:
#         largest = n
#     if n < smallest:
#         smallest = n
# print("Largest:", largest)
# print("Smallest:", smallest)

#Question 3
# num = int(input("Number likho: "))
# original = num
# reverse = 0
# while num > 0:
#     digit = num % 10            # last digit nikalo
#     reverse = reverse * 10 + digit
#     num = num // 10             # last digit hata do
# if original == reverse:
#     print("Palindrome hai")
# else:
#     print("Palindrome nahi hai")

#Question 4
# num = int(input("Number likho: "))
# while num > 9:                  # jab tak single digit na ho
#     total = 0
#     while num > 0:
#         total += num % 10       # last digit add karo
#         num //= 10              # last digit hata do
#     num = total                 # sum ko naya number bana lo
# print("Single digit:", num)


#Question 5
#s = input("String likho: ")
#for i in range(len(s)):
#     print(s[i:])



#Question 6
# nums = list(map(int, input("Numbers likho (space se alag): ").split()))
# n = len(nums) + 1               # ek number missing hai, isliye +1
# expected_sum = n * (n + 1) // 2
# actual_sum = sum(nums)
# print("Missing number:", expected_sum - actual_sum)

#Question 7
# nums = list(map(int, input("Numbers likho (space se alag): ").split()))
# pos = neg = zero = 0
# for n in nums:
#     if n > 0:
#         pos += 1
#     elif n < 0:
#         neg += 1
#     else:
#         zero += 1
# print("Positive:", pos)
# print("Negative:", neg)
# print("Zero:", zero)

#Question 8
# n = int(input("N likho: "))
# for i in range(1, 77 * n + 1):
#     if i % 7 == 0 and i % 11 == 0:
#         print(i)

#question 9
#n = int(input("N likho: "))
#for num in range(1, n + 1):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:        # i, num ka factor hai
#             count += 1
#     if count == 3:
#         print(num)

#Question 10
# def trailing_zeros(n):
#     count = 0
#     i = 5
#     while n // i > 0:
#         count += n // i
#         i *= 5
#     return count
# limit = int(input("Limit likho: "))
# for n in range(1, limit + 1):
#     if trailing_zeros(n) == 2:
#         print(n)

#Question 11
# def trailing_zeros(n):
#     count = 0
#     i = 5
#     while n // i > 0:
#         count += n // i
#         i *= 5
#     return count
# limit = int(input("Limit likho: "))
# for n in range(1, limit + 1):
#     if trailing_zeros(n) == 2:
#         print(n)

#Question 12
# name = "apple"
# for i in "aeiou":
#     if i in name:
#         print(i, end=" ")
# print()

#Question 13
# print(3.)
# for i in range(1,6):
#    for j in range(1,5-i+1):
#        print(" ",end=" ")
#    for k in range(i):
#       print("*",end=" ")
#    print()

#Question 14
# print(6.)
# for i in range(1,6):
#     for j in range(1,i):
#           print(" ",end=" ")
#     for k in range(1,2*(5-i+1)):
#           print("*",end=" ")
#     print()

#Question 15
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i == 5 or j == 1 or (j == 2*i - 1 and i < 5) or (j == 19 - 2*i and i > 5):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#question 16
# for i in range(1, 6):
#     for j in range(i):                  # left wing ke stars
#         print("*", end="")
#     for k in range(2 * (5 - i)):        # beech ke spaces
#         print(" ", end="")
#     for l in range(i):                  # right wing ke stars
#         print("*", end="")
#     print()
# for a in range(5 - 1, 0, -1):
#     for b in range(a):                  # left wing ke stars
#         print("*", end="")
#     for c in range(2 * (5 - a)):        # beech ke spaces
#         print(" ", end="")
#     for d in range(a):                  # right wing ke stars
#         print("*", end="")
#     print()

#Question 17
# n = 7
# for i in range(1, n + 1):
#     for j in range(n + 2 - i):          # shuru ke spaces
#         print(" ", end="")
#     for k in range(2 * i - 1):          # is row ki width = 2i - 1
#         if k == 0 or k == 2 * i - 2 or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#Question 18
# for i in range(1,10):
#      for j in range(1,10):
#           if j==i or j==9-i+1:
#               print("*",end=" ")
#           else:
#              print(" ",end=" ")
#      print()

#Question 19
# for i in range(1,6):
#    for j in range(i):
#       print(i, end="")
#    print()

##Question 20
# for i in range(1, 5):
#     for j in range(4 - i):              # shuru ke spaces
#         print(" ", end="")
#     for k in range(1, i + 1):           # badhte numbers: 1 se i tak
#         print(k, end="")
#     for l in range(i - 1, 0, -1):       # ghatte numbers: i-1 se 1 tak
#         print(l, end="")
#     print()