#Question 1
# for i in range(1,6):
#     print("*"*i)

#Question 2
# for i in range(6,0,-1):
#     print("*"*i)

#question 3
# for i in range(1,6):
#     for j in range(1,6-i+1):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()
        
#Question 4
# for i in range(1,6):
#     for j in range(1,6):
#         if i in [1,5] or j in [1,5]:  
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#Question 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#Question 6
# n=1
# for i in range(1,7):
#     for j in range(i):
#         print(n,end=" ")
#         n+=1
#     print()

#Question 7
# for i in range(1,6):
#     row=""
#     for j in range(1,10):
#         if i==5 or j==5-i+1 or j==5+i-1:
#             row+="*"
#         else:
#             row+=" "
#     print(row)
# for i in range(4,0,-1):
#     row=""
#     for j in range(1,10):
#         if j==5-i+1 or j==5+i-1:
#             row+="*"
#         else:
#             row+=" "
#     print(row)



#Question 8
# for i in range(1,6):
#     for j in range(1,10):
#         if j==5-i+1 or j==5+i-1:
#             print(i,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(4,0,-1):
#     for j in range(1,10):
#         if j==5-i+1 or j==5+i-1:
#             print(i,end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#Question 9
# for i in range(1,6):
#     for j in range(1,6):
#         if i in [1,5] or j==5 or i==3 and j<=3 or i==4 and j in [1,3]:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#Question 10
# for i in range(1,6):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for k in range(1,2*(5-i+1)):
#         print("*",end=" ")
#     print()
# for i in range(2,6):
#     for j in range(1,5-i+1):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()

#Question 11
# for i in range(3):
#     for j in range(14):
#         if i==0 and j in [3,7,11]:
#             print("*",end=" ")
#         elif i==1 and j  in [2,4,6,8,10,12]:
#             print("*",end=" ")
#         elif i==2 and j in [1,5,9,13]:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# #Question 12
# for i in range(1,6):
#     print(" "*(5-i),end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#SECOND METHOD
# for i in range(1,6):
#     for j in range(1,5-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()

#Question 13
# for i in range(5):
#     if i%2==0:
#         print("* * *")
#     else:
#         print(" * *")

#Question 14
# n=1
# for i in range(1,5):
#     for j in range(i):
#         print(n,end=" ")
#         if j<i-1:
#            print("*",end=" ")
#            n+=1
#     print()

#Question 15
# for n in range(4,0,-1):              # decreasing: 4,3,2,1
#     count = 1
#     for k in range(2*n-1):
#         if count % 2 != 0:            # odd position → number
#             print(n, end="")
#         else:                          # even position → star
#             print("*", end="")
#         count = count + 1
#     print()

# for n in range(1,5):                   # increasing: 1,2,3,4
#     count = 1
#     for k in range(2*n-1):
#         if count % 2 != 0:
#             print(n, end="")
#         else:
#             print("*", end="")
#         count = count + 1
#     print()