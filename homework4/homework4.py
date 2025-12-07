#HOMEWORK$
#3.1 Lis Operations 
fav_food = ["QuesaTacos", "pasta", "ramen", "pozole"]
print(fav_food[1])
"""
 I encountered this error:
 NameError: name 'prit' is not defined. Did you mean: 'print'?

 I fixed it by spelling "print" instead of "prit"
"""

print(fav_food[-1])

fav_food.append("burrito")

fav_food.insert(0, "apple")

del fav_food[2]

print(len(fav_food))

for food in fav_food:
    print(food.upper())

first_and_last_food = [fav_food[0], fav_food[-1]]
print(first_and_last_food)

if "potato" in fav_food:
    print("A potato!")
else:
    print("No potato!")


#3.2 Slicing and Striding
numbers = list(range(21)) 
#Personal note: Ramge goes to 20 bc it excludes 21.


def get_first_15(nums):
    return nums[:15]


def get_every_5th(lst):
    return lst[0:15:5]


def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]


step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

# print(get_first_15(numbers))
# print(get_every_5th(get_))
print (step1)
print(step2)
print(step3)


#3.3 Nested Lists
numbers_nested = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#3.3.1#1
print(numbers_nested[2])
'''
I got this error: 
IndexError: list index out of range
I fixed it by making 3 into 2. This is because I forgot python reads the first index as place zero and not one.
'''
#3.3.1 #2
print(numbers_nested[1][1])

#3.3.1 #3
numbers_nested.append([10, 11, 12])

#3.3.1 #4 
def sum_nested(nested):
    total = 0
    for row in nested:
        for num in row:
            total += num
    return total


print(sum_nested(numbers_nested))

#3.4 Create a 5x5 list

def list_fivebyfive():
    grid = []
    num = 1
    for r in range(5):
        row = []
        for c in range(5):
            row.append(num)
            num += 1
        grid.append(row)
    return grid


table = list_fivebyfive()


def replace_multiplesthree(grid):
    updated = []
    for row in grid:
        new_row = []
        for value in row:
            if value % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(value)
        updated.append(new_row)
    return updated

table2 = replace_multiplesthree(table)


def sum_without_questionmark(grid):
    total = 0
    for row in grid:
        for value in row:
            if value != "?":
             '''
             I got this error:
             TypeError: unsupported operand type(s) for +=: 'int' and 'str'
             I fixed it by adding the "if value != "?":
             This is because my past code was tring to add a string and interger. instead of using value != "?".
             '''
             total += value
    return total

print(sum_without_questionmark(table2))

#4 DICTIONARIES!!!
#4.1 Dictionary operations
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])

ages["Mira"] = 100

ages["Milana"] = 52

del ages["Mariam"]

for name, age in ages.items():
    print(name, age)

print("fav_function:", sum_nested(numbers_nested))