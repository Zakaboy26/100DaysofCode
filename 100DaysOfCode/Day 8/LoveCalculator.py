#MY SOLUTION WHICH MANUALLY CHECKS EACH LETTER:
def calculate_love_score(name1, name2):
    true_score = 0
    love_score = 0
    true_list = ['T', 'R', 'U', 'E']
    love_list = ['L', 'O', 'V', 'E']
    couple_name = (name1 + name2).upper()
    for char in couple_name:
        if char in true_list:
            true_score += 1
        if char in love_list:
            love_score += 1

    love_score = str(true_score) + str(love_score)
    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")


#ANGELA YU SOLUTION: SHE USES THE .COUNT METHOD WHICH IS CLEANER
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score("Kanye West", "Kim Kardashian")