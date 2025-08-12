from abc import ABC, abstractmethod 

# === Classes & Objects ===
# Classes: blueprint/template that describes the properties or behavior of an object
# Object: an instance of a class

class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
        
    def start_engine(self):
        print(f"Starting engine {self.make} {self.model}!")
        
toyota_car = Car("Toyota", "Camry", 2022)
toyota_car.start_engine()

chevy_car = Car("Chevrolet", "Tahoe", 2002)
chevy_car.start_engine()

# === Encapsulation ===
# Encapsulation: hiding away implementation details of an object from the users and only exposing necessary information to the public through methods
class BankAccount:
    def __init__(self, account_number: int, balance: int):
        self.__account_number = account_number
        self.__balance = balance
        
    def withdraw(self, amount):
        if amount > self.__balance: 
            print(f"Insufficient funds. Cannot withdraw ${amount}")
        else:
            self.__balance -= amount
            print(f"Succesfully withdraw ${amount}! Balance: ${self.__balance}")
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Succesfully deposit ${amount}! Balance: ${self.__balance}")
        
    def get_balance(self):
        return self.__balance
    
my_bank = BankAccount(101556, 100)
print("my_bank has $", my_bank.get_balance())
my_bank.withdraw(10)
my_bank.deposit(55)
# print(my_bank.__account_number) -> Encapsulation, you won't get the account number. Though you can break encapsulation by doing my_bank._BankAccount__account_number

# === Inheritance ===
# Inheritance: a mechanism that allows you to inhherit properties and methods of another class, called a superclass or parent class. The class that inherits is called the subclass or child class
class Occupations:
    def __init__(self, name: str, occupation_name: str, salary: int):
        self.name = name
        self.__occupation_name = occupation_name
        self.__salary = salary
    
    def give_raise(self, amount: int):
        self.__salary += amount
        
    def get_occupation_name(self):
        return self.__occupation_name

    def get_salary(self):
        return self.__salary
    
class Teacher(Occupations):
    def __init__(self, name, salary):
        super().__init__(name, "Teacher", salary)
    
    def teach(self):
        print(f"{self.name}, {self.get_occupation_name()} with salary ${self.get_salary()}, is teaching.")
        
class Firefighter(Occupations):
    def __init__(self, name, salary):
        super().__init__(name, "Firefighter", salary)
        
    def extinguish_fire(self):
        print(f"{self.name}, {self.get_occupation_name()} with salary ${self.get_salary()}, is extinguishing fire!")
        
tony = Firefighter("Tony", 95000)
tony.extinguish_fire()

dolores = Teacher("Dolores", 80000)
dolores.teach()

# === Polymorphism ===
# Polymorphism: the ability of an object to take on multiple forms.
class Document:
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Pdf(Document):
    def show(self):
        return "Show PDF content"
    
class Word(Document):
    def show(self):
        return "Show Word content"
    
docs = [Pdf(), Word()]
for doc in docs: 
    print(doc.show())
    
# === Abstraction ===
# Abstraction: the concept of showing only the necessary information to the outside world while hiding unnecessary details.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius
        
    def area(self):
        return (22/7) * self.radius ** 2
    
shape1 = Circle(7)
print(shape1.area())
shape2 = Rectangle(4, 5)
print(shape2.area())
    
"""
Abstraction vs. Polymorphism
Abstraction:
from abc import ABC, abstractmethod

class RemoteControl(ABC):
    @abstractmethod
    def power(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

Polymorphism:
class SonyRemote(RemoteControl):
    def power(self):
        print("Sony TV power toggled")

    def volume_up(self):
        print("Sony volume increased")

    def volume_down(self):
        print("Sony volume decreased")

class SamsungRemote(RemoteControl):
    def power(self):
        print("Samsung TV power toggled")

    def volume_up(self):
        print("Samsung volume increased")

    def volume_down(self):
        print("Samsung volume decreased")

Allows you to do:
def press_buttons(remote: RemoteControl):
    remote.power()
    remote.volume_up()
    remote.volume_down()

sony = SonyRemote()
samsung = SamsungRemote()

press_buttons(sony)      # Calls Sony's implementation
press_buttons(samsung)   # Calls Samsung's implementation

"""