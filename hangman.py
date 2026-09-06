print("===== HANGMAN GAME =====")
import random
words = ["python", "computer", "programming", "developer", "keyboard"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0

display = ""

for letter in word:
    if letter in guessed_letters:
        display += letter
    else:
        display += "_"

print(display)

while True:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("Wrong guess!")

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print(display)
    print("Guessed letters:", " ".join(guessed_letters))
    print("Incorrect guesses:", wrong_guesses)
    print("Remaining attempts:", 6 - wrong_guesses)

    if "_" not in display:
        print("You win!")
        break

    if wrong_guesses == 6:
        print("Game over!")
        print("The word was:", word)
        break