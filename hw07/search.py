#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

nums=input_nums()
nums.sort()

print "I have sorted your numbers"
huey=int(raw_input("Which number should I find: "))

dewey=0
louie=len(nums)-1

#hurr variable names hurr
#work

while louie>=dewey:
    mid=louie+dewey/2

    if nums[mid]==huey:
        break
    elif huey>nums[mid]:
       dewey=mid+1
    else:
       louie=mid-1

#problem line "else:" above. Non comprehendo.

if nums[mid]==huey:
    print "Found %s at %s"%(huey,mid)
else:
    print "Could not find", huey
