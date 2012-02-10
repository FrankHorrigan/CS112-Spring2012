#!/usr/bin/env python
from hwtools import *
print "Enter a series of numbers seperated by commas to find their sum."

nums=input_nums()
leng=int(len(nums))
print "sum: ",sum(nums)
"""
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?

print "1.", __


# 2. Print every even number in nums
print "2. even numbers" """

print "even numbers: "
for i in nums: 
    if i %2==0:
        print i,
print


"""
# 3. Does nums only contain even numbers? 
only_even = False
"""

for i in nums:
    if i%2!=0:
        snot=2
if snot==1:
    print "All numbers are even"
elif snot==2:
    print "Some numbers are odd."

"""
print "3.",
if only_even:
    print "only even"
else:
    print "some odd"

# 4. Generate a list every odd number less than 100. Hint: use range()
print "4.", __

# 5. [ADVANCED]  Multiply each element in nums by its index
print "5.", __
"""
oddball=[]
for i in range(1,101,2):
    oddball.append(i)
print
print oddball
print





