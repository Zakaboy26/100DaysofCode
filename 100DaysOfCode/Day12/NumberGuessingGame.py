import random
import art

lives = 0

print(art.logo)
print("Welcome to the number guessing game!")


def game_diff(tries):
    difficulty = input("Wanna play easy mode (10 guesses max) or hard(5 guesses max)? [E/H]:\n").upper()
    if difficulty == "E":
        tries += 10
    elif difficulty == "H":
        tries += 5
    else:
        print("Invalid input")
    return tries

def check_answer(guess, answer, num_tries):
    if guess == answer:
        print("Correct! You win :)")
        return num_tries, True

    elif guess > answer:
        print("Too high...")
        num_tries -= 1

    elif guess < answer:
        print("Too low...")
        num_tries -= 1

    return num_tries, False


def main_game():
    game_over = False
    num_tries = game_diff(lives)
    answer = random.randint(0, 99)

    while not game_over:
        guess = int(input("Enter a number from 1-100:\n"))

        num_tries, game_over = check_answer(guess, answer, num_tries)
        if not game_over:
            if num_tries > 0:
                print("Guess again")
                print(f"You got {num_tries} attempts remaining to guess the random number")
            else:
                print("You got 0 lives, you lose")
                game_over = True


main_game()
