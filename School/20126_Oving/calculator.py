

#Looping
while True:
    num1=float(input("First number:  "))
    op = input("Operators (+, -, *, /): ")
    num2=float(input("Second number:  "))

    if op == "+":
        result = num1+num2
        print(f"{num1}{op}{num2} = {result}")
    elif op == "-":
        result = num1-num2
        print(f"{num1}{op}{num2} = {result}")    
    elif op == "*":
        result = num1*num2
        print(f"{num1}{op}{num2} = {result}")
    elif op == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            result=None
        else:
            result=num1/num2
            int_result=int(num1)/int(num2)
            print(f"{num1}{op}{num2} = {result}")
            print(f"Integer Division: {int(num1)}{op}{int(num2)} = {int_result}")    
    else:
        print("Invalid operator!")
        result=None
    again=input("Calculate again?  (yes/no): ")
    
    if again.lower() != "yes":
        print("Thanks for using the calculator!")
        break


