'''Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.'''

def check_value(a:int = 5):
     if a > 5:
        return(f"{a} is bigger than 5.")
     elif a < 5:
        return(f"{a} is smaller than 5.")
     else:
        return(f"{a} is equal to 5.")
   

    