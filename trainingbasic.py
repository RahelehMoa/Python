print("hello Raheleh Moallemi")
#---N = 1
#---n = 1.0
#---S = "c:\temp"
#---B = True
#---time = dt.time(16,41,25,13)
#---shopping_list = ["bread","pumpkin"]
#---shopping_tuple = ("mascara","shoes",1000)
#---Ita_Eng = {"casa":"house","cane":"dog"}
#---DataFrame = {'col1':['obs1','obs2'],
#                'col2':['pippo1','pippo2'],
#                'index':['idx1',’idx2']}
#number , write on number
N = 1
print(type(N))

n = 1.0
print(type(n))

#string , write one string
S = "1"
print(type(S))

#boolean
B = True
print(type(B))

b = False
print(type(b))

print(B*2)

#ERROR
Q = None
print(type(Q))

#print(Q+1)

#basic operations
a = 3
c = 4
print(a+c)
print(a-c)
print(a*c)
print(a/c)
print(a**c)   #توان #power or exponentiation
print(a%c)    #بقیه بخش #rest of the division

name = "nome"
lastname = "cognome"
number = 3
print(name+lastname)        #concatenate without space 
print(name+" "+lastname)    #concatanate with space
print(name*number)          #repet the string number times of repet
#print(name+number)         #ERROR for concatenate with int and string
print(name, number)

D = "Questa è una stringa"
print(D[0])                 #first charecter
print(D[-1])                #end   charecter
print(D[-3])
print(D[0:10])             #from 0 to 9 charecters
print(D[0:7])

E = "Questa è una stringa"                        #write one sentences in string type.
print(E.replace("Questa", "la variabile 'a'"))    # replaces
print(E.upper())                                  # all uppercase
print(E.lower())                                  # all lowercas
#-------------------------------------------------------------------------------------------------
#---------------------------------------------list------------------------------------------------
shopping_list1 = ["bread","pumpkin"]
print(shopping_list1)
print(type(shopping_list1))

shopping_list2 = ["bread", 0.75, True]
print(type(shopping_list2))

G = "stringa"
l = [G , 2]   #list of one variable G and number 2.
print(l)

l_long = [10, 20, 30, 40, 50, 60, "70", 80, 90]   #list of Numbers and "70" is string.
print(l_long[0])         # first element
print(l_long[-2])        # second element from the End 
print(l_long[1:4])       # second to fourth element
print(l_long[4:])        # fifth element to End
print(l_long[0:3:2])     # first three elements in steps of two 
print(l_long[0::2])      # all elements in steps of two (even indices)

l_num = [3, 2, 3, 4, 1, 8, 21] 
l_num[1] = 7
print(l_num)

l_num.append(10)
l_num.remove(1)
l_num.sort()
l_num.extend([5,6])
l_num.count(3)

l_number = [3, 2, 3, 4, 1, 8, 21]
print(5 in l_number)
print(3 in l_number)

N = "nuova stringa"
print("nuo" in N)

Letter = "un'altra nuova stringa"
M = Letter.split(" ")
print(M)
print(type(M))

l_num2 = [3, 2, 3, 4, 1, 8, 21]
num_2 = [11, 5, 8]
print(l_num2 + num_2)

num = 5
#stringa = "test"
#num_f = 2.2
#print(l_num + num)        #ERROR
#print(l_num + stringa)    #ERROR

print(l_num2 * num)
#print(l_num2 * num_f)     #ERROR

#--------------------------------------------------------------------------------------------------
#------------------------------------------tuple---------------------------------------------------

wife_shopping_tuple = ("mascara", "shoes", 1000)
print(wife_shopping_tuple)
print(type(wife_shopping_tuple))

#wife_shopping_tuple.append("nuovo") #tuple has no append because read-only
#wife_shopping_tuple.remove("shoes") #tuple has no remove because read-only
print(wife_shopping_tuple.count("mascara"))
print(wife_shopping_tuple[0])

print(1000 in wife_shopping_tuple)

# two tuple is add toghether 
t1 = (1, 3, 5)
t2 = (2, 4)
t1 = t1 + t2
print(t1)
#print(t1 – t2) #unsupported 
print(t1 * 2)
#num_2 = [11, 5, 8]  #concatenate list and tuple is not possible
#print(t1 + num_2)
#--------------------------------------------------------------------------------------------------
#----------------------------------dictionary------------------------------------------------------
#key is string and value is string and number.
Italian_English = {"casa": "house", "cane": "dog", "patata": 4}
print(type(Italian_English))
#print(Italian_English[0])  #ERROR in dic, it is just posibile in list and tuple
print(Italian_English["casa"])

print(Italian_English.keys())
print(Italian_English.values())

#Replace in Dictionary
Italian_English["tavolo"] = "table"
Italian_English["patata"] = "potato"
print(Italian_English)
#Remove in Dictionary
Italian_English.pop("casa", None)
print(Italian_English)
#cocatenate key and value in Dictionary
Italian_English[0] = 2
Italian_English["10"] = 2
print(Italian_English)

print("cane" in Italian_English.keys())
print("table" in Italian_English.values())
print(2 in Italian_English.keys())
print("patata" in Italian_English)

#--------------------------------------------------------------------------------------------------
#-----------------------------------------SET------------------------------------------------------
my_set = {1.0,"Hello",(1,2,3)}
print(my_set)
print(type(my_set))

#my_set[0]    #ERROR
print(1.0 in my_set)

my_set.add("nuovo")
my_set.update(["primo", "secondo"])
print(my_set)

my_set.discard((1,2,3))
print(my_set)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
#print(a + b)  #UNSUPPORTED
print(a - b)   
#print(a * 2)  #UNSUPORTED

