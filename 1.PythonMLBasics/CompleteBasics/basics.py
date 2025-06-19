from math import * ##Number
from Student import Student #Classes and Objects
from Chef import Chef ##inheritance
from ChineseChef import ChineseChef ##inheritance

#simple print
print("Hello world!")

#simple shape
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#data types in python
name = "Name"
age = 21
height = 170.5
is_true = True
print(name + " is already " + str(age) + " and is " + str(height) + " long and " + name + " is " + str(is_true) + ".")

##String
name = "String_Functions"
print(name.upper())
print(name.isupper())
print(name.upper().isupper())
print(len(name))
print(name[0])
print(name.index("i"))
print(name.index("Fun"))
print(name.replace("Functions", "Learning"))

##Number
print(-45.544)
print(3 + 4.45)
num = -5.45
print(abs(num))
print(pow(num, 2))
print(max(num, int(height)))
print(min(num, int(height)))
print(round(num))
print(floor(num))
print(ceil(num))
print(sqrt(81))

#inputting
'''some_info = input("Insert some info: ")
print("info from user: " + some_info)
num1 = input("Insert first num: ")
num2 = input("Insert second num: ")
result = float(num1) + float(num2)
print(result)'''

#Lists
colors = ["blue", "black", "white", "red", "black"]
print(colors)
print(colors[0])
print(colors[-1]) #indexing from the back
print(colors[1:])
print(colors[1:3])

##functions
numbers = [45, 54, 7, 15, 5]
colors.extend(list[str](numbers)) #colors.extend(numbers) is also okay, though pycharm is giving warning
print(colors)
colors.append("yellow")
print(colors)
colors.insert(1, "purple")
print(colors)
colors.remove("yellow")
print(colors)
'''colors.clear()
print(colors)'''
colors.pop()
print(colors)
print(colors.index("red"))
print(colors.count("black"))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
copied_list = colors.copy()
print(copied_list)

#Tuples - are unchangeable in python
coordinates = (5, 4)
print(coordinates[0])
list_of_tuples = [(5, 4), (34, 45), (15, 4)]
print(list_of_tuples)

#functions
def hello_function(user_name):
    print("Hello " + user_name)

hello_function("Name")

def cube(number):
    return pow(number, 3)

print(cube(3))

#if statement
is_tired = False
is_skilled = True
if is_tired and is_skilled:
    print("The user is both tired and skilled")
elif (not is_tired) or is_skilled:
    print("The user isn't tired or skilled")
else:
    print("The user is neither both tired and skilled nor not tired and skilled")

##comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("The max num is: " + str(max_num(5, 45, 32)))
# != // == // <= // >= // < // >

#Dictionaries
month_converter = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
print(month_converter)
print(month_converter[5])
print(month_converter.get(5))
print(month_converter.get(-1))

#loops

##While
i = 1
while i <= 10:
    print(i)
    i += 1

##For
for letter in "Word":
    print(letter)
for num in numbers:
    print(num)
for i in range(5):
    print(i)
for i in range(len(numbers)):
    print(numbers[i])

#exponent function
print(2**3) #exponent

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))

#2D lists
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12, 13, 14]
]
print(number_grid)
print(number_grid[1][1])

#Nested loops
for x in number_grid:
    for y in x:
        print(y)

#Exceptions
'''try:
    int_num = int(input("Enter a number: "))
    print(int_num)
    print(5/int_num)
except ZeroDivisionError as err:
    print("Divided by zero!")
    print(err)
except ValueError:
    print("Invalid input!")'''

#reading/writing files
'''with open("test.txt", "a") as create_test_file:
    create_test_file.write("Some content to be written\n")
    create_test_file.write("Some new content to be written")
create_test_file.close()'''

test_file = open("test.txt", "r")
print(test_file.readable())
print(test_file.read())
test_file.close()
test_file = open("test.txt", "r")
print(test_file.readline())
test_file.close()
test_file = open("test.txt", "r")
print(test_file.readlines())
test_file.close()

'''test_file = open("test.txt", "a") #"w" - overwriting/creating new file
test_file.write("new line\n")
test_file.close()'''

#Classes and Objects
student1 = Student("Tim", "IT", 4.5, False)
print(student1)
print(student1.gpa)

##Classes functions
print(student1.on_honor_roll())

##inheritance
chef1 = Chef("Blush", "Italian", "Ramen")
chef1.make_special_dish()
chef2 = ChineseChef("Li", "Zhang", "Udon", "Rice noodles")