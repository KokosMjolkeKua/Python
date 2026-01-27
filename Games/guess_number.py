import random
num = int(input("Guess a number between 1-5: "))


def guess(x):
    random_int = random.randint(1,5)
    if random_int == x:
        print("You guessed Correctly!")
    else:
        print("Try again!")    

guess(num)        