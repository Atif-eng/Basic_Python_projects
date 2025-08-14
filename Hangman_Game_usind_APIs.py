# Hangman Game
# This is a simple implementation of the Hangman game using an API to fetch a random word
# The player has to guess the word by suggesting letters within a certain number of guesses
# The game ends when the player either guesses the word or runs out of guesses


# with APIs 
import requests
response = requests.get("https://random-word-api.herokuapp.com/word")
user=input('Enter a word: ')
word = response.json()[0]
print(word)
print(user)

if user == response:
    print('you guess the right Word')
else:
    print('you did not guess the right one')

