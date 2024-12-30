from random import randint

print("Welcome to the number guessing game!")
print("I am thinking between 1 and 100")
answer = randint(1, 100)

def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
    elif user_guess < actual_answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {actual_answer}")
        return True  # The correct answer is guessed
    return False  # Incorrect guess

EASY = 10
HARD = 7

def set_difficulty():
    level = input("Choose a difficulty: easy or hard: ").lower()
    if level == "easy":
        return EASY
    else:
        return HARD

turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number")

guessed_correctly = False

while turns > 0 and not guessed_correctly:
    guess = int(input("Make a guess: "))
    guessed_correctly = check_answer(guess, answer)
    if not guessed_correctly:
        turns -= 1
        if turns > 0:
            print(f"You have {turns} attempts remaining.")
        else:
            print("You've run out of attempts. Game over!")
            print(f"The correct answer was {answer}.")
