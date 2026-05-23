# STRING FORMATING & STRING METHODS :
first_name = "Anil"
last_name = "Kumar"
city = "Chennai"
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"City: {city}")


text = " python programming "
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print(text.strip())
print(text.lstrip())
print(text.rstrip())


words = text.strip().split()
print(words)
joined = "-".join(words)
print(joined)


sample = "Python Programming"

print(sample.find("Program"))
print(sample.count("m"))
print(sample.startswith("Python"))
print(sample.endswith("ing"))


a = "12345"
b = "Python"
c = "Python123"
print(a.isdigit())
print(b.isalpha())
print(c.isalnum())

print("Hello\nworld")
print("python\tprogramming")

#ERRORS AND EXCEPTIONS HANDLING : 
# SYNTAX ERROR:
print("Hello")

# RUN TIME ERROR:
a = 10 
b = 0
print(a / b)

# LOGICAL ERROR:
a = 10
b = 20
average = a + b /2
print("Average:", average)


# Type Error:
a = "10"
b = 5
print(a + b)

# Value Error:
num = int("abc")
print(num)

# Zero Division Error:
a = 10
b = 0
print(a / b)

# Name Error:
print(value)

EXCEPTIUON HANDLING USING TRY, EXCEPT, FINALLY :
try:
num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input.")
finally:
    print("Execution completed.")


DIVISION PROGRAM HANDLING DIVISION-BY-ZERO :
try:
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))

print("Result: ", a / b)

expect ZeroDivisionError:
print("Error: Division by Zero is not allowed")

PROGRAM HANDLING INVALID DATATYPE ERROR :
try:
    age = int(input("Enter your age: "))
    print("Age is:", age)

except ValueError:
    print("Please enter numbers only")