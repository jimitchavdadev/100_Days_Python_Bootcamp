from random import randint

# List of words for the hangman game
hangman_words = {
    "easy": ["apple", "house", "chair", "pencil", "orange", "cloud", "tiger", "flower", "water", "beach"],
    "medium": ["glacier", "anchor", "forest", "castle", "pumpkin", "thunder", "cactus", "cobweb", "galaxy", "dragon"],
    "hard": ["labyrinth", "astronaut", "sapphire", "elephant", "paradox", "maverick", "whirlwind", "phoenix", "epiphany", "iceberg"]
}

difficulty = input("Choose difficulty: easy, medium, or hard? ").lower()
if difficulty not in hangman_words:
    print("Invalid difficulty level.")
    exit()

length = len(hangman_words[difficulty])
word = hangman_words[difficulty][randint(0, length - 1)]
fin = ["_" for _ in word]  # Create a list of underscores for the word
lives = 5

print(" ".join(fin))  # Display the initial state of the word

while "".join(fin) != word and lives > 0:
    letter = input("Enter a letter: ").lower()
    if letter in word:
        print("You guessed it correctly!")
        for index, char in enumerate(word):
            if char == letter:
                fin[index] = letter
        print(" ".join(fin))
    else:
        lives -= 1
        print(f"You guessed it wrong. Remaining lives: {lives}")

if "".join(fin) == word:
    print(f"Congratulations! You guessed the word: {word}")
else:
    print(f"Game over! The word was: {word}")
