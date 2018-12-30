import random
secret_number = random.randint(1, 10)
guesses = []
guess = 0
def run_game(): 
    while len(guesses) < 5:
        try:
           guess = int(input("guess a number if u can?\n "))

        except ValueError:
               print("{} . its not number ".format(guess))
        else:
            if guess < secret_number:
                print("u have to pluss to the ur number")
            elif guess == secret_number:
                print("it s rigth congratulat")
                break

            elif guess > secret_number:
                print("u have to lost ur number")

            else:
                    # print hit/miss
                print("That's not it!")
                print("Here's your list:")
            for item in guesses:
                print(item)
        guesses.append(guess)
    else:
        print("You didn'y get it! My number was {}".format(secret_number))

    

    play_again = input("Do you want to play again? [Y/n]")
    if play_again.lower() != 'n':
        run_game()
    else:
        print("good luck!")


run_game()