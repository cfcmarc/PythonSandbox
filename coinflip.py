import random
heads = 1
tails = 0
valid_guesses = [heads, tails]
correct_statement = "Correct! The coin flip landed "
incorrect_statement = "incorrect! The coin flip landed "
guess_list = []
coin_flip_otcme = random.randint(0,1)
for guess in valid_guesses:
    def coin_flip(user_guess):
        if coin_flip_otcme == user_guess:
            if user_guess == heads:
                return (correct_statement + heads + "!")
            else:
                return (correct_statement + tails + "!")
        elif coin_flip_otcme == 0:
            if user_guess == tails:
                return (correct_statement + tails + "!")
            elif user_guess == tails:
                return(correct_statement + tails + "!")

print(coin_flip(heads))
print(coin_flip(tails))
print(coin_flip("bat"))
print(coin_flip("Heads"))
print(coin_flip("Tails"))