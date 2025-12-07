#HOMEWORKTHREE
#3.1
name = "valerie"
def say_goodbye(name):
    print("Goodbye,"+ name)
say_goodbye(name)

#3.2
pi = 3.14
radius = 29
area_circle = pi * (radius ** 2) #Are of a circle is pi times radius squared
print(area_circle)

#4.1 
#Return functions
def subtract(a, b):
    return a + b
print(subtract (a = 4, b = 54363))

def multiply(a, b): 
    return a * b
print(multiply(a = 64762, b = 76))

def divide(a, b):
    return a // b
print(divide (a = 156, b =78))

#5
#Deciding what to wear based on temperatures
temperatures = [55, 57, 53, 60, 63, 61, 62]
def get_min_and_max_temperatures(temperatures):
    print( "(" + str(min(temperatures)) + "," + str(max(temperatures)) + ")")
get_min_and_max_temperatures(temperatures)


#5.2
# Interge represents the day of the week 
# Monday = 1 ; Tuesday = 2 ; Wednesday = 3 ; Thursday = 4 ; Friday = 5; Saturday = 6 ; Sunday = 7 
def is_weekend(day):
    if day == 6 or day == 7:
        return True 
    else: 
        return False
print(is_weekend(7))

#5.3
distance = 72
fuelused = 20
def fuel_efficency_calculator(distance, fuelused): 
    return (distance/fuelused)
print(fuel_efficency_calculator(distance, fuelused))

#5.4
number = 12345
def encrypt_astrophysics(number):
    last_number = number % 10
    other_numbers = number // 10
    return (str(last_number)+ str(other_numbers))
print(encrypt_astrophysics(number))
# print(encrypt_astrophysics(number))

#6 Loops
#6.1 Oski stole your power
x = 6
y = 8

def powerthatworks(x, y):
    result = 1
    for i in range(0, y):
        result = result * x
    return result
print(powerthatworks(x, y))

#6.2 Min and Max w/ Loops
x = [1,2 , 3, 4, 5, 6] 

def valeriemin(x):
    min = x[0]
    for i in range(len(x)):
        if x[i]<min:
            min = [i]
    return min
print(valeriemin(x))


def valeriemax(x):
    max = x[0]
    for i in range(len(x)):
        if x[i]>max:
            max = x[i]
    return max
print(valeriemax(x))

#6.2.2 While loops

y = [1, 2, 3, 4, 5, 6, 7, 8]

def valeriemin(x):
    length = len(x)
    min_val = x[0]
    i = 0
    while i < length:
        if x[i] < min_val:
            min_val = x[i]
        i = i + 1
    return min_val

print(valeriemin(y))  



y = [1, 2, 3, 4, 5, 6, 7, 8]

def valeriemax(x):
    length = len(x)
    max_val = x[0]    
    i = 0
    while i < length:  
        if x[i] > max_val:
            max_val = x[i]
        i = i + 1
    return max_val

print(valeriemax(y))  


#6.3
x = 12345
def sumcalculator(integer):
    sum = 0
    length = len(str(integer))
    for i in range (0, length):
        sum += integer%10
        integer = integer // 10
    return sum
print(sumcalculator(x))

print(f"The result of Oski Stole Your Power(5.1) with x  = {6} and y = {8} is {1679616}.")

# x = 6
# y = 8

# def powerthatworks(x, y):
#     result = 1
#     for i in range(0, y):
#         result = result * x
#     return result
# print(powerthatworks(x, y))h

