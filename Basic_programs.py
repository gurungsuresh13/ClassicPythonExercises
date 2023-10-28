""""

#Factorial Program
f=1
a=int(input("Enter a number: "))
if a<0:
    print("No factorial")
elif a==0:
    print("Factorial is 1")
else:
    for i in range(1,a+1):
         f=f*i
    print("The factorial of a number is ",f) 

"""

""""
#Fibonnaci Series
first=0
second=1
print(first)
print(second)
for i in range(2,10):
    next=first+second
    first=second
    second=next
    print(next)
"""

"""
#Swapping two numbers
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=a
a=b
b=c 
print("The swapped numbers are",a,b)
"""

"""
#Reversal of a string
string="How tremendous the agony of unmade decisions"
b=string.split()
b=b[-1::-1]
outputstring=" ".join(b)
print(outputstring)
"""

"""
#Prime Number
x = int(input("Enter a number:"))
for i in range(2, x):
    if x % i == 0:
        print("Not a prime")
        break
else:
    print("A prime")
"""

"""
#Armstrong Number
number = int(input("Enter a number:"))
sum=0
order=len(str(number))
a=number
while number>0:
 digit = number % 10
 sum += digit ** order
 number = number // 10
if (sum==a):
  print("Armstrong number")
else:
 print("Not Armstrong number")
 """

"""
#Call By
def tech(string):
 string = "Greatlearning"
 print("Inside", string)
string = "GL"
tech(string)
print("Outside", string)

def tech(set):
 set.add(56)
 print("Inside",set)
set1 = {43,57,88}
tech(set1)
print("Outside", set1)
"""

"""
#Second largest number
list1=[1,2,3,4,5,9,6,11] 
list1.sort()
print(list1[-2])
"""

"""
#Palindrome number
number = int(input("Enter a number:"))
reverse = 0
a=number
while (number>0):
 digit=number%10
 reverse=reverse*10+digit
 number=number//10
if(reverse==a):
   print("Palindrome number")
else:
    print("Not Palindrome number")
"""

"""
#Pattern
no_of_rows = 5
for i in range(no_of_rows):
 for j in range(i):
  print(i, end=' ')
 print('')
"""

"""
#Pascal triangle
no_of_rows = 5
x=no_of_rows
for i in range(x): 
 print(' '*(x-i), end='') 
 print(' '.join(map(str, str(11**i))))
"""

"""
#Matrix Multiplication
import numpy as np
a = ([1, 4, 5],[6 ,5, 4],[7, 6, 5])
b = ([9, 2, 8],[3, 2, 1],[1,13, 7])
c = np.dot(a,b)
print(c)
"""
