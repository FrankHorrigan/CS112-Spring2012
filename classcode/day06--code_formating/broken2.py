#!/usr/bin/env python

#I have no idea what this code does
from random import randint
bacon=1
egg=int(raw_input())
spam=[]
for _ in range(egg):
    spam.append(randint(0,20))
print spam
while bacon:
    bacon=0
    for i in range(1,egg):
        if spam[i-1]>spam[i]:
            egg1=spam[i-1]
            egg2=spam[i]
            spam[i-1]=egg2
            spam[i]=egg1
            bacon=1
print spam
