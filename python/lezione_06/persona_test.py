'''from persona1 import Persona

fm:Persona = Persona("Philip", "Daoud", 26)

#print(fm.name,fm.last_name,fm.age)

# richiamare la funzione dispalyData della classe Pesrona per mostrare in output i dati relativi alla persona
fm.displayData()

print("------------")'''

from persona2 import Persona

fm:Persona = Persona()

#richiamo la funzione diplayData della classe persona per mostrare in output le informazioni relative all'oggetto
fm.displayData()

#modificare i dati della persona fm
print("------------")

fm.setName("Philip")

fm.setLast_name("Daoud")

fm.setAge(26)

fm.displayData()

print("----------")
print(fm.getName(), fm.getLast_name(), fm.getAge())
