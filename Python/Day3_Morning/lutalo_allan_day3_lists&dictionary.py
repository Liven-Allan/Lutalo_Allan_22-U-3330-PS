#Lists used to store multiple data in a single variable

# Example 1: Basic list compression
# Create a list of squares in range of 10
list_of_square = [x**2 for x in range(10)]
print(list_of_square)

# Exercise 1:
# Create a list of even numbers squares in the range of 20
list_of_even_squares = [x**2  for x in range(20) if x**2 % 2 ==0]
print(list_of_even_squares)

# Example 2: Dictionary compression
# Create a dictionary compression for favorite cars and count the length of characters
favorite_car = ['BMW', 'Jeep', 'Mercedes', 'Fordraptor']
car_length = {car: len(car) for car in favorite_car}
print(car_length)

# Exercise 2:
# Create a list of tuple where each tuple contains number and its cube for numbers between
# 1 and 10 using a dictionary compression
number_cubes_dict = {num: num**3 for num in range(1, 11)}
number_cubes_tuple = list(number_cubes_dict.items())
print(number_cubes_tuple)

