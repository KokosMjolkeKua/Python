temp = 37
if temp < 36.5:
    print("Hypothermia!")
elif temp > 38:
    print("Fever!") 
else:
    print("Normal")


timp = float(input("Please enter a number: "))
print("You entered: ", temp)

while True:
    tim = float(input("Please enter a number between 1-100: "))
    if temp < 36.5:
        print("Hypothermia!")
    elif temp > 38:
        print("Fever!") 
    else:
        print("Normal")

    con = input("Do you wish to continue? (yes,no) : ")
    if con == "yes":
        print("Nice!")
    else:
        print("Goodbye!")
        break;    