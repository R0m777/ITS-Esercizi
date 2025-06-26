'''Un palindromo è una stringa che non cambia anche se letta al contrario, come la stringa "radar". 
Si scriva una funzione ricorsiva chiamata recursivePalindrome() che accetti in input un parametro di tipo stringa e restituisca True 
se l'argomento è un palindromo e False altrimenti.

Non si tenga conto degli spazi nella stringa e non si faccia distinzione tra lettere maiuscole e minuscole.

La funzione dovrebbe considerare palindrome le seguenti stringhe:
"radar"
"Anna"
" I topi non avevano nipoti"

La funzione non dovrebbe considerare palindrome le seguenti stringhe:
"casa"
"Marta"
"Roma e Amore"

Suggerimento: usare la funzione replace() per sostituire gli spazi con una stringa vuota.'''

def recursivePalindrome(stringa:str) -> bool:

    stringa = stringa.replace(" ", "").lower()

    if len(stringa) <= 1:
        return True

    if stringa[0] != stringa[-1]:
        return False

    return recursivePalindrome(stringa[1:-1])

p = recursivePalindrome(" I topi non avevano nipoti")
print(p)

p1 = recursivePalindrome("Radar")
print(p1)

p2= recursivePalindrome("casa")
print(p2)

p3= recursivePalindrome("Roma e Amore")
print(p3)