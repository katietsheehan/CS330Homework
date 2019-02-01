########LAB 1 Intro to Python ##########
##### Guessing Game ########
import random

name = input ("What is your Name?")
print (name)
print ("You will have 7 tries to guess a random number 1 - 10")

win = False 
num = random.randint(1,10)
turns = 0
guess = 0
guesses = []

while guess != num and turns < 7:
    guess = int(input("Enter a number: "))
    print (guess)
    if guess not in guesses:
        guesses.append(guess)
        if guess == num:
            print ("Correct")
            win = True
        else:
            print ("Incorrect")
            turns = turns + 1
    else:
        print ("Already guessed, guess again.")

if win:
    print (name + ", Congradulations you win!")
else:
    print ("Sorry, " + name + " you lost!")
    print ("The correct answer was " + str(num))
        
print ("Your guesses were: ")
for guess in guesses:
    print (guess)

