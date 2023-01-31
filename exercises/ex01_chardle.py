"""EX01 - Chardle"""
__author__ = "730517752"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
char: str = input("Enter a single character: ")
if len(char) != 1:
    print("Error: Character must be a single character.")
    exit()
number_of_char: int = 0
print("Searching for " + char + " in " + word)

if word[0] == char:
    number_of_char = number_of_char + 1
    print(str(char) + " found at index 0")
if word[1] == char:
    number_of_char = number_of_char + 1
    print(str(char) + " found at index 1")
if word[2] == char:
    number_of_char = number_of_char + 1
    print(str(char) + " found at index 2")
if word[3] == char:
    number_of_char = number_of_char + 1
    print(str(char) + " found at index 3")
if word[4] == char:
    number_of_char = number_of_char + 1
    print(str(char) + " found at index 4")
if number_of_char == 0:
    print("No instances of " + str(char) + "found in heels")
if number_of_char == 1:
    print(str(number_of_char) + " instance of " + str(char) + " found in " + str(word))
else:
    print(str(number_of_char) + " instances of " + str(char) + " found in " + str(word))
