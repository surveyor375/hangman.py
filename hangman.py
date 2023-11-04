import random

# create a greeting
print("Welcome to hangman!")

# create your wordlist
words = ["hacker", "bounty", "random"]

# randomly choose a word from the list you have created
secret_word = random.choice(words)

# ask the user to guess a letter
guess = input("Guess a letter").lower()

# bonus make the program take input from the user and make it lowercase

# check if the letter is in the word
for letter in secret_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
