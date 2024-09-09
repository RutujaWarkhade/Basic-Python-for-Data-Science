# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:47:55 2024

@author: OM
"""
#print odd number
start,end=4,19
for num in range(start,end+1):
#checking condition
    if num%2!=0:
        print(num,end=" ")
        
#even number
for i in range(1,21):
    if i%2==0:
        print(i,end=" ")
        
start,end=1,15
for n in range(start,end+1):
    if n%3==0:
        print(n,end=" ")
        
x=5
y=6
z=7
print(x)
print(y)
print(z)
########################
x,y,z=5,6,7
print(x)
print(y)
print(z)
#it's give an error because we can not assume diffrent value 
#we can assume same value for diffrent variable in this type
x,y,z=5
print(x)
print(y)
print(z)

#########################
#global variable
x="awesome"
def my_function():
    print("python is "+x)
my_function()

#global and local variable
x="awesome"
def my_function():
    x="fantastic"
    print("python is "+x)
my_function()
print("python is "+x)

#############
x=5
print(type(x))

#########
x=range(6)
print(type(x))
###############
x={"name":"rutuja","age":19}
print(type(x))

##################
#assignment value
x=1
y=2.3
z=2+3j
print(type(x))
print(type(y))
print(type(z))

#############################
str1="hello"
str2=3
str3=str1+str2
#to concatenate strings use str() function
#here you will error: can only concatenate str(not int)
##############
#string
#if you want multiple strings
x="""This is python. It is very powerful"""
print(x)
##############
#string slicing
x="""This is python.It is very powerful"""
print(x)
#string slicing
#string slicing is use print the any particular part from given data
#8-1=7 hence end at 7th position
x="""This is python.It is very powerful"""
print(x[2:8])
####################
#slice from the start
#starts from 0th position
#end at 2nd position
print(x[:3])
########################
#slicing to the end
#at ending last letter should be coming
print(x[4:])
#negative indexing
#-2-1=-3 so end at -3
print(x[-5:-2])
#####################
#modify string
print(x.upper())
#############
x=x.upper()
print(x.lower())
####################
#remove white space, reove white space from initial to final
#remove by default left space
x="  This is python"
#print(x)#in this space is consider
print(x.strip())
##############
x="   this is python"
print(x.lstrip())
#remove left space
############
x="this is python   "
print(x.rstrip())
#remove right spae
#################
x="Hello World!"
print(x.replace("Hello","Gello"))
###############
#use of split which replace white space/or , between letter
x="hello world"
print(x.split(" "))
############################
x="Hello World"
string1=x[::-2]
print(string1)
################
#it is use for reverse the string
x="Hello World"
string1=x[::-1]
print(string1)
#find method,searches the string for a specific value an
x="This is python and it is very powerful"
print(x.find("and"))
#####################
#string concatiness
x="hello"
y="world"
print(x+y)
#################
#to add white space
print(x+" "+y)#to add space between to string
####################
#string format
x=19
y="my name is Rutuja"
print(x+y)
#it will give an error
print(f"my name is rutuja and my age is {x}")
##################
quantity=3
item_no=54
price=67
print(f"I want {quantity} pieces and item number is {item_no},its price is {price}")
my_order="I want {} and item number is {},its price is {}"
print(my_order.format(quantity,item_no,price))

##############################
quantity=str3
item_number=54
price=67
print(f"I want {quantity} pieces and item number is {item_no},its price is {price}")
#in empty space generate the id the id should start with 0
my_order="I want {0} and item number is {1},its price is {2}"
print(my_order.format(quantity,item_no,price))
###################
#the escape character allows you to use double quotes when we print in double quotes
text="This is fun fair it has got big \"round rigo\" "
#text="This is fun fair it has got big "round rigo"" it will give an error
print(text)
########################
a=20
b=10
print(a!=b)
#####################
#operator precedance
print(3*3+3/3-3)
"""
Rules for Mathematical Operations
PEMDAS
P:paranthesis
E:Exponential
M:Multiplication
D:division
A:addition
S:Substration
"""
#########################
#python list
lst=["cherry","banana","apple"]
print(lst)
#########################
#list items are indexed, the first item has index[0],the second item has index[1]
print(lst[0])
print(lst[2])
#########################
#append() add an element at the end of the list
lst=["cherry","banana","apple"]
lst.append("Mango")
print(lst)
#####################
#clear removes all the elements from the list
lst=["cherry","banana","apple"]
lst.clear()
print(lst)
#######################
#copy() method
lst=["cherry","banana","apple"]
lst2=lst.copy()
print(lst2)
#################################
#count() Return the number of times the value "cherry" in the list
lst=["cherry","cherry","banana"]
lst.count("cherry")
###################################
#extend() Add the elements of cars to the fruits list
lst=[1,2,3]
lst1=[4,5,6]
lst.extend(lst1)
print(lst)
############################
#features of python
#mixed datatype
#repeated data type
#mutable
#insert() method,insert the value "orange" as the
#insert the element at given position 
lst=["cherry","cherry","banana"]
lst.insert(1,"mango")
print(lst)
#############################
#pop() removes the element at the specific position
lst=["cherry","cherry","banana"]
lst.pop(2)
print(lst)
################################
#remove() remove the element by default at 0th position
lst=["cherry","cherry","banana"]
lst.remove("banana")
print(lst)
###################################
#to reverse the element in reverse order
lst=["cherry","cherry","banana"]
lst.reverse()
print(lst)
################################
#sort() sort the list alphabetically
lst=["cherry","orange","banana"]
lst.sort()
print(lst)
###################################
#########Tupple
#tupple is immutable i.e we can not change
#it allows mixed datatype
tup=("cherry","cherry","banana")
print(tup)
print(tup[2])
#################################
#once a tuple is created, you cannot change its value
#if change then it is converted into list
x=("apple","banana","cherry")
#x[1]="kiwi"#in tuple we can not change
#to replace 1st convert it into list
#it gives an error if not convert it into list 
#if we direct perform operation on tuple
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)
###########################
a=("rutuja","tanuja","sai","yash")#assume tuple
b=list(a)#convert into list
b[1]="tanuuu"#make changes
a=tuple(b)#again convert it into tuple
print(a)#print changes tuple
#########################
x=("apple")
print(x[1])
###########################
#to join two or more tuples you can use the + operator
tuple1=('a','b','c')
tuple2=(1,2,3)
tup1=tuple1+tuple2
print(tup1)
############################
#Dictionary
dict1={"Brand":"Maruti","model":2345,"year":2011}
print(dict1)
print(len(dict1))
print(type(dict1))
##########################
dict1.get("model")
dict1.keys()
###############################
#nested dictionary
dict={"brand":["Maruti","Mahendra","Toyato"],
   "Model":["a","b","c"],
   "year":[2011,2012,2013]}
print(dict)
#################################


