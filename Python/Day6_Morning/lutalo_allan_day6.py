# Error Handling in python
# Exception handling with try, except, else, and finally
# Custome Exception

"""_summary_
Error handling in python it helps to handle unexpected situations and errors

1. try : contains code that might through an exception, 
NB  : if an exception occures the code in the try block is skipt or ignored.

2. except : catches and handles exceptions
NB        : You can specify different handlers for different exception types.

3. else : the code runs if no exception occurs
NB      : if no exception raised in the try-block it runs

4. finally : it runs whether an exception is raised/occurred or not
NB         : used for clean up actions

"""
# Example 1:
# Handle exception with division by zero
try:
    number = int(input("Enter a number : "))
    result = 20 / number

except ValueError:
    print("Invalid number! Please enter a valid number")    

except ZeroDivisionError:
    print("Error, division by zero is not supported") 

else :
    print(f"Result is {result}")

finally:
    print("Operation completed successfully ")  

# Exercise 1:
# Write a function that converts a string to an integer and handle both value error if the string
# can not be converted to an integer and the TypError if the input is not a string
# Use multiple except block to handle these exception.

def my_int_converter():
   
   try:
       result = int(input("Enter any string value : "))

   except TypeError:
       print("Please enter a number")

   except ValueError:
       print("Invalid type input")
   else :
    print(f"Your string is {result}")

   finally:
    print("Operation completed successfully ")     

my_int_converter()

# Custome exception handling
# Example 2: Exception raised for error in the input if funds are insufficient
class InsufficientFundsError(Exception):
   def __init__(self, balance, amount):
      self.balance = balance
      self.amount = amount
      self.message = f"Attempt to withdraw {self.amount} with only {self.balance} in account."
      super().__init__(self.message)

def withdraw(balance, amount) :
   if amount > balance:
      raise InsufficientFundsError()
   return balance - amount

# Custome exception handling    
try:
   balance = 20000
   amount_to_withdraw = 15000
   new_balance = withdraw(balance,amount_to_withdraw)

except InsufficientFundsError as e:
   print("Error: {e.message} ") 

else:
   print(f"Withdraw Successful! New balance is {new_balance}") 
   

# Note : 
"""_summary_
Defining a custome exception 

class CustomError(exception):
   # custom exception for specific error cases

   def __init__(self, message):
       super().message = message

### Raising a custom exception 
    def check_value(value):
      if value is < 0 or value :
         raise CustomeError ("value cannot be negative")         
      return value

# Handle exception with try, except, else and finally
try :    

result = check_value(-10)

except CustomError as e:
     print(f"Custom error caught: {e.message}")  

"""
# Exercise 2: 
# Create custom exception InvalidAgeError and write a function that raises this exception if the 
# given age is negative , handle this custom exception when calling a function   

class InvalidAgeError(Exception):
   def __init__(self, age):
      self.age = age
      self.message = print(f"Negative age is not allowed.")
      super().__init__(self.message)

def my_age(age):
   if age < 0:
      raise InvalidAgeError(age)
   print(f"Your age is {age}")
   
try:
   age = int(input("Enter your age : "))
   my_age(age)

except InvalidAgeError as e:
   print(f"Error : {e.message}")

finally:
   print("Operation Complete")      
      
         
               