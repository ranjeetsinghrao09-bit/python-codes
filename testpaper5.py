##1
# print("2.")
# for i in range(6,0,-1):
#        print("*"*i)

##2
# print("4.")
# for i in range(1,6):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(5-i+1):
#         print("*",end=" ")
#     print()

##3
# print("6.")
# for i in range(1,6):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(1,2*(5-i+1)):
#         print("*",end=" ")
#     print()

##4
# print("8.")
# for i in range(6):
#     print(i*"*")
# for j in range(4,0,-1):
#         print(j*"*")

##5
# print("13.")
# n = 5
# for i in range(1, n + 1):
#     row = ""
#     for j in range(1, 10):
#         if i == 1 or j == i or j == 10 - i:
#             row += "*"
#         else:
#             row += " "
#     print(row)

##6
# print("14.")
# for i in range(9):
#     row=""
#     for j in range(9):
#         if j==0 or i==4 or i<4 and j==2*i or i>4 and j==(8-i)*2:
#             row+="*"
#         else:
#             row+=" "
#     print(row)



##7
# for i in range(11):
#        row=""
#        for j in range(11):
#              if j==5-i or j==5+i or j==i-5 or j==15-i:
#                     row+="*"
#              else:
#                      row+=" "
#        print(row)

#8
# for i in range(10):
#     row=""
#     for j in range(1,10):
#         if j==i or j==10-i :
#             row+="*"
#         else:
#             row+=" "
#     print(row)

##9
# for i in range(1,12):
#     row=""
#     for j in range(1,12):
#         if i in [1,11] or j in [1,11] or j==i or j==12-i:
#             row+="*"
#         else:
#             row+=" "
#     print(row)

##10
# for i in range(1,6):
#      for j in range(1,i+1):
#            print(j,end=" ")
#      print()

##11
# for i in range(1,6):
#      print(str(i)*i)

##12
# n = 5
# for i in range(1, n + 1):
#     row = ""
#     for j in range(i, 0, -1):
#         row += str(j)
#     print(row)

##13
##14
##15
# n = 4
# for i in range(1, n + 1):
#     row = ""
#     for j in range(1, 2 * i):
#         if j % 2 == 1:
#             row += "1"
#         else:
#             row += "0"
#     print(row)

##16
# print("A")
# print("BC")
# print("DEF")
# print("GHIJ")
# print("KLMNO")

##17
# print("A")
# print("BA")
# print("CBA")
# print("DCBA")
# print("EDCBA")

##18
# print("ABCDE")
# print("BCDE")
# print("CDE")
# print("DE")
# print("E")

##19
# print("ABCDCBA")
# print("ABCBA")
# print("ABA")
# print("A")

##20
print("*"*19)