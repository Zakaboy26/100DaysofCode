import art
import random
import game_data

def initial_rand_q():
    initial_A = random.choice(game_data.data)
    initial_B = random.choice(game_data.data)
    while initial_B == initial_A:
        initial_B = random.choice(game_data.data)

    nameA = initial_A["name"]
    descA = initial_A["description"]
    countryA = initial_A["country"]
    followersA = initial_A["follower_count"]

    nameB = initial_B["name"]
    descB = initial_B["description"]
    countryB = initial_B["country"]
    followersB = initial_B["follower_count"]

    first_A = f"{nameA}, a {descA} from {countryA}"
    first_B = f"{nameB}, a {descB} from {countryB}"

    return first_A, first_B, followersA, followersB, initial_A, initial_B


def compare_first_q(first_A, first_B, followersA, followersB, game_score):
    print(f"Compare A: {first_A}\n{art.vs}\nAgainst B: {first_B}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # A wins?
    if followersA > followersB:
        correct_answer = "A"
    else:
        correct_answer = "B"

    if guess == correct_answer:
        game_score += 1
        print(f"Correct! Current Score is: {game_score}")
        return True, correct_answer, game_score
    else:
        print(f"Sorry that's wrong, final score: {game_score}")
        return False, correct_answer, game_score


def main_game():
    print(art.logo)
    game_score = 0

    # Get first two people
    first_A, first_B, followersA, followersB, dictA, dictB = initial_rand_q()

    game_over = False

    while not game_over:

        # Compare current A/B
        is_correct, correct_answer, game_score = compare_first_q(
            first_A, first_B, followersA, followersB, game_score
        )

        if not is_correct:
            game_over = True
            break

        # Winner becomes new A
        if correct_answer == "A":
            dictA = dictA
        else:
            dictA = dictB

        # Pick NEW random B not equal to A
        dictB = random.choice(game_data.data)
        while dictB == dictA:
            dictB = random.choice(game_data.data)

        # Extract new formatted values
        first_A = f"{dictA['name']}, a {dictA['description']} from {dictA['country']}"
        followersA = dictA["follower_count"]

        first_B = f"{dictB['name']}, a {dictB['description']} from {dictB['country']}"
        followersB = dictB["follower_count"]


main_game()
