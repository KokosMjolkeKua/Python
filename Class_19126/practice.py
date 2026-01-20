x=11
y=5

sum=x+y
print(sum)
sum=x-y
print(sum)
sum=x*y
print(sum)
sum=x/y
print(sum)
sum=x%y
print(sum)

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)


if x>y:
    print("x is greater than y")
if x<y:
    print("x is less than y")
if x==y:
    print("x is equal y")
if x!=y:
    print("x is not equal y")        


if x!=y and y<x:
    print("x is not equal to y, and y is smaller than x")    
if x>y or x==y:
    print("if x is larger than y , or x is equal to y")


#TEmperatures eks

temperature = 25
if temperature > 30:
    print("Its Hot!")
else:
    print("Its not too bad")        

#elif == else if

if temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
elif temperature > 10:
    print("Cool")
else:
    print("Issa cold..") 



#Excersise:
score = input("Give me a score bewteen 0-100:")
i = int(score)
if i <= 100 and i >= 0:
    if i >= 90:
        print("You got an A")
    elif i >= 80 and i <=89:
        print("You got a B")
    elif i >= 70 and i <=79:
        print("You got a C")
    elif i >= 60 and i <=69:
        print("You got a D")
    else:
        print("You got an F") 
else:
    print("It has to be a number between 0 and 100!")                           



#For loops
#starting number, end number, what it increases with for each turn

for i in range (3,10,2):
    print(i)

for i in range (5,15,3):
    print(i)


#for loops with strings
word = "Hello World"
for letter in word:
    print(letter)

for i in range(1,11):
    print(i*7)


#Excersise
    

#COnstant Functions

#Making function
def greet(name):
    print("Hello ", name)

#Calling function
greet("Alice")
greet("Thomas")        

def square(num):
    print("The Square root of: ", num, " is : ",num*num)

square(2)
square(16)
square(3)


#CElsius to Farenheit
C = int(input("Write the degree in Celsius:  "))
F = C * 9.5 + 32
print(C," degree Celsius is ", F, " Fareheit!")