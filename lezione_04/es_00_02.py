'''Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.'''

def check_length(stringa1):
    
    stringa1 = str("hello world")
    if len(stringa1) > 10:
        print(f"{check_length} is bigger than 10 characters.")
    elif len(stringa1) < 10:
        print(f"{check_length} is smaller tham 10 characters.")
    else:
        print(f"{check_length} is equal to 10 characters.")