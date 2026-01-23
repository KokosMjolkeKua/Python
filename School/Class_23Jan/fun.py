name = input("Enter your calling card: ")
print("Congratulations ",name," you have been selected to fight for the Kingdom of Crusalia.")
print("You are to report to the nearest soilder to start training.")
print("Welcome to the rest of your life.")

choice = input("Go to soilder? (yes/no): ")
if choice == "yes":
    print("You chose a life of death and will probably die...")
if choice == "no":
    print("You run for your life!")
    print("The soilder see you and chase after you!")
    choice = input("What do you do? (run/hide/give up)")
    if choice == "run":
        print("You continue running!")
        print("Suddenly you here a shot fired, you fall to the ground!")
        print("Bleading out.. You died.. Better than the military maybe?")
    if choice == "hide":
        print("You jump head first into the bushes!")
        print("Barely dodging the soilders as they sprint past you..")
        print("You escaped for now..")
        print("What do you do? ()")
    if choice == "give up":
        print("You raise your hands and yell: 'I Give UP'")
        print("The soilders capture you and take you to the military camp..")
        print("Because you tried to run, the officer decide to hang you..")
        print("Youll be an example for other people..")
        print("At least you had a purpose?")
    else:
        print("You didnt write a valid response..")
        print("Since the choice wassnt clear, the soilders just walk over to you and take you in..")
        print("Welcome to the school of cannon-fodder.")   
else:
    print("You didnt enter a valid response.")
    print("You just stand there, looking lost.")
    print("I guess youll stay here for a while...")                     