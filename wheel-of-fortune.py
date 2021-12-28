# %%
#Set up
player_turn = 1
next_turn = "yes"
bank = {1: 0, 2: 0, 3: 0}
round = 1
vowels = ["a", "e", "i", "o", "u"]
option = "spin"
game_over = "no"

wheel = ["BANKRUPT", "Lose a Turn", "100", "100", "100", "100", "100", "150", "150", "150", "150", 
"200", "200", "200", "200", "300", "300", "300", "450", "450", "600", "600", "700", "900"]

#using word dictionary file 
import random
f = open("words_alpha.txt")
word_list = f.read().split()
f.close()

def letter_guess():
    global guess, num_of_letters
    num_of_letters = 0
    for i in range(0,len(word)):
        if word[i] == guess:
            word_reveal[i] = guess
            num_of_letters += 1
    return word_reveal, num_of_letters

def turn_over():
    global player_turn, next_turn, option
    if player_turn < 3:
        player_turn += 1
    else:
        player_turn = 1
    next_turn = "yes"
    option = "none"
    return player_turn, option, next_turn

def option_word():
    global word, round, next_turn
    guess_word = str(input("Guess the word: "))
    if guess_word == word:
        print(f"Congratulations! {guess_word} is the correct word!")
        round += 1
        turn_over()
        next_turn = "no"
        return round, next_turn
    else:
        print(f"Sorry! {guess_word} is not the correct word.")
        turn_over()

#Game Start
print("Welcome to Wheel of Fortune!")

while game_over == "no":
    #Rounds 1 and 2
    if round < 3:
        print(f"\nRound {round}")
        word = random.choice(word_list)
        all_guesses = []
        word_reveal = ["_"] * len(word)
        next_turn = "yes"
        while next_turn == "yes":
            print(f"Player {player_turn}, Spin the wheel or guess the word?")
            option = str(input('Enter "spin" or "word": '))
            if option == "spin":
                print(f"\nPlayer {player_turn}, please spin the wheel.")
                wheel_spin = random.choice(wheel)
                option = "spin1"
                while option == "spin1":
                    if wheel_spin == "BANKRUPT":
                        print("You have landed on BANKRUPT. You lose all your money and your turn is over.")
                        bank[player_turn] == 0
                        turn_over()
                        break
                    elif wheel_spin == "Lose a Turn":
                        print("You have landed on Lose a Turn. Your turn is over.")
                        turn_over()
                        break
                    else:
                        print(f"You have landed on ${wheel_spin}")
                        option = "spin2"
                        while option == "spin2":
                            print(word_reveal)
                            print(f"All guesses: {sorted(all_guesses)}")
                            guess = str(input("Guess a consonant: "))
                            print(f"Guess a consonant: {guess}")
                            if len(guess) == 1 and guess not in vowels:
                                all_guesses.append(guess)
                                if word.find(guess) != -1:
                                    letter_guess()
                                    bank[player_turn] += (int(wheel_spin)*num_of_letters)
                                    print(f"Congratulations. That consonant appears in the word {num_of_letters} times. Your bank now has ${bank[player_turn]}.")
                                    print(word_reveal)
                                    option = "spin3"
                                    while option == "spin3":
                                        print("Spin the wheel, buy a vowel for $250, or guess the word?")
                                        option = str(input('Enter "spin", "vowel", or "word".'))
                                        if option == "spin":
                                            break
                                        elif option == "vowel":
                                            while option == "vowel":
                                                if bank[player_turn] < 250:
                                                    print("Error: You do not have enough money in the bank to buy a vowel. Please try again.")
                                                    option = "spin3"
                                                    break
                                                else:
                                                    print(word_reveal)
                                                    print(f"All guesses: {sorted(all_guesses)}")
                                                    guess = str(input("Guess a vowel: "))
                                                    print(f"Guess a vowel: {guess}")
                                                    if len(guess) == 1 and guess in vowels:
                                                        bank[player_turn] -= 250
                                                        print(f"Your bank now has ${bank[player_turn]}")
                                                        all_guesses.append(guess)
                                                        if word.find(guess) != -1:
                                                            letter_guess()
                                                            print(f"Congratulations. That vowel appears in the word {num_of_letters} times.")
                                                            print(word_reveal)
                                                            option = "spin4"
                                                            while option == "spin4":
                                                                print("Buy another vowel for $250, guess the word, or end your turn?")
                                                                option = str(input('Enter "vowel", "word", or "end turn".'))
                                                                if option == "vowel":
                                                                    if bank[player_turn] < 250:
                                                                        print("Error: You do not have enough money in the bank to buy a vowel. Please try again.")
                                                                        option = "spin4"
                                                                        continue
                                                                    else:
                                                                        option  = "vowel"
                                                                        continue
                                                                elif option == "word":
                                                                    option_word()
                                                                    break
                                                                elif option == "end turn":
                                                                    turn_over()
                                                                    print("Turn ended.")
                                                                    break
                                                                else:
                                                                    print(f"Error: {option} is not an option. Please try again.")
                                                                    option = "spin4"
                                                        else:
                                                            print(f"{guess} is not in the word.")
                                                            turn_over()
                                                            break
                                                    else:
                                                        print(f"{guess} is not a vowel. Please try again.")
                                        elif option == "word":
                                            option_word()
                                            break
                                        else:
                                            print(f"Error: {option} is not an option. Please try again.")
                                            option = "spin3"
                                else:
                                    print(f"{guess} is not in the word.")
                                    turn_over()
                                    break
                            else:
                                print(f"{guess} is not a consonant. Please try again.")
            elif option == "word":
                option_word()
                break
            else:
                print(f"{option} is not an option. Please try again.")
    else:
        #Round 3
        for i in range(1,4):
            if bank[i] == max(bank.values()):
                print(f"Congratulations, player {i}! You have earned the most money and will be moving on to the final round.")
                player_turn = i
        print(f"\nRound {3}: Final Round\nPlayer {player_turn}")
        word = random.choice(word_list)
        word_reveal = ["_"] * len(word)
        print('We will now reveal the letters "r", "s", "t", "l", "n", and "e" in the word.')
        for guess in ["r", "s", "t", "l", "n", "e"]:
            letter_guess()
        print(word_reveal)
        num_cons_guesses = 3
        while num_cons_guesses >= 1:
            guess = str(input("Guess a consonant: "))
            print(f"Guess a consonant: {guess}")
            if len(guess) == 1 and guess not in vowels:
                if word.find(guess) != -1:
                    letter_guess()
                num_cons_guesses -= 1
            else:
                print(f"{guess} is not a consonant. Please try again.")
        guess = str(input("Guess a vowel: "))
        print(f"Guess a vowel: {guess}")
        if len(guess) == 1 and guess in vowels:
            if word.find(guess) != -1:
                letter_guess()
            num_cons_guesses -= 1
        else:
            print(f"{guess} is not a vowel. Please try again.")
        print("Let's see how many of your guesses showed up in the word.")
        print(word_reveal)
        guess_word = str(input("Guess the word: "))
        if guess_word == word:
            print(f"Congratulations! {guess_word} is the correct word!\nPlayer {player_turn} has won the game!\nYour prize is $10,000!\nThanks for playing!")
            game_over = "yes"
        else:
            print(f"Sorry! {guess_word} is not the correct word.\nThe correct word was {word}.\nGame over.")
            game_over = "yes"



# %%
