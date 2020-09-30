# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:10:58 2020

@author: shrey
"""

print("Rock..")
print("paper..")
print("Scissor..")
#This are in main script in python

player1 =str(input("player 1,make your move:"))
player2 =str(input("player 2,make your move:"))

if player1 == player2:
    print("it's a tie")
elif player1 == "rock":
    if player2 == "scissors":
      print("player1 wins")
elif player1 == "paper":
      print("player2 wins")
elif player1 == "paper":
  if player2 =="rock":
      print("player1 wins")
elif player2 =="scissors":
    print("player2 wins")
elif player1 =="scissors":
  if player2 =="paper":
      print("player1 wins")
elif player2 =="rock":
    print("player 2 wins")
else:
   print("something went wong")    
     
     

