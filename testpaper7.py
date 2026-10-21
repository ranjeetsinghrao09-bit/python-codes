##Q1:
# print("PyThOn123".swapcase().lower()) #python123  encode

##Q2:
# print("hello world".title().swapcase()) #hELLO wORLD

##Q3:
# print("abc123".isalnum() and "abc".isalpha()) #True

##Q4:
# print("ABC".isupper() and "abc".islower()) #True

##Q5:# print("Hello World".istitle()) #True

##Q6:
# print("Hello world".istitle()) #False

##Q7:
# print("python".find("th") + "python".count("p")) #3 
# yaha find yaani ki th in index hai jo ki 2 par hai aur p 1 hai toh total 3 ho gye na

##Q8:
# print("banana".count("an") * "banana".find("na"))
#yaha an 2 baar hai aur find na index 2 par hai toh 2*2=4 ho gya

##Q9:
# print("HELLO".lower().isupper()) #False

##Q10:
# print("hello".upper().islower()) #False


##Q11:
# print("123abc".isalpha() or "123".isdigit()) #True

##Q12:
# print("   ".isspace() and "A".isalpha()) #True

##Q13:
# print("hello".find("l", 3)) #3


##Q14:
# print("hello".rfind("l")) #3

##Q15:
# print("mississippi".count("iss")) #2

##Q16:
# print("Hello123".isalnum() and not "Hello 123".isalnum()) #True

##Q17:
# print("abc".center(7,"*"))#**abc**

##Q18:
# print(" hello ".strip().upper())#HELLO

##Q19:
# print("python".replace("p","P").islower())#False

##Q20:
# print("abcabc".find("abc",1))#3

##Q21:
# print("ABC123".isupper())#True

##Q22:
# print("Hello".startswith("He") and "World".endswith("id")) #False

##Q23:
# print("Hello".startswith("he"))#False

##Q24:
# print("abc".zfill(5))##00abc

##Q25:
# print("hello".upper())#HELLO

##Q26:
# print("python"[::2])#pto aakhir yaar kyu mai inko bhul gya yaha 0 se string suru ho rhi hai yaani p se har 2 number wala letter aa rha hai isi liye pto aaya

##Q27:
# print("abc"*2) #abcabc

##Q28:
# print(" he ".strip())#he yaha 2 option same the aur space dikh bhi nahi rha tha toh mujhe kaise pta chale ki kisme space hai aur kisme nahi


##Q29:
# print("abc".find("d")) #-1

##Q30:
# print(",".join(["a","b","c"])) #a,b,c

##Q31:
# print("abc".index("d")) #value Error

##Q32:
# print("hello".count("l")) #2

##Q33:
# print("Hello".islower()) #False

##Q34:
# print(bool(""))#False

##Q35:
# print("abc">"abd") #False — kyunki 3rd character pe 'c' < 'd' hai (ASCII 99 < 100), toh "abc" < "abd" hota hai, > nahi.

##Q36:
# print("10">"2") #False
# print("10"<"2") #True — kyunki '1' < '2' ASCII-wise (49 < 50), first character pe hi decision ho gaya.

##Q37:
# print(len(" ")) # length zero se nahi 1 se suru hoti hai

##Q38:
# print("abc".capitalize()) #Abc

##Q39:
# print("HELLO".lower())#hello

##Q40:
# print("abc".startswith("a")) #True

##Q41:
# print("abc".endswith("c")) #True

##Q42:
# print("a"*0) # kuchh bhi output nahi aayega empty aayega sab

##Q43:
# print(type("5"+"5"))#<class 'str'>

##Q44:
# print("abc".isalpha()) #True

##Q45:
# print("123".isdigit()) #True

##Q46:
# print(" hello ".strip().upper()) #HELLO YAHA DONO OPTION SAME THE SPACE KAHA HAI AUR KAHA NAHI YE KAISE PTA CHALE ISA LIYE YE GLATA HO GYA

##Q47:
# print("python".replace("p","P").capitalize()) #Python

##Q48:
# print("abc".upper().lower())#abc

##Q49:
# print(" hello ".strip().replace("h","H")) #Hello

