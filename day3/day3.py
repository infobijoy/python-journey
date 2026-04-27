# Integer (int)
age = 25
year = 2026
followers = 1000

# Float (float)
price = 99.99
rating = 4.8
temperature = 36.5

#Math Operators
print(10 + 5)   # Addition
print(10 - 5)   # Subtraction
print(10 * 5)   # Multiplication
print(10 / 5)   # Division
print(10 % 3)   # Remainder
print(10 ** 2)  # Power
print(10 // 3)  # Floor division


# Store Results in Variables
price = 500
tax = 50
total = price + tax

print(total)


#Real World Examples========
#Freelance Earnings
project1 = 150
project2 = 300
total = project1 + project2

print(total)

#Monthly Expense
rent = 100
food = 80
internet = 20

total = rent + food + internet
print(total)


#Type Conversion============
#Sometimes we need to convert one data type to another, for example, we have two numbers as strings and we want to add them together, we need to convert them to integers first using int() function.
num1 = "10"
num2 = "20"

print(int(num1) + int(num2))

#Number to String
age = 25
print("My age is " + str(age))

#Core Concept: Strings vs Numbers
print("10" + "5")

#Division returns decimal
#Use // if you want whole number.
print(5 / 2)

#Forgot conversion
num = "10"
# print(num + 5) Wrong: this will give us an error because we are trying to add a string and an integer, we need to convert num to an integer first using int() function
print(int(num) + 5)