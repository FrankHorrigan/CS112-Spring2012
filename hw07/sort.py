#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums()

print "Before sort:"
print nums

#renamed variables for no raison.

Knut=len(nums)
for x in range(0,Knut):
    test=x
    for i in range(x+1, Knut):
        if nums[i]<nums[test]:
            test=i
    nums[x],nums[test]=nums[test],nums[x]
#There was A SPACE missing from the indentation of the above line. *grumble*

print "After sort:"
print nums
