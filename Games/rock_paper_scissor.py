import random
choice = str(input("Rock, Paper, Scissor?: "))


def rock_paper_scissor(choice):
    random_int = random.randint(1,3)
    if random_int == 1:
        # "Rock"
        if choice == "Rock":
            print("Its a Tie!")
        elif choice == "Paper":
            print("You win!")
        elif choice == "Scissor":
            print("You loose..")        
    elif random_int == 2:
        # "Paper"
        if choice == "Paper":
            print("Its a Tie!")
        elif choice == "Scissor":
            print("You win!")
        elif choice == "Rock":
            print("You loose..")
        print("You guessed Correctly!")
    else:
        # "Scissor"
        if choice == "Scissor":
            print("Its a Tie!")
        elif choice == "Rock":
            print("You win!")
        elif choice == "Paper":
            print("You loose..")   

rock_paper_scissor(choice)        