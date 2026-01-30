name="Yeshy"
age=78
print(name," you are ", age, " years old..S")

#Docstring
def convert_celcius_to_fahrenheit(celsius):
    """ Converter function from Celsius to Fahrenheit
        Returns the value. """
    return (celsius * 9/5)+32

#always use docstring to showcase your thinking 


#Function int
def add(a,b):
    return a + b

print(add(2,3))
print(add(3.2,3.8))
print(add("Hello","Yeeshy"))


#Type Hints:
name:str="Alice"
age:int=30
temp:float=37.5
is_healthy:bool=True

#Functions
def add(a:int,b:int):
    """Add Integers"""
    return a + b

def get_patient(id:int) -> dict:
    """Return patient Record"""
    return {"Id":id,"Name":"Alice"}




#Class Example:
name="Hello"
print(name)

name:str="HI"
name=4 
#it still works because python has dynamic types, 
#but for humans we can see that something is wrong

#If you go to settings, search typechecking and choose basic, the variabel will 
#get an error, it will still run, but now you will know something is wrong

print(name)


#Lists:
temps:list[int]=[1,2,3] #if you put 3.3 you will get an error from pylance
print(temps)



#Logging: How to use!
import logging
#Tell logging what you want to logg¨
logging.basicConfig(
    level=logging.DEBUG,#This makes you decide what level you start on
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

#The levels start at DEBUG, then info,warning,error,critical.

logger=logging.getLogger(__name__)
logger.debug("Starting application")
logger.info("Patient loaded: Alice")
logger.warning("Temperature above 38 degrees celsius!")
logger.error("Database connection failed")



def addition(a,b):
    result= a+b
    print(result)
    return result

print(addition(14,5))

def test_add():
    result = add(3,7)
    assert result == 10
    #to test if the code is correct