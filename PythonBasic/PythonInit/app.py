# age = 20
# age = 30
# price = 19.95
# print(price)
# first_name = "Deepak"
# print(first_name)
# is_online = False
# print(is_online)
# print("Hello World")
# print(age)
#
# name = input("What is you name? ")
# print(name)
# print("Hello "+ name)

#input function return string
# birth_year = input("Enter ;your birth year: ")
# age = 2024 - int(birth_year); #doing type conversion string to int
# print(age)

#int(), float(), bool(), str() - type converters

# first_num = input("First: ")
# second_num = input("Second: ")
# sum = int(first_num) + int(second_num)
# input("Sum: "+ str(sum))

#in keyword
# course = "Python for Beginners"
# print('Python' in course)

#Strings are immutable in Python

#// and / divide operator
# // will return int value, whereas / will return float values

#** this is exponent operator. Say if you have 10 ** 3, this implies 10 to the power of 3

# x = 1
# #x++ will not work in this case if you want to increment, for that use below methodology
# x += 1 #similarly for + and - also
# print(x)

#and logical operator is used in place of && and or is used in place of || operator. not is used in place of ! in java

#conditional operators

# temperature = 35
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# print("Done")

def ifElseConditions():
    temperature = 8
    if temperature > 30:
        print("It's a hot day")
        print("Drink plenty of water")
    elif temperature > 20:
        print("it's a nice day")
    elif temperature > 10:
        print("it's a bit cold")
    else:  # only difference between java here is that, those intermediate else will be called as elif
        print("It's cold")
    print("Done")
# ifElseConditions()

def loopExmple1():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
# loopExmple1()


def whileExample():
    count = 0
    while count < 5:
        print(count)
        count += 1
# whileExample()

def switchCaseOrMatchExampel():
    lang = input("What programming language do you want to learn: ")

    match lang:
        case "JavaScript":
            print("You can become web developer")
        case "Python":
            print("You can become Data Scientist")
        case "Java":
            print("You can become Android developer")
        case _:
            print("The language doesn't matter, what matters is the solving problems")
# switchCaseOrMatchExampel()


