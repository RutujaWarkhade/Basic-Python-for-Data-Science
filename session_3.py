# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 19:37:08 2024

@author: OM
"""
#division
print(100/20)
print(type(100/20))
#integer division(floor division)
print(100//20)
print(type(100//20))
#modulus division
print('modulus division 100%13',100%13)
print('modulus division 3 % 2',3 % 2)

#power operator
a=5
b=3
print(a**b)

#Assignment operator
x=5
x
x+=1
x

#None operator
winner=None
print(winner is None)

winner=None
print('winner:',winner)
print('winner is None:',winner is None)
print('winner is None:',winner is not None)
print(type(winner))

#Indentation
num=int(input('enter a number'))
if num>0:
    print(num)#not provide indentation it give indentation error

#when it execute it can select whole code the execute
#let's give indentation
#if
num=int(input("enter a number"))
if num>0:
    print(num)

#else is an if statement
#else if
num=int(input('enter number'))
if num<0:
  print('It is negative')
else:
  print('It is not negative')

#elif
savings=float(input('enter how much you have saving:'))
if savings==0:
    print("sorry no saving")
elif savings<500:
    print("weldone")
elif savings<1000:
    print("That's a tidy sum")
elif savings<10000:
    print('Welcome Sir!')
else:
    print("Thank you")
    
#while loop
count=1
print('starting')
while count<=10:
    print(count)
    count+=1

#FOR LOOP
#loop over set of values in a range
print("print out values in range")
for i in range(2,10):
    print(i)
print("done")
    
##################
print("only print code if all iterations completed")
num=int(input("enter a number to check for:"))
#if we enter above 16 number then it can stop at 15
for i in range(0,16):
    if i==num:
        break
    print(i)
print("done")
    
#ANONYMOUS VARIABLE
#use for saving space of memory or space complexity
for _ in range(1,11):
    print(".",end="")
    print()
##########################  
for _ in range(1,11):
    print("#",end=' ')
    #print()