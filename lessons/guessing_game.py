"""Asks user for a number, goes until they get it right"""

SECRET: int = 4
guess: int = int(input("Guess a number! "))
playing: bool = True

while playing:
    if guess == SECRET:
        print("Yay! You got it right.")
        playing = False
    else: 
        print("Wrong number :(")
        if guess % 2 == 1: 
            print("Your guess is odd. The answer is even.")
        if guess > SECRET:
            print("Your guess is too high! ")
        guess = int(input("Make another guess! "))