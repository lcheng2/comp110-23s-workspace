"""EX02 - Wordle."""

__author__ = "730517752"

word: str = "python"
word_num: int = len(word)
guess: str = input(f"What is your {word_num}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
output: str = ""

while i < word_num: 
    guess_num: int = int(len(guess))
    if word_num == guess_num and word[i] == guess[i]:      # checks if number of letters is correct and if the index matches
        output += GREEN_BOX
    elif word_num == guess_num and word[i] != guess[i]:    # checks if number of letters is correct and if the index does not match
        idx: int = 0
        inWord = False
        while idx < word_num:     # checks for letter in word but not at right index
            if guess[i] == word[idx]:
                inWord = True
            idx = idx + 1
        if inWord:
            output += YELLOW_BOX
        else:
            output += WHITE_BOX
    elif word_num != guess_num:
        guess = str(input(f"That was not {word_num} letters! Try again:"))
    i = i + 1
print(output)
if word == guess:
    print("Woo! You got it!")
if guess_num == word_num and word != guess:
    print(str("Not Quite. Play again Soon!"))