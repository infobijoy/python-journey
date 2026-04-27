# Now user can type values live.
# input() function takes input from user and returns it as a string.
name = input("Enter your name: ")
print(name)

#Use prompts for clean UX.
city = input("Enter your city: ")
print("City:", city)

skill = input("Your skill: ")
print("You are skilled in", skill)

#Important Rule — Input = String
#Even if user types number:
#It becomes text.
num1 = input("First: ")
num2 = input("Second: ")

print(num1 + num2) #This will concatenate the two strings instead of adding them as numbers.

#Convert Input to Number
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

print(num1 + num2)

#Mini Real Projects ==> Age Greeting App & Profit Calculator
name = input("Name: ")
age = input("Age: ")

print("Hello", name)
print("You are", age, "years old")

income = int(input("Income: "))
expense = int(input("Expense: "))

profit = income - expense
print("Profit =", profit)