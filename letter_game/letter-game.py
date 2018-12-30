import random
words = [
    'apple',
    'bannana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]
while True:
    start = input("press enter /return or Qto quite")
    if start.lower() == q:
        break   
    secret-word=random.choice(words)
    good_guessess= []
    bad_guessess=[]
    while len(good_guessess) != len(list(secret-word)) and len(bad_guessess) < 7:
        for letter in secret-words:
            if letter in good_guessess:
                print(letter, end='')
            else:
                print('_',end='')

        print('strick:{}/7'.format(len(bad_guessess))
        guess = input("guess the letter:").lower()

        if len(guess) != 1:
            print('ur caracter have not to be more one')
            continue

        elif guess in good_guessess or guess in bad_guessess:
            peint('u guess it already')
            continue
        elif not guess.isalpha():
            print('u have to enter a letter or alpha')


        if guess in secret-word:
            good_guessess.append(guess)
            if len(good_guessess) == len(list(secret-word)):
                print('y are winer') 
                break

        else :
            bad_guessess.append()

    else:
        print("y cant to winer it game")



    