##Q50:
# print(",".join("abc".upper())) #A,B,C

##Q51:
# print("HELLO".lower().count("l"))#2

##Q52:
# print("python".capitalize().startswith("P")) #True

##Q53:
# print("  hi  ".strip().upper().endswith("I"))#True

##Q54:
# print("abcabc".replace("a","A").count("A"))#2

##Q55:
# print("python".lower().replace("p","P"))#Python

##Q56:
# print(" data ".strip().capitalize())#Data

##Q57:
# print("hello".startswith("he")and "hello".endswith("lo"))#True

##Q58:
# print("abc".replace("a","A").islower())#False

##Q59:
# print("123".zfill(5)) #00123 zfill means aage ki traf zeros lagane hai

##Q60:
# print("hello".find("l")) #3

##Q61:
# print("abc123".isalnum())#True

##Q62:
# print("HELLO".isupper())#True

##Q63:
# print("abc".ljust(5,"-")) #abc--

##Q64:
# print("abc".rjust(5,"-")) #rjust matlab content ko right pe le jao, isliye padding left mein aati hai → --abc

##Q65:
# print("Python".swapcase()) #pYTHON

##Q66:
# print("hello world".title()) #Hello World

##Q67:
# print("abc".encode()) #b"abc"

##Q68:
# print("abc".replace("a","").upper()) #BC

##Q69:
# print("123abc".isalpha())#False

##Q70:
# print("abc".islower() and "ABC".isupper()) #upper

##Q71:
# print("abc".partition("b")) #('a', 'b', 'c')

##Q72:
# print("-".join(["x","y","z"]).upper()) #X-Y-Z

##Q73:
# print(" PYTHON ".strip().lower().startswith("p")) #True

##Q74:
# a=[1,2,3]
# a.append(4)
# print(a) #[1,2,3,4]

##Q75:
# a=[1,2,3]
# a.pop()
# print(a)#[1,2] aakhir yaar mujhe pta hai ki pop last digit yaa string ko remove karta hai phir bhi galat kar diya anwser

##Q76:
# a=[1,2,3]
# a.extend([4,5])
# print(a) #[1,2,3,4,5]

##Q77:
# a = [1, 2, 3]
# a.append([4, 5])
# print(a) #[1, 2, 3, [4, 5]]

##Q78:
# a = [1, 2, 3]
# print(a * 2) #[1, 2, 3, 1, 2, 3] ye bhi galat hua tha

##Q79:
# a = [1, 2, 3]
# print(a[:2]) #[1, 2]

##Q80:
# a = [1, 2, 3]
# b = a[:]
# b.append(4)
# print(a) #[1, 2,3]

##Q81:
# a = [1, 2, 3]
# print(a[::-2]) #[3,1]

##Q82:
# a = [1, 2, 3]
# b = a.copy()
# b[0] = 99
# print(a) #[1, 2, 3]

##Q83:
# a = [1, 2, 3]
# b = a[:] # iska matlab copy banana hi hota hai 
# b[1] = 99
# print(a) #[1, 2, 3]

##Q84:
# a = [1,2,3]
# print(a * 0) #0

##Q85:
# a = [1,2,3]
# print(a.index(3)) #2

##Q86:
# a = [1,2,3]
# print(a[::-1][1]) #2 yaani -1 se puri list reverse hogi aur phir batana hai ki 1 par consa element hai

##Q87:
# a = [1, 2, 3]
# print(a[10]) #Index error

##Q88:
# a = [1, 2, 3]
# b = a
# a = a + [4] jab [4] add kiya gya toh a ki ak new list bna gyi isi liye b mai 4 add nahi hua
# print(b) #[1, 2, 3]

##Q89:
# a = [1, 2, 3]
# print(a + None) #Type Error

##Q90:
# a = [1, 2, 3]
# b = a
# b = None
# print(a) #[1,2,3]

##Q91:
# a = [1, 2, 3]
# b = a
# a += [4]
# print(b) #[1,2,3,4]

##Q92:
# a = [[0]*3]*3
# a[0][0] = 1 #iska matlab hai ki "a" ke andar box first[0] ke first[0] element ko 1 kar diya isi liye har box ka first element 1 aaya hai
# print(a) #[[1, 0, 0], [1, 0, 0], [1, 0,0]]

