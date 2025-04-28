import random
import time
def posizioni(posizione_tartaruga:int, posizione_lepre:int):
    posizione = ["_"] * 70
    if posizione_tartaruga == posizione_lepre:
        posizione[posizione_tartaruga - 1] = "OUCH!!!"
    else:
        if posizione_tartaruga <= 70:
            posizione[posizione_tartaruga - 1] = "T"
        if posizione_lepre <= 70:
            posizione[posizione_lepre - 1] = "H"
    
    print(" ".join(posizione))


def passi_tartaruga():
    i = random.randint(1, 10)
    if 1 <= i <= 5:
        return 3
    if 6 <= i <= 7:
        return -6
    if 8 <= i <= 10:
        return 1


def passi_lepre():
    i = random.randint(1, 10)
    if 1 <= i <= 2:
        return 9
    if 3 <= i <= 4:
        return 0
    if i == 5:
        return -12
    if 6 <= i <= 8:
        return 1
    if 9 <= i <= 10:  
        return -2


def gara():
    posizione_T = 1  
    posizione_H = 1
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    
    while posizione_T < 70 and posizione_H < 70:
        posizione_T += passi_tartaruga() 
        posizione_H += passi_lepre()  
        
        if posizione_T < 1:
            posizione_T = 1
        if posizione_H < 1:
            posizione_H = 1
        
        if posizione_T > 70:
            posizione_T = 70
        if posizione_H > 70:
            posizione_H = 70
        
        posizioni(posizione_T, posizione_H)
        
        if posizione_T >= 70 and posizione_H >= 70:
            print("IT'S A TIE.")
            return
        elif posizione_T >= 70:
            print("TORTOISE WINS! || VAY!!!")
            return   
        elif posizione_H >= 70:
            print("HARE WINS || YUCH!!!")
            return
        
        time.sleep(0.2)
gara()

