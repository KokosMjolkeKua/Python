import random
win = 0
loose = 0
tie = 0

def rock_paper_scissor(choice):
    random_int = random.randint(1,3)
    if random_int == 1:
        # "Rock"
        if choice == "Rock":
            print("Its a Tie!")
            tie += 1
        elif choice == "Paper":
            print("You win!")
            win += 1
        elif choice == "Scissor":
            print("You loose..") 
            loose += 1     
    elif random_int == 2:
        # "Paper"
        if choice == "Paper":
            print("Its a Tie!")
            tie += 1
        elif choice == "Scissor":
            print("You win!")
            win += 1
        elif choice == "Rock":
            print("You loose..")
            loose += 1
        print("You guessed Correctly!")
    else:
        # "Scissor"
        if choice == "Scissor":
            print("Its a Tie!")
            tie += 1
        elif choice == "Rock":
            print("You win!")
            win += 1
        elif choice == "Paper":
            print("You loose..")
            loose += 1

while True:
    choice = input("Rock, Paper, Scissor?: ")
    rock_paper_scissor(choice)        
    print("SCORE:")
    print("Wins: ",win)
    print("Losses: ",loose)
    print("Ties: ",tie)
    x = input("Do you wish to continue? (yes/no) : ")
    if x == "no":
        break