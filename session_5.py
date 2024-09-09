# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 02:45:24 2024

@author: OM
"""
car={
     "brand":"ford",
     "model":"mustarg",
     "year":1964
     }
x=car.keys()
print(x)
car["colour"]="white"#to add new key value pair
car
x=car.keys()
print(x)
#removing the dictionary element
car={"brand":"ford","model":"mustang",
     "year":1964}
car.pop("model")
print(car)
####################################
#accessing keys in dictionary
for x in car:
    print(car[x])
#accepting both keys and values
#IMP

for key,value in car.items():
    print("%s=%s"%(key,value))
    
    
#coping dictionary
car={"brand":"ford","model":"mustang",
     "year":1964}
car2=car.copy()
car2
#another way to make copy of dictionary
thisdict={"brand":"ford","model":"mustang",
     "year":1964}
dict1=dict(thisdict)
dict1
#############################
#A dictionary can contain dictionaries,
#this is called nested dictionaries
our_family={"child1":{"name":"ram","dob":"21-05-2005"},
            "child2":{"name":"sham","dob":"01-05-2005"}}
our_family
                      
#clear():remove all elements from car
car={
     "brand":"ford","model":"mustang",
     "year":1965}
car.clear()
car
#fromkey()
#create a dictionary with 3 keys,
x={'key1','key2','key3'}
y=3
thisdict=dict.fromkeys(x,y)
thisdict
#get():to get the value
car={
     "brand":"ford","model":"mustang",
     "year":1964}
car.get("model")
############################################
#items()return the dictionarys key value
car={
     "brand":"ford","model":"mustang",
     "year":1964}
car.items()
############################################
#values():display all the values
car={
     "brand":"ford","model":"mustang",
     "year":1964}
car.values()
###################################
#update():insert an item to the dictionary
car={
     "brand":"ford","model":"mustang",
     "year":1964}
car.update({"color":"white"})
car
#############################
#for loop
fruits=["apple","banana","cherry"]
for i in fruits:
    print(i)
####################
#use of break statement
fruits=["apple","banana","orange"]
for i in fruits:
    print(i)
    if(i=="banana"):
        break
#here first time it will print apple,check
fruits=["apple","banana","orange"]
for i in fruits:
     if(i=="banana"):
         break
     print(i)
#############################
#continue:banana not print
fruits=["apple","banana","orange"]
for x in fruits:
    if(x=="banana"):
        continue
    print(x) 
    
    
##################################
car={"brand":"fort",
     "model":"mustarg",
     "year":1964 
     }
x=car.keys()
print(x)
car["color"]="white"
car
x=car.keys()
print(x)
#removing the dictinory element
car={"brand":"ford","model":"mustang","year":1964}
car.pop("model")
print(car)

######################
#accessing keys in dictionary
for x in car:
    print(car[x])
#accepting both keys and values 
#import 
for key,value in car.items():
    print(car)
#Adding data items in dictionary
#Range
for x in range(2,6):
     print(x)
################################
for x in range(2,30,3):
    print(x)
###########################
#a nested loop is a loop inside a loop
colors=["green","yellow","red"]
fruits=["guava","banana","apple"]
for x in colors:
    for y in fruits:
        print(x,y)
###########################
#function()without agrument/parameeter
def my_function():
    print("Hello from a function")
my_function()
##########################
def my_function(name):
    print("Hello"+name)
my_function("ram")
###########################
#functiom of position called postional argument
def my_function(name1,name2):
    print(name1+" "+name2)
my_function("world","hello")
################################
#arbitrary arguments, *args
#if you dont know how many arguments that
#will be passed in your function
#add a* before the parameter name
#the function definition
def my_function(*kids):
    print(kids[0]+" "+kids[2])
my_function("hello","world","india")
####################################
#keyword arguments
#kwargs it is a word only ** is imp give key and value

def myfun(**kwargs):
    for key, value in kwargs.items():
        print("%s==%s"%(key,value))
myfun(first='papalala',mid='mohanlal',last='goyal')
################################


def my_function(country=" norway"):
      print("I am from" + country)
my_function(" sweden")
my_function(" India")
my_function()
my_function(" Brazil")

##################################
#passing list as an arrgument
fruits=["orange","banana","guava"]
def my_function(fruits):
    for x in fruits:
        print(x)
my_function(fruits)
##################################
#return values
def my_function(x):
    return x*5
my_function(5)
my_function(7)
##################################
#pass function
def my_function():
    pass
#have an empty function definition
#like this would raised an error
#without pass stament
################################
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
factorial(3)
factorial(6)
############################
#a lambda function is a small
#anonymous function
#a lambda function can take
#any number of arguments
#but can only have one expression
def add(a):
    sum=a+10
    return sum
add(20)
add=lambda a:a+10
print(add(20))
######################
#lambada function can take any number of arguments:
add=lambda a,b:a+b
print(add(5,6))
###############################
lst=[34,12,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2!=0),lst))
print(odd_lst)
###################
#find out even numbers
lst=[34,12,64,55,75,13,63]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)
###########################
