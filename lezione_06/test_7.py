'''Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.'''

def check_parentheses(expression:str) -> bool:
    count:int = 0
    for i in expression:
       if i == "(":
        count+=1
       elif i == ")":
        count-=1
        if count <  0:
           return False
    return count == 0



print(check_parentheses("()()"))
print(check_parentheses("(()))("))
print(check_parentheses("((()))"))
print(check_parentheses(")("))
print(check_parentheses("(())"))