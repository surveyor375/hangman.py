import random

# create a greeting
print("Welcome to hangman!")

# create your wordlist
words = ["hacker", "bounty", "random"]
# randomly choose a word from the list you have created
secret_word = random.choice(words)
print(secret_word)
print("You have 5 guesses")
display_word = []

for lett in secret_word:
    display_word += "_"
print(display_word)
# ask the user to guess a letter

# bonus make the program take input from the user and make it lowercase

# check if the letter is in the word
num = 0
game_over = False
while not game_over:
    guess = input("Guess a letter").lower()

    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num+=1
        guesses_left = 5 - num
        print(f"You have {guesses_left}")
        if num>= 5:
            print("You lost")
            game_over = True    

    print(display_word)

    if "_" not in display_word:
        print("you won")
        game_over = True 
