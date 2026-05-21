def addition(a, b):
    print("Addition = ", a + b)
addition(5, 3)

def largest(a, b, c):
    if a > b and a > c:
        print(a, " is the largest number")
    elif b > a and b > c:
        print(b, " is the largest number")
    else:
        print(c, " is the largest number")

largest(10, 20, 15)

def even_odd(num):
    if num % 2 == 0:
        print(num, " is an even number")
    else:
        print(num, " is an odd number")

even_odd(10)
even_odd(15)


def student(name, age):
    print("Student Name: ", name)
    print("Student Age: ", age)

student("RAM", 25)


def employee(name, salary):
    print("Employee Name: ", name)
    print("Employee Salary: ", salary)

employee("SITA", 50000)


def country(name, place="INDIA"):
    print(name, " is a country in ", place)
 
country("VINOD")

def sum_numbers(*args):
    total = sum(args)
    print("Sum of numbers: ", total)

sum_numbers(1, 2, 3, 4, 5)


def students_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ": ", value)

students_details(name="RAM", age=25, department="CSE")


def square(num):
    return num * num
result = square(5)
print("Square = ", result)