import random

#gen random number 1-10
secret_num= random.randint(1,10)
guesses = []

def game():
    while len(guesses) < 3:
    #get a number guess from the player
        try:
            guess = int(input("Guess a number between 1 and 10:   "))
    #compare guess to the secret number

        except ValueError:
            print("{} isnt a number!".format(guess))
        else:
            if guess == secret_num:
                print("You won! Great Guess! The number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("My number is lower than {}".format(guess))
            elif guess > secret_num:
                print("My number is higher than {}".format(guess))
            else:
                print("Try again!")
            guesses.append(guess)
    else:
        print("You didn't get it. My number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/N")
    if play_again.lower() !='n':
        game()
    else:
        print("Bye!")
game()
#print hit/miss
