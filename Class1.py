#import random

'''
x = ((8+5)*6/ 10)
print(x)


y = ((1+1)**(5-2))

print(y)
print(x, y)

fName = "Alamgir"
lName = "Khan"
fullName = fName + " " + lName
count = 3
print(fullName)
# print(fName * count)

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
print(name , age)

'''
'''
# Q1. Greet meesage
name = input("Enter your name: ")
print('Hello ' + name)
'''

# Q2. Wage Calculator
try:
    hrs = float(input("Enter Hours: "))
    ratePerHour = float(input("Enter Hourly Wage: "))

    if hrs < 40:
        grossPay = hrs * ratePerHour
        print("Hourly Wage: ", grossPay)
    else:
        newhrs = hrs - 40
        grossPay = hrs * ratePerHour
        overtime = newhrs * (1.5*ratePerHour)
        print("Hourly Wage more than 40 hours: ", grossPay + overtime)


except:
    print("Enter a Number.")

'''
# Q3. Temperature Convertor
cel = int(input("Enter Temperature in Celsius: "))
cel_to_Far = (cel * 9/5) + 32
print("Temperature in Fahrenheit: ", cel_to_Far)
'''
'''
# Score Calculator
try:
    score = float(input("Enter Score: "))

    if score > 0.0 and score < 1.0:
        if score >= 0.9:
            print("Grade: A")
        elif score >= 0.8:
            print("Grade: B")
        elif score >= 0.7:
            print("Grade: C")
        elif score >= 0.6:
            print("Grade: D")
        else:
            print("Fail")
    else:
        print("\nPlease enter between 0 and 1.")
except:
    print("\nPlease enter a number.")
'''
