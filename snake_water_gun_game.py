import random

'''
"""
🎮 Snake Water Gun Game 🎮

How to Play:
------------
- This game is similar to Rock-Paper-Scissors.
- You will play against the computer.

Choices:
- Press 's' for Snake 🐍
- Press 'w' for Water 💧
- Press 'g' for Gun 🔫

Rules:
- Snake drinks Water → Snake wins 🐍💧
- Water douses Gun → Water wins 💧🔫
- Gun kills Snake → Gun wins 🔫🐍
- If both choose the same → It's a draw!

Example:
--------
Enter your choice: s
Computer chose: gun
Result: You Lose! Gun kills Snake
"""

snake : 1
water : -1
gun : 0

'''
user_choice= input("what will you choose ? Enter s for snake , w for water or g for gun : ").lower()
youDictionary={"s":1, "w":-1, "g":0}
reverseDictionary = {1:"snake", -1:"water", 0:"gun"}
computer = random.choice ([1,-1,0])
if user_choice not in youDictionary:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
    exit()

you = user_choice
youReverse =youDictionary[you]
computer_choice= reverseDictionary[computer]
print(f"You chose {reverseDictionary [youDictionary[user_choice]]}! \nComputer has chosen {computer_choice}")

if (computer==youDictionary[user_choice]):
    print("it's a draw! ")

else:
 if(computer==1 and youDictionary[user_choice]==-1):
    print("Snake drinks Water 🐍💧...")
    print("Computer wins ")
 elif(computer==1 and youDictionary[user_choice]==0):
    print("Gun kills Snake 🔫🐍...")
    print("You win! ")
 elif(computer==0 and youDictionary[user_choice]==-1):
    print("Water douses Gun 💧🔫... ")
    print("You win! ")
 elif (computer==0 and youDictionary[user_choice]==1):
    print("Gun kills Snake 🔫🐍...")
    print("Computer wins! ")



 elif(computer==-1 and youDictionary[user_choice]==1):
    print("Snake drinks Water 🐍💧...")
    print("You win! ")
 elif(computer==-1 and youDictionary[user_choice]==0):
      print("Water douses Gun 💧🔫...")
      print("Computer wins! ")
 else:
    print("Sorry, something went wrong!")
