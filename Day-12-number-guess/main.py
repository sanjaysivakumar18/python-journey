import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return turns


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)
turns = set_difficulty()
game_over = False

while not game_over:
    print(f"You have {turns} attempts remaining.")

    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)

    if guess == answer:
        game_over = True
    elif turns == 0:
        print(f"You've run out of guesses. The answer was {answer}.")
        game_over = True
    else:
        print("Guess again.")