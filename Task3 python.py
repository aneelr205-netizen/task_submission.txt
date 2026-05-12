# Task 5
# Conditional Statements 

marks = int(input("Enter marks:"))
if marks >= 90:
    print("Grade O")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 45:
    print("Grade C")
else:
    print("fail")



# Task 6 
# Nested if

age = int(input("Enter your age: "))
citizen = input("Are you a citizen ? (yes/no): ")
if age >=18:
    if citizen.lower() == "yes":
            print("Eligible to vote")
    else:
         print("Citizenship Required")
else:
    print("Not Eligible")


# Task 7
# Multiple conditions

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password":
    print("Login successful")
else:
    print("Invalid credentials")