##def cribbage_sequence(card_list):
##    print(card_list)
##    card_list.sort()
##    print(card_list)
##    if(1 <= card_list[0] <= 13) and (1 <= card_list[1] <= 13) and (1 <= card_list[2] <=13):
##        if(card_list[1] == card_list[0] + 1) and (card_list[2] == card_list[0] + 2):
##            return True
##        else:
##            return False
##    else:
##        return False
##

import turtle
import random


window = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["red", "green", "blue"]:
    alex.color(aColor)
    alex.forward(50)
    alex.left(120)
