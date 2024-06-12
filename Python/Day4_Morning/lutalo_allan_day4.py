# Dictionaries
# Creating and using Dictionaries
# Dictionary methods and operations

"""_Summary_

Dictionaries are a collection of keys and values
Unordered
Mutable
indexed by keys

"""
# Example1 : Creating a dictionary
# Create a dictionary for student pursuing software engineering,
# the key must be your name, age, technology interest, course and year of study.
# Put your own details

student_dictionary =  {
    'name': 'Lutalo Allan',
    'age': 23, 
    'technology_interest': 'Artificial Intelligence',
    'course': 'BSSE',
    'year': 2
      }

print(student_dictionary)
print(student_dictionary['name'])

# Exercise 
# Modify a your age and technology
student_dictionary['age'] = 30
student_dictionary['technology_interest'] = "Machine Learning"
print(student_dictionary)

# Example 2:
# Adding keys and values
student_dictionary['email'] = 'lutaloallan20@gmail.com'
print(student_dictionary)

# Exercise 2:
# Remove a key and value from dictionary
del student_dictionary['technology_interest']
print(student_dictionary)

# Common dictionary methods
"""_summary_

get()   // returns the value for the specified key if in dictionary. if not, it returns default value
update() // updates the dictionary with the elements from another dictionary
pop()   // removes the specified key and returns the corresponding value

"""
# Example 3: Use get method to get value
print(student_dictionary.get('technology'))

# Exercise 3;
# use update method to change value in age
print(student_dictionary.update({'age': 45}))
print(student_dictionary)

# Exercise 4:
# Use the if to check  if the key age is present in the dictionary and return its value
if 'age' in student_dictionary:
    print(student_dictionary['age'])

# keys(), values(), and items() methods
print(student_dictionary.keys())
print(student_dictionary.values())
print(student_dictionary.items())

"""_summary_
keys() returns a view of objects that dipsplays a list of all keys
values() returns a view of objects that dipsplays a list of all values
items() returns a view of objects that dipsplays a list of dictionary keys and values

"""

# Exercise 5:
# Use the update method to change the course and add a new key 'WhatsApp_Number' to the dictionary
student_dictionary.update({'course': 'Web Development', 'WhatsApp_Number': '0758869259'})
print(student_dictionary)
