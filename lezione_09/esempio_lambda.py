add = lambda x,y: x / y
print(add(9,3))
print("-"*30)
# List of tuples
items = [(1, 'apple'), (3, 'banana'), (2, 'orange')]

# Sort by the second item of the tuple
sorted_items = sorted(items, key=lambda x: x[1])

print(sorted_items)
# Output: [(1, 'apple'), (3, 'banana'), (2, 'orange')]
print("-"*30)

numbers = [1, 2, 3, 4, 5]

# Using lambda to square each number
squared_numbers = map(lambda x: x**2, numbers)

# Convert the result to a list and print
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
print("-"*30)

numbers = [1, 2, 3, 4, 5, 6]

# Using lambda to filter out even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert the result to a list and print
print(list(even_numbers))  # Output: [2, 4, 6]
