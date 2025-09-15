# File: homework1. py
# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an interger, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a real number with a decimal component

c = 3j
print(c)
print(type(c)) # c is a complex, where a real and imaginary number are expressed

d = "hello"
print(d)
print(type(d)) #d is a string, a sequence of characters (a word, sentence, statement, etc)

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, an ordered sequence of multiple items in a single variable

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a key and corresponding values that can be modified

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, multiple items in a single variable enclosed by commas

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list of strings, an ordered sequence of multiple items in a single variable

i = True
print(i)
print(type(i)) # i is a boolean, it represents one of two possible values: True or False

j = None
print(None)
print(type(None))#j is a NoneType, an object that indicates no value 

k = [True, "blue", 12]
print(k)
print(type(k)) #k is a list, an ordered sequence of multiple items in a single variable


l = str(14)
print(str(14))
print(type(str(14))) #l is a string, a sequence of characters (a word, sentence, statement, etc)

m = 1e4
print(1e4)
print(type(1e4)) # m is a float, a real number with a decimal component

frozen_set_from_tuple = frozenset(g)
print(f"Frozenset from tuple: {frozen_set_from_tuple}")
print(type(frozen_set_from_tuple))

#3.2 BOOLEAN PROBLEMS
print(10>9) #True, 10 is greater than 9

print (10==9) #False, 10 does not equal 9

print (10<=9) #False, 10 is not less than or equal to 9

print (bool("abc")) #True, because the booelan contains a nonempty string

print(bool(123)) #True, because 123 is a non-zero interger

print(bool(["apple", "cherry", "banana"])) #True, 

print("hello")
print (bool(True)) #True, because this evaluates to True

print (bool(False)) #False, because the boolean evalautes to False

print(bool(0)) # False, because zero is associated with falsy values

print(bool("")) #False, because this is an empty sequence (string)

print(bool(" "))#True, because the space creates a non-epmty string

print(bool(())) #False, because this is an empty tuple

print(bool([])) #False because this is an empty list

print(bool({})) #False because this is an empty dictionary

print("Hello")

print(bool(True and False)) # False, because both conditions are not "true" so it is false

print(bool(True and True)) #True, because both conditions are true

print(bool(False and False)) #False because both conditions are false through the "And" operator

print(bool(True or False)) #True, because the operator runs true if at least one is true

print(bool(True or True)) #True, because the operator runs true if at least one (in this case both) are true

print(bool(False or False)) #False, because the operator runs false if neither boolean expression is true

print(bool(not(False))) #True, because the operator"not" runs opposite of false, in this case, true. 

print(bool(not(True))) #False, because the operator "not" runs the opposite of the expression, in this case, false. 

print((bool(4*2 ==8)))

print((bool(3<3)))

#3.3.1 Arithmetic Operators

print(10+5) #15, + performs addition

print (10-5) #5, - performs subtraction

print(2*4) #8, * performs multiplication

print(6/3) #2.0, / performs division

print(5 % 2) #1, %  finds the remainder of the division

print (3**2) #9, ** calculates 3 raised to the power of 2

print (15//2) #7, // divides numbers and rounds the result down to the nearest interger

# 3.3.2 Comparison Operators
print( 5==2 ) #False, == determines if two intergers are equal to one another

print( 10 !=10) #False, ! checks the operator and in this case it is asking if 10 is not equal to 10 but it is so it returns false.

print(2<5) #True, < checks if interger a is less then interger b 

print(12>5) #True, > checks if b is greater then a

print(5<=6) #True, <= operator if a is less than or equal to b

print(1>=10) #False, >= operator checks if 1 is greater than or equal to 10

# 3.3.3 Assignments Operators
x=5
x +=5 
x-=4 
x *=3  

#3.4 Strings
my_string = "hello"
print(my_string) #Prints: hello

print (my_string[0]) #prints: h

print (my_string[1]) #prints: e

print (my_string[2]) #prints: l

print (my_string[3]) #prints: l

print (my_string[4]) #prints: 0

print (my_string[-1]) #prints: 0

print(my_string[1:3]) #prints el

print(my_string[0:5:2]) #print hlo

print(len(my_string))

print(7*(my_string))

#3.4.1 Questions: 
name = "Oski"
print("Hello, my name is", name) #Hello, my name is Oski , it reuslts in the string and name variable Oski
print(f"Hello, my name is {name}") #Results in Hello, my name is Oski using an f-string

#3.5 Terminal Commands

# 1.) cd; changes directories. Use it to move from one folder to another. 
#Example: cd Desktop

# 2.) ls; shows all visible files
# Example: ls 

# 3.) ls-a: lists all files including hidden ones
# Examples: ls-a

#4.) mkdir: creates a new directory
#Example: mkdir new_python_decal_fa

#5) cat; displays the contents of a file 
#Example: cat python_decal_fa

#6) pwd: shows you whay directory you are currently on
# Example: cat python_decal_fa

#7) cd.. : Moves you to the parent directory (parent folder)
#Example: cd... sends me to python_decal_all

#8) cd. : just rfefers to current directory so 
#Example: python_decal_all would keeo me at python_decal_all

#9)cd ~: Is used by moving to the home directory on the terminal
#Example: cd ~ 

#10) cp: Is used to copy a file or folder by chooisng what to copy and where to place it
#Example: cp python_decal_spring26 python_decal_all

#11) mv : can be used to rename or move a file or folder by choosing what file or folder and what directory to place it
#Example: mv my_homework my_python_homework
#Example: mv file_here file_there

#12) rm : used to delete a file or directory without being able to undo it
# Example: rm unused_file

#13) clear : used to clear the screen on the terminal
#Example: clear

#14) grep: searches for a text within a afile (similar to control f)
#grep "python"  my_python_homework