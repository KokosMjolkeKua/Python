#Write aprogram
#reads temps in a loop
#stores in a list, dict or set
#calculates average

temps = ["Name:","Temperature:"]

for i in range(2):
    name = input("What is your name? : ")
    temp = float(input("What is the temp? : "))
    temps[i] = [name,temp]

print(temps)


tim = [37.3,37.2]
average = 0.0
for i in range(3):
    tom = int(input("Write temp: "))
    average += tom
    tim[i] = tom

print(tim)
print("Average temp: ",average)    


#TEACHER EXPLAIN
tmp = float(input("Enter temp: "))
temperatures = []
while True:
    temperatures.append(tmp)
    print("Average temp: ",sum(temperatures)/len(temperatures))
    tmp = float(input("Enter temp: "))
