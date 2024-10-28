# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:47:37 2024

@author: om
"""

"""
Q2. Write a python program to find a list of integers with exactly two 
occurrences of nineteen and at least three occurrences of five. Return True 
otherwise False. 
e.g. Input: 
[19, 19, 15, 5, 3, 5, 5, 2] 
Output: 
True 
Input: 
[19, 15, 15, 5, 3, 3, 5, 2] 
Output: 
False 
"""

l=list(map(int,input("Input:").split()))
print(l)
def my_fun(l):
    if l.count(19)==2 and l.count(5)>=3:
        return True
    return False
my_fun(l)
       
"""
Q3. Write a python program to find numbers that are greater than 10 and have 
odd first and last digits. 
e.g:  Input: 
[1, 3, 79, 10, 4, 1, 39, 62] 
Output: 
[79, 39] 
Input: 
[11, 31, 77, 93, 48, 1, 57] 
Output: 
[11, 31, 77, 93, 57]
""" 
l=list(map(int,input("Input:").split()))
def my_fun(l):
    a=str(l)
    first_digit = int(a[0])
    last_digit = int(a[-1])
    return first_digit%2!=0 and last_digit%2!=0
result = [i for i in l if i>10 and my_fun(i)]
print(result)

#or
l1=[1, 3, 79, 10, 4, 1, 39, 62]
l2=[]
for i in l1:
    if i>10:
        n=str(i)
        f=int(n[0])
        l=int(n[-1])
        if (f%2!=0) and (l%2!=0):
            l2.append(i)
print(l2)

        
"""
Q4. Write a python program to find the largest negative and smallest positive 
numbers (or 0 if none). 
e.g. Input:   
[-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18] 
Output: 
[-6, 2]
"""
l=list(map(int,input("Input:").split()))
p=[i for i in l if i>0]
n=[i for i in l if i<0]
l1 = max(n),min(p)
print(list(l1))


"""
2. Write a Python program to find the median of below three values. 
Values: (25,55,65) 
"""
Values= [25,55,65] 
a=int(len(Values)/2)
print(Values[a])

"""
3. Write a program to create a decorator function to measure the 
execution time of a function.
"""

"""
4. Write a python program that opens a file and handles a 
FileNotFoundError exception if the file does not exist. 
"""
try:
    import os
    with open("data.txt") as raw_data:
        print(raw_data.read())
except FileNotFoundError:
    print("FileNotFoundError")
    
"""
5. Write a python program to find the intersection of two given arrays 
using Lambda. 
Original arrays: 
[1, 2, 3, 5, 7, 8, 9, 10] 
[1, 2, 4, 8, 9] 
Intersection of the said arrays: [1, 2, 8, 9]
"""
a=[1, 2, 3, 5, 7, 8, 9, 10] 
b=[1, 2, 4, 8, 9] 
c=list(filter(lambda x : x in a,b))
print(c)
