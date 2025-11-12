import random
import hangman_words
import hangman_art

lives = 6
word_list = hangman_words.word_list

print(hangman_art.logo)

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for number in range (word_length):
    placeholder += "_"
print(f"Word to guess: {chosen_word}")
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"***********************************************{lives} LIVES LEFT**************************")
    guess = input("Guess a letter:\n").lower()

    if guess in correct_letters:
        print("Already guessed! Try again")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True

            print(f"**************YOU LOSE, CORRECT ANSWER WAS {chosen_word} !!!************************")

    if "_" not in display:
        game_over = True
        print("******************YOU WIN************************")

stages = hangman_art.stages
print(stages[lives])