x = a.union(b) # (a | b) unione
print(x)

y = a.intersection(b) # (a & b) intersezione
print(y)

w = a.symmetric_difference(b) # (a ^ b) diff simmetrica
print(w)

z = a.difference(b) # (a - b) differenza
print(z)

#--------------------------------------------------------------------------------------------------
#---------------------------------Generic operators------------------------------------------------

l = [1, 3, 5]
print(sum(l))
print(min(l))
print(max(l))
print(min(3, 5))
#sum(3, 5) #ERROR

pi =-3.14159
print(abs(pi))
print(round(pi))
print(round(pi, 3))

sentences = "esempio stringa"
list = [1, 3, 5]
my_dict = {"cane":"dog", "gatto":"cat"}
print(len(sentences))
print(len(list))
print(len(my_dict))

#--------------------------------------------------------------------------------------------------
#---------------------------------------------Del--------------------------------------------------
New_list = [1, 4, 7]
del New_list
#print(New_list)  #ERROR New_list is empty

New_list2 = [1, 4, 7]
New_dict3 = {"cane":"dog", "gatto":"cat"}

del New_list2[1]
del New_dict3["cane"]

print(New_list2)
print(New_dict3)

#--------------------------------------------------------------------------------------------------
#---------------------------------------------Dir--------------------------------------------------

print(dir(New_list2))
print(dir(str))
print(dir("papera"))
print("-------------------------------------------------------------------------------------------")
#--------------------------------------------------------------------------------------------------
#--------------------------------------------Date Time---------------------------------------------

import datetime as dt

d = dt.date(2026, 6, 20)
print(d)
print(type(d))

dir(dt.date)

today = dt.date.today()
print("Year Current:", today.year)
print("Month Current:", today.month)
print("Day Current:", today.day)

print("-------------------------------------------------------------------------------------------")

Hour = dt.time(14, 55, 27)
print(Hour)
print(type(Hour))

orario = dt.time(14, 55, 27)
print("Hour Current:", orario.hour)
print("Minute Current:", orario.minute)
print("Second Current:", orario.second)

print("-------------------------------------------------------------------------------------------")

d1 = dt.datetime(2026, 7, 15)
print(d1)
print(type(d1))

d2 = dt.datetime(2026,7,15, 14,55,27)
print(d2)
print(type(d2))

print(dt.datetime.now())
print(d2.time())
print(d2.date())

print("-------------------------------------------------------------------------------------")

print("Year Corrent:", d2.year)
print("Month Corrent:", d2.month)
print("Day Corrent:", d2.day)
print("Hour Corrent:", d2.hour)
print("Minuti Corrent:", d2.minute)
print("Second Corrent:", d2.second)

print("---------------------------------------------------------------------------------------")

#Different Times

data1 = dt.date(2026, 1, 20)
data2 = dt.date(2026, 6, 23)
diff = data2- data1
print(diff)
print(type(diff))

print("---------------------------------------------------------------------------------------")

dt_1 = dt.datetime(2026, 4, 8, 16, 10, 0)
dt_2 = dt.datetime(2026, 6, 23, 22, 29, 12)
dt_diff = dt_2- dt_1
print(dt_diff)
print(type(dt_diff))

print(dt_diff.days)
print(dt_diff.seconds)

print("---------------------------------------------------------------------------------------")

t1 = dt.timedelta(12, 8)
t2 = dt.timedelta(weeks=3, days=12, hours=20)
print(t1)
print(t2)

print("---------------------------------------------------------------------------------------")

# Sum or Differents of Times

dt_2 = dt.datetime(2026, 6, 23, 22, 29, 12)
t2 = dt.timedelta(weeks=3, days=12, hours=20)
t_d1 = dt_2 + t2
t_d2 = dt_2- t2
print(t_d1)
print(t_d2)
print(type(t_d1))
print(type(t_d2))

print("---------------------------------------------------------------------------------------")

print("date", t_d1.date(), "has day index:", t_d1.weekday())
print("date", t_d2.date(), "has day index::", t_d2.weekday())

print("---------------------------------------------------------------------------------------")

import datetime as dt
data2 = dt.date(2026, 6, 23)
data_s = str(data2)   #string
data_s2 = data2.strftime("%d/%m/%Y")   #string with another format
print(data_s)
print(data_s2)
print(type(data_s))
print(type(data_s2))

print("---------------------------------------------------------------------------------------")

new_datetime = dt.datetime.strptime(data_s2, "%d/%m/%Y")
print(new_datetime)
new_date = new_datetime.date()
print(new_date)
print(type(new_datetime))
print(type(new_date))

print("New Date Format:")

print(data2.strftime("%d/%m/%y"))
print(data2.strftime("%d/%b/%y"))

print("---------------------------------------------------------------------------------------")

print("Convert int to String and List , Dictionary :")

string = "-10"
num = int(string)
print(type(num))
print(num + 1)

num =-10
string = str(num)
print(type(string))

#string = "10, stringa"
#num = int(string)    #ERROR
l_C = [1, 2, 3, "quattro"]
l_s = str(l_C)
print(type(l_s))
print(l_s)
#l_C_list = list(l_s)
#print(type(l_C_list))

#Italian_English2 = {"casa": "house", "cane": "dog", "patata": 4}
#keys = list(Italian_English.keys())
#values222 = list(Italian_English2.values())
#print(type(keys))
#print(type(values222))

#d22 = dict(zip(keys, values))
#print(type(d22))

print("list to set:")
list_set = [1, 2, 3, 5, 1, 2, 2, 3]
set = set(list_set)
print(type(list_set))
print(list_set)