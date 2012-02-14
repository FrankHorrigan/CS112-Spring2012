#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

#Understood. "Now I suppose you're going to tell me you're just out looking for a water chip. Do I look dumb? Get him!" 

print "there are 50 stones in the pile. You may take from 1 to 5 out of the pile. The player who takes away the last stone loses."

#The actual code goes here. Comments. Blah.

stones=50
player = 1

while stones>0:
    remove=int(raw_input("Player "+str(player)+": take from 1-5 stones: "))
    if remove>5 or remove<1:
        print "I'm sorry Dave, I'm afraid I really can't do that."
    else: 
        stones-=remove
        if player == 2:
            player = 1
        else:
            player = 2
        if stones>0:
            print "-",stones,"stones remain."
        elif stones<=0:
            print "The wasteland has claimed you."

#This sentence is a comment.
	 
raw_input()