##Q93:
# a = [1, 2, 3]
# print(a[1:100]) #[2, 3] yaha 1 index se suru hua hai aur 100 tak gya hai but jitna list mai tha utna hi print hua hai

##Q94:
# a = [1, 2, 3]
# print(a[100:200]) #[] empty list isa liye aayi hai kyuki yaha range 100 se start ho rhi hai naa ki 0 se 

###Q95:
# a = [1, 2, 3]
# print(a[3]) #index error

##Q96:
# a = [1,2,3]
# print(list(enumerate(a))) #[(0, 1), (1, 2), (2, 3)] enumerate() list (ya kisi bhi iterable) ke har element ke saath uska index bhi attach kar deta hai — pairs bana deta hai (index, value).

##Q97:
# a = [1, 2, 3]
# b = a
# a = [4, 5]
# print(b) #[1, 2, 3]

##Q98:
# a = [1,2]
# a += [3,4]
# print(a) #[1, 2, 3, 4] yaha sirf bracket ke andar ki chize add huyi hai naa ki full bracket

##Q99:
# s = "  Python  "
# print(s.strip().center(10, "*")) #**Python**

##Q100:
# s = "banana"
# print(s.find("na", 3)) #4 Index 3 se search start: banana(b0 a1 n2 a3 n4 a5) → "na" milta hai index 4 se.

##Q101:
# s = "apple,banana,mango,grapes"
# print(s.rsplit(",", 2)) #['apple,banana', 'mango', 'grapes'] isa list mai total 3 elements hai kyuki apple,banana mil kar sirf ak hi element hai

##Q102:
# s = "mississippi"
# print(s.count("issi")) # mere kitne saare question aate huye bhi galat ho gyi meine dhayan nahi diya isi liye

##Q103:
# s = "Python Programming"
# print(s.startswith("Pro", 7)) #True

##Q104:
# s = "a-b-c-d"
# print(s.partition("-")) #('a', '-', 'b-c-d') partition ki starting aage se huyi hai naa ki pichhe se

##Q105:
# s = "Python"
# print(s.zfill(10)) #0000Python zfill yaani aage se fill karna hai aur pichhe tak lekar jaana hai

##Q106:
# s = "Python3"
# print(s.isalpha(), s.isalnum()) #False True

##Q107:
# s = "Python"
# print(s.ljust(10, "-")) #Python----

##Q108:
# s = "abababab"
# print(s.replace("ab", "X", 2)) #XXababcount=2 matlab sirf pehle 2 occurrences replace honge, baaki as-is rahenge

##Q109:
# s = "Python Java Python"
# print(s.rfind("Python")) #12 yaha python 12 par hai 2 index ke baad

##Q110:
# s = "Python"
# print(s.index("z")) #Value Error

##Q111:
# s = "   "
# print(s.isspace()) #True

##Q112:
# s = "hello WORLD"
# print(s.swapcase()) #HELLO world

##Q113:
# s = "Python\nJava\nC++"
# print(s.splitlines()) #['Python', 'Java', 'C++'] splitlines ka matlab hi /n hota hai

##Q114:
# s = "www.example.com"
# print(s.removeprefix("www.")) #example.com

##Q115:
# s = "report.pdf"
# print(s.removesuffix(".txt")) #report.pdf

##Q116:
# s = "  hello  world  "
# print(s.split()) #['hello', 'world']


##Q117:
# data = ["Python", "Java", "React"]
# print("-".join(data)) #Python-Java-React

##Q118:
# s = "Straße"
# print(s.casefold()) #strasse

##Q119:
# s = "Python123"
# print(s.lower().endswith("123")) #True

##Q120:
# s = "abcabcabc"
# print(s.find("abc", 1, 6)) #3 Search sirf s[1:6] range ke andar hota hai — us range mein "abc" index 3 pe milta hai.

##Q121:
# nums = [10, 20, 30]
# x = nums.append(40)
# print(nums, x)#[10, 20, 30, 40] None

