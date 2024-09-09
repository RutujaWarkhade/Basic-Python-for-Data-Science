# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:03:16 2024

@author: OM
"""
age=input('enter age:')
print(type(age))
print(age)

age1=input("enter age1")
print(type(age1))
print(age1)
age2=input("enter age2")
print(type(age2))
print(age2)
age=age1+age2
print(age)

age1=int(input("enter age1"))
print(type(age1))
print(age1)
age2=int(input("enter age2"))
print(type(age2))
print(age2)
age=age1+age2
print(age)

exchange_rate=1.83
print(exchange_rate)
print(type(exchange_rate))

int_value=160
string_value='1.5'
float_value=float(int_value)
print('int value as a float:',float_value)
print(type(float_value))
float_value=float(string_value)
print('string value as a float:',float_value)
print(type(float_value))

#complex number
c1=1
c2=3j
print('c1:',c1,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#Boolean value
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))
####################################
#you can also convert string into boolean as long a
#True or False (and nothing else).
status=bool(input('ok it is confirmed?:'))
print(status)
print(type(status))
#if we don't give any input then it print false
#####################################
#Arithmatic Operator
home=10
away=15
print(home+away)
print(type(home+away))
print(10*4)
print(type(10*4))
goals_for=10
goals_against=7
print(goals_for-goals_against)
print(type(goals_for-goals_against))

print(100/20)
print(type(100/20))

print(100//20)
print(type(100//20))

