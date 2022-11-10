
print("Welcome to wordle! A random word will be selected for you and you get to guess what it is.")
print("Correct letters will appear in lower case and correct letters in correct spaces will appear in capital letters.")
print("Goodluck!")
import random
play_again = "yes"
while play_again == "yes":
    list = ["beans", "toast", "jacob", "hairy"]
    magic_word = random.choice(list)
    print(" _ " * len(magic_word))
    guess = input("What is your guess? ").lower()
    count = 1
    while guess != magic_word:
        count = count + 1
        for i, letter in enumerate(magic_word):
        
            if magic_word[i] == guess[i]:
                print(guess[i].upper(), end=" ")
            elif guess[i] in magic_word:
                print(guess[i].lower(), end=" ")
            else:
                print("_", end=" ")
             
            
        print()
        guess = input("Oof, you're wrong...Guess again. ").lower()
    print(f"You guessed it in {count} guesses!")
    play_again = input("Want to play again? ")
print()
print("Thanks for playing!")
    # f{variable[index]}
