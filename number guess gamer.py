import random

number=random.randint(1,100)
guesses=0

print("welcome to a guessing game!!!")
print("i have guessed a number now its your turn !")

while True:
    num=int(input("enter a number:"))
    guesses += 1

    if num>number:
        print("the guess is too high")

    elif num<number:
        print("the guess is low")

    else:
        print("you have guessed the correct number !!!")
        break

print("u had quite a good amt of guesses: ",guesses)