'''Write a function add_one(). It takes an integer as argument. The function adds 1 to the integer and returns it.
Write another function add_one_to_list(). It takes a list of integers as argument.
Define a variable new_list in this function.
Using a for loop, iterate through the argument list.
Using add_one(), fill new_list with integers from the argument list incremented
by 1.
Print new_list.'''

def add_one(a:int):
    return a+1
numbers = [1,2,4,5,6]
result = add_one(numbers)
new_list:list = []
def add_one_to_list(b:list) -> list:
    for n in numbers:
        new_list.append(add_one(numbers))
    return new_list


