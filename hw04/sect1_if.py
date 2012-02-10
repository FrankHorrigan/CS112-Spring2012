#!/usr/bin/env python

"""
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

print "1.", __


# 2. If n is odd, double it
print "2.", n


# 3. If n is evenly divisible by 3, add four
print "3.", n


# 4. What is grade's letter value (eg. 90-100)
egg = raw_input("Enter a grade [0-100]: ")
egg = int(egg)

print "4.", __

"""
n = raw_input("Enter a number: ")
n = int(n)
if n %2==0:
        print "Even Number."
else:
        print "Odd number. Doubling:"
	n*=2
	print n
if n %3 == 0:
	print "Divisible by three. Adding Four:"
	n+=4
	print n

egg = raw_input("Enter a grade, #0 - 100: ")
egg = int(egg)

if egg >=0 and egg <60: 
	print "fail"
elif egg >60 and egg <=70:
	print "D."
elif egg >70 and egg <=80:
	print "C."
elif egg >80 and egg <=90:
	print "B."
elif egg >90 and egg <=100:
	print "A."
elif egg >100 and egg <=9000:
	print "I never asked for this."
elif egg >9000:
	print "OVER NINE THOUSAAAAAAAAAAAAAAAAAAAAAAAAAND!"



