age=28
height=1.72
name="Ingur"
isStudent=True
print(name," is ", age, " years of age, and ",height,"m. ",isStudent)
print(f"Types: {type(age)}, {type(name)}, {type(height)}, {type(isStudent)}")


name=input("What is your name?")
age_text=input("What is your age?")

age=int(age_text)
birth_year=2026-age
print(f"{name}, you were born either in {birth_year} or {birth_year-1}.")

import sys
print(f"Memory: int size = {sys.getsizeof(age)} bytes.")

#This will crash:
#age=input("Age:")
#birth_year=2026-age

#Error handling:
try:
    age=int(input("Your age:"))
    print(f"Birth year: {2026-age} or {2025-age}")
except ValueError:
    print("Please enter a valid number!")



#Dynamic Excersice
x=5
print(f"x = {x}, type = {type(x)}, length = {len(str(x))}")     
x="Hello"
print(f"x = {x}, type = {type(x)}, length = {len(str(x))}")
x=[1,2,3]
print(f"x = {x}, type = {type(x)}, length = {len(str(x))}")
x=3.14
print(f"x = {x}, type = {type(x)}, length = {len(str(x))}")  

import sys
print("\n=== MEMORY COMPARISON ===")
print(f"int(42): {sys.getsizeof(42)} bytes")
print(f"float(3.14): {sys.getsizeof(3.14)} bytes")
print(f"str('hello'): {sys.getsizeof('hello')} bytes")