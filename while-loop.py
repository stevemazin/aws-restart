import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)
isGuessRight = False

# ask user to guess
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    # is the guess the correct number?
    if int(guess) == number:
        # if it was the correct guess
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        # if it is the wrong guess, tell the user it was the wrong guess and continue the loop
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
