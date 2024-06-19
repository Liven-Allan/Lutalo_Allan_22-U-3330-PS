# Inheritance and Polymorphism
"""_summary_

Inheritance and method overloading
Polymorphism and method resolution
order
Abstract classes and Inheritance

"""
# Inheritance and method overriding
"""_summary_
--description

Inheritance and method overriding allows a class(child class) inherit attributes and methods 
from another class(parent class)

Key Concepts
Base class (parent class) : Class whose properties are inherited by another class
Derived class (child class) : Class that inherits attributes and properties from another base class

"""

# Example 1: Syntax of inheritance 

# Create a class where a Dog inherits from animal and overrides with a speak method

class Animal:
    def speak(self):
        return 'Mwe Mwe Mwe'

class Dog(Animal):
    def speak(self):
        return 'Barks'
    
# Implementation of Inheritanced classes
animal = Animal()
dog = Dog()

print(animal.speak())
print(dog.speak())

# Polymorphism
# Allows objects of different classes to be treated as object of a common super class 
# Method resolution (MRO) : is order in which python looks for a method in a hierarchy classes

# Example 2:
# How polymorphism works in python

class Animal:
    def speak(self):
        return 'Mwoooo'
    
class Dog(Animal):
    def speak(self):
        return 'Barks'  

class Cat(Animal):
    def speak(self):
        return 'Meow'       

def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(Dog())  
make_animal_speak(Cat())  

# Exercise 1 :
# Create a simple application to manage different types of vehicles
# Implement a class to demonstarte inheritance and polymorphism
"""
Requirements
1. Base class to vehicle
Attributes: make, model, and year
methods: display_info()

2. Derived classes:
Car: inherit from vehicle
attribute: number_of_doors
overrides: display_info()

motorcycle: inherit from vehicle
Attribute: type_of_bike(cruiser, sport, touring)
overrides: display_info()

# Exercise 2: polymorphism
# Create a function that accepts a list of vehicle objects and call their display_info() method
# to print details of each vehicle
"""

# Exercise 1 : Inheritance
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Make : " f"{self.make}")
        print("Model : " f"{self.model}") 
        print("Year: " f"{self.year}")
    
class Car(Vehicle):
    def __init__(self,make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors    

    def display_info(self):
        super().display_info()
        print("Doors : " f"{self.number_of_doors}")    
    
class Motorcycle(Vehicle):
    def __init__(self,make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike   

    def display_info(self):
        super().display_info()
        print("Type :" f"{self.type_of_bike}")      
    
car = Car("Land Cruiser", "V8", 2005, 4)  
print(car.display_info()) 

motorcycle = Motorcycle("Honda","Ford", 2012, "Sport")
print(motorcycle.display_info())

# Exercise 2: Polymorphism
def display_vehicle_info(vehicle_list):
    for vehicle in vehicle_list:
        vehicle.display_info()
        print() # new line for readerbility

vehicles = [car, motorcycle]
print(display_vehicle_info(vehicles))  


# FILE HANDLING
"""
1.Working with text files
2.Handling CSV files
3.JSON and XML file processing

""" 
# 1. Working with text files, open, read, write and close
# Note : Python provides inbuilt function to handle text files.
# Key concepts
"""
-- description
Opening File: open() function (r, w, a, r+)
Reading File: read() function
Writing File: write() function
Closing File: close() function  
"""

# Example 3:
# Write a file and read a file
print("-------------Write a file and read a file---------------")
with open("doc1", "w") as file:
    # Writing to a text file
    file.write("I am Allan and i love Python.\n") 
    file.write("I use Python for automation.")

with open("doc1", "r") as file:
    # Reading from a text file
    content = file.read()
    print(content)

# Handling CSV files
print("------------Handling CSV files---------------")   

"""_summary_
CSV (Comma Separated Values) file widely for data exchange

key concepts 
Reading CSV files: Using 'csv.reader()'
Writing CSV files: Using 'csv.writer()'
DictReader and DictWriter: The class read and write csv files as dictionaries

"""
# Example 4:
# Writing and reading CSV file
import csv

# Writing to a csv file
with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'position', 'course'])
    writer.writerow(['Liven Allan', 'student', 'BSSE'])
    writer.writerow(['Lauben Mpaire', 'student', 'BSC'])
    writer.writerow(["Jeffff Geoff","lecturer","Recess"])

# Read from csv file
with open("data.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)    

# JSON and XML file processing
"""_summary_
JSON (JavaScript Object Notation)
XML (eXtensible Markup Language)
   : are formats used to structure data

Key concepts:
Loading JSON Data: Using json.load() for reading JSON file 
Dumping JSON Data: Using json.dump() for writing JSON file 
Parsing JSON Data: Using json.loads() for handling JSON string   

"""
# Write and Read a JSON file
print("---------------Write and Read a JSON file-------------")
import json

student_data = {
    "name" : "Allan",
    "course" : "BSSE",
    "year" :"year3"
}
# open jason file
with open('student_data.json', 'w') as json_file:
    json.dump(student_data, json_file)

# reading to json file
with open('student_data.json', 'r') as json_file:
    student_data = json.load(json_file)
    print(student_data)

# Exercise 2:
# Write and read XML file

# Using Elementtree
# Reading XML Files (part 1)

# importing element tree under the alias of ET
import xml.etree.ElementTree as ET

print("------------Reading XML Files Using Elementtree-------------")

# Passing the path of the xml document to enable the parsing process
tree = ET.parse("dict.xml")

# Getting the parent tag of the xml document
root = tree.getroot()

# printing the root (parent) tag of the xml document, along with its memory location
print("----------------printing the root (parent) tag of the xml document------------")
print(root)

# printing the attributes of the first tag from the parent 
print("---------------printing the attributes of the first tag-----------")
print(root[0].attrib)

# printing the text contained within first subtag of the 5th tag from the parent
print("--------------printing the text contained within first subtag of the 5th tag-----")
print(root[5][0].text)

# Writing  XML files (part 2)
print("-------------Writing  XML files using Elementtree-----------")

# This is the parent (root) tag onto which other tags would be created
data = ET.Element('chess')

# Adding a subtag named `Opening` inside our root tag
element1 = ET.SubElement(data, 'opening')

# Adding subtags under the `Opening` subtag
s_element1 = ET.SubElement(element1, 'E4') 
s_element2 = ET.SubElement(element1, 'D4') 

# Adding attributes to the tags under
# `items
s_element1.set('type', 'Accepted')
s_element2.set('type', 'Declined')

# Adding text between the `E4` and `D5` 
# subtag
s_element1.text = "Allan accepted"
s_element2.text = "Mathias declined"
 
# Converting the xml data to byte object, for allowing flushing data to file stream
byte_xml = ET.tostring(data)

# Opening a file under the name `items2.xml`, with operation mode `wb` (write + binary)

with open("items.xml", "wb") as f:
    f.write(byte_xml)
 
    
# Exercise 3:
# Using abstruction calculate the area and perimeter of a rectangle   
print("-----------Using abstruction to calculate the area and perimeter of a rectangle-------") 
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

length = 5
width = 3
rectangle = Rectangle(length, width)

print(f"Area of rectangle: {rectangle.area()}")
print(f"Perimeter of rectangle: {rectangle.perimeter()}")