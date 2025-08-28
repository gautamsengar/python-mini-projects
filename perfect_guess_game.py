'''🎮 Guess the Number Game

This is a simple Python game where:

The computer randomly selects a number between 0 and 100.

The player’s goal is to guess the number.

After each guess, the program gives hints:

“Guess bigger number” if the guess is too small.

“Guess smaller number” if the guess is too large.

“Out of range” if the guess is not between 0–100.

The loop continues until the player guesses correctly.

Finally, the program prints 🎉 a congratulatory message with the number of attempts taken.'''


import random
computer_choice = random.randint(0,100)
print("Guess! a number that computer has chosen between 0-100 🙌")
print("now it's your turn to find the number chosen by the computer 😊 ")
user_choice = -1
guess=0
while (user_choice!=computer_choice):
    user_choice = int(input("Choose a number :"))
    guess+= 1
    if(user_choice<0 or user_choice>100):
     print("you chose number which is out of range, kindly choose number between 0-100 ,TRY AGAIN!")
    elif(user_choice<computer_choice):
     print("guess bigger number")

    elif(user_choice>computer_choice):
     print("guess smaller number")
    
    
    else:
     print(f"Yay! you guessed the {computer_choice} number in {guess} attempts! 🎊🎉")