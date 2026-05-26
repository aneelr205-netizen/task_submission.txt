class bottle:
    def __init__(self, color, height):
        self.color = color
        self.height = height 

    def open(self):
        print(f"{self.color} bottle is opened.")

    def close(self):
        print(f"{self.color} bottle is closed.") 

bottle1 = bottle("red", 20)
bottle2 = bottle("blue", 30)
print("==== Bottle class Example ====")
print("Bottle 1 color:", bottle1.color)
print("Bottle 1 height:", bottle1.height)

print("Bottle 2 color:", bottle2.color)
print("Bottle 2 height:", bottle2.height)

bottle1.open()
bottle1.close()

bottle2.open()
bottle2.close()


class student:
    def __init__(self, student_name, student_age, course):
        self.student_name = student_name
        self.student_age = student_age
        self.course = course

    def display(self):
        print("\nStudent Name:", self.student_name)
        print("Student Age:", self.student_age)
        print("Student Course:", self.course) 

        student1 = student("Alice", 20, "Python")
        student2 = student("Bob", 22, "Java")
        student3 = student("Charlie", 21, "Data Science")

        print("\n==== Student class Example ====")

        student1.display()
        student2.display()
        student3.display()

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

        def deposit(self, amount):
            self._balance += amount 
            print("Deposted Amount: {amount}")

        def withdraw(self, amount):
            if amount <= self.__balance:
               self.__balance -= amount 
               print("Withdrawn Amount: {amount}")
            else:
                print("Insufficient Balance!")

            def display_balance(self):
                print("Current Balance:", self.__balance)

                print("\n=====  Encapsulation Example =====")

            account = BankAccount(5000)

            account.display_balance()

            account.deposit(2000)
            account.display_balance()

            account.withdraw(1000)
            account.display_balance()

            print("Trying to access private variable:")
            try:
                print(account.__balance)
            except AttributeError as e:
                print("Error:", e)


class Animal:

    def sound(self):

        print("Animals make sounds")


class Dog(Animal):

    def bark(self):

        print("Dog barks: Bow Bow")

class Cat(Animal):

    def meow(self):

        print("Cat meows: Meow Meow")

print("\n===== Inheritance Example =====")


dog = Dog()
cat = Cat()

dog.sound()
dog.bark()

cat.sound()
cat.meow()


class Vehicle:

    def start(self):

        print("Vehicle starts")

class Bike(Vehicle):

    def start(self):

        print("Bike starts with self button")

print("\n===== Polymorphism - Method Overriding =====")

vehicle = Vehicle()

bike = Bike()

vehicle.start()

bike.start()


class Bird:

    def action(self):

        print("Bird flies in the sky")

class Airplane:

    def action(self):

        print("Airplane flies in the sky")


def perform_action(obj):

    obj.action()

print("\n===== Duck Typing Example =====")

bird = Bird()

plane = Airplane()

perform_action(bird)

perform_action(plane)



class CoffeeMachine:

    # Public method

    def make_coffee(self):

        self.__boil_water()

        self.__add_coffee()

        print("Coffee is ready!")

    # Private method

    def __boil_water(self):

        print("Boiling water...")

    # Private method

    def __add_coffee(self):

        print("Adding coffee powder...")

print("\n===== Abstraction Example =====")

machine = CoffeeMachine()

machine.make_coffee()

