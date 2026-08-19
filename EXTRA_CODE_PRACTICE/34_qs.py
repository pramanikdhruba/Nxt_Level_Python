# Lambda Functions
# 1.Write a lambda function that adds two numbers and test it.
# 2.Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.

# 1.
add_two_numbers = lambda x , y : x+y
first_operation = add_two_numbers(5,11)
print(f"ADD : {first_operation}")

# 2.
first_list = [1,2,3,4,5]

square_of_list = list(map( lambda x : x*x, first_list))
print(f"SQUARE OF LIST : {square_of_list}")