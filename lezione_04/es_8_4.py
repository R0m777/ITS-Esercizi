'''Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''

def make_shirt(size="Large", message="I love Python"):
    print(f"the shirt is size {size}, and {message} is printed on it.")

make_shirt()
make_shirt(message="I love Python")
make_shirt(size="Small", message= "I hate Python")