##Q122:
# a = [1, 2]
# a.extend("34") # [1,2,'3','4'] extend string ko character-by-character iterate karta hai, poora string ek unit ki tarah add nahi karta.
# print(a)

##Q123:
# a = [10, 20, 30]
# a.insert(10, 40) #[10,20,30,40] Agar insert index list ki length se bada ho, toh Python end mein hi daal deta hai (error nahi deta) insert mai 10 length thi aur 40 value.
# print(a)

##Q124:
# a = [1, 2, 3]
# a.remove(5) #value error

##Q125:
# a = [10, 20, 30, 40]
# x = a.pop()
# print(x, a)#40, [10,20,30] Bina argument ke pop() last element nikalta hai aur usse return karta hai.

##Q126:
# a = [10, 20, 30, 40]
# print(a.pop(-2)) #30

##Q127:
# a = [1, 2, 3, 2, 4]
# a.remove(2)
# print(a)#[1, 3, 2, 4]

##Q128:
# a = [5, 10, 5, 20, 5]
# print(a.count(5))#3

##Q129:
# a = [10, 20, 30, 20, 40]
# print(a.index(20, 2))#3

##Q130:
# a = [10, 20, 30]
# print(a.index(100))#Value Error Value list mein exist nahi karti, toh ValueError aata hai (IndexError sirf position ke liye hota hai, value ke liye nahi).

##Q131:
# a = [3, 1, 4, 2]
# x = a.sort()
# print(a, x)#[1, 2, 3, 4] None

##Q132:
# words = ["apple", "kiwi", "banana", "fig"]
# words.sort(key=len)
# print(words) #['fig', 'kiwi', 'apple', 'banana']

##Q133:
# a = [5, 1, 4, 2]
# a.sort(reverse=True)
# print(a) #[5, 4, 2, 1]

##Q134:
# a = [1, 2, 3, 4]
# a.reverse()
# print(a) #[4, 3, 2, 1]

##Q135:
# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(a, b)#[1, 2, 3] [1, 2, 3, 4] #.copy() naya independent list banata hai, isliye a change nahi hota

##Q136:
# a = [[1, 2], [3, 4]]
# b = a.copy()
# b[0].append(5)
# print(a) #[[1, 2, 5], [3, 4]]

# #Q137:
# a = [1, 2, 3]
# b = a
# a.clear()
# print(b) #[]

##Q138:
# a = [1, 2]
# a.append([3, 4])
# print(len(a)) #3
# print(a)#[1, 2, [3, 4]]

##Q139:
# a = [1, 2]
# a.extend([3, 4])
# print(len(a)) #4


##Q140:
# a = [1, 2, 3]
# a.insert(-1, 99)
# print(a) #[1, 2, 99, 3]

##Q141:
# a = [1, True, 2, 1]
# print(a.count(1)) #3

##Q142:
# a = ["10", "2", "30", "4"]
# a.sort()
# print(a) #['10', '2', '30', '4'] Ye string comparison hai (numeric nahi) — "10" < "2" < "30" < "4" (jaisa pehle discuss kiya tha), toh list already sorted order mein hai.

##Q143:
# a = ["A", "B"]
# a.extend(("C", "D"))
# print(a) #['A', 'B', 'C', 'D']

##Q144:
# a = [1, 2, 3]
# print(a.pop(5)) #Index Error

##Q145:
# a = [10, 20, 30]
# a.insert(-10, 5)
# print(a) #[5, 10, 20, 30]

##Q146:
# a = [3, 1, 2]
# b = sorted(a)
# print(a, b) #[3, 1, 2] [1, 2, 3]

##Q147:
# a = ["cat", "elephant", "dog", "ant"]
# a.sort(key=len, reverse=True)
# print(a) #['elephant', 'cat', 'dog', 'ant']

##Q148:
# a = [1, 2, 3]
# print(a.reverse()) #None

##Q149:
# a = [1, 2]
# a.extend({"x": 10, "y": 20})
# print(a)#[1, 2, 'x', 'y']

##Q150:
# a = [10, 20, 30, 20, 40]
# print(a.index(20, 2, 4)) #3

# print("Hello".startswith("lo", 3) and "Hello".endswith("ell", 0, 3)) #False
