'''Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
oppure "Azione negata" a seconda delle condizioni che sono soddisfatte'''

def verifica(x,y,z) -> str:
    if x == True and (y | z == True):
        return "Azione permessa"
    else:
        return "Azione